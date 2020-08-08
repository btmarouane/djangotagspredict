import pandas as pd
from sklearn.externals import joblib
import dill
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import re
from nltk.tokenize import word_tokenize
import os
import pickle
import traceback

from tagsystem.settings import BASE_DIR


class TagsClassifier:
    def __init__(self):
        with open(os.path.join(BASE_DIR, "ml/classifier/tags.txt"),"rb") as tagsfile:
            self.tags = pickle.load(tagsfile)

        self.stop_words = set(stopwords.words('english'))
        self.stemmer = SnowballStemmer("english")
        

    def striphtml(self,data):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, ' ', str(data))
        return cleantext


    def preprocessing(self,title,body):
        body = self.striphtml(body.encode('utf-8'))
        title = title.encode('utf-8')
        body = str(title) + " " + str(title) + " " + str(title) + " " + body
        body = re.sub(r'[^A-Za-z0-9#+.\-]+', ' ', body)
        words = word_tokenize(str(body.lower()))
        body = ' '.join(str(self.stemmer.stem(j)) for j in words if j not in self.stop_words and (len(j) != 1 or j == 'c'))

        body = pd.DataFrame([body])

        with open(os.path.join(BASE_DIR, "ml/classifier/tfidfvectorizer.pkl"),"rb") as tfidf:
            tfidfvectorizer = dill.load(tfidf)
        body = tfidfvectorizer.transform(body[0])

        return body

    def predict(self, data):
        model = joblib.load(os.path.join(BASE_DIR, "ml/classifier/final_model.pkl"))
        return model.predict(data)

    def postprocessing(self, prediction):
        return [self.tags[i] for i in range(0,1000) if prediction[0,i]==1]

    def compute_prediction(self, title, body):
        try:
            input_data = self.preprocessing(title, body)
            prediction = self.predict(input_data)
            prediction = self.postprocessing(prediction)
        except Exception as e:
            traceback.print_exc()
            return {"status": "Error", "result": str(e)}

        return prediction
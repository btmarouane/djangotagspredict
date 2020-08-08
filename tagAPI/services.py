from .models import Prediction
from tagsystem.wsgi import tagsClassifier
import json
def predict(token, title, body):
    prediction = Prediction(token=token, title=title, body=body, predicted=False)
    prediction.save()
    result = tagsClassifier.compute_prediction(title, body)
    prediction.predicted = True
    prediction.prediction = json.dumps(result)
    prediction.save()
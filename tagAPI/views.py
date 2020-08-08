
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import requests
from django_q.tasks import async_task
from .models import Prediction
import json
@api_view(["POST"])
def predict(request):
	stackOverFlowApi = "https://api.stackexchange.com/2.2/questions/{}?site=stackoverflow&filter=withbody"
	try:
		data = request.data

		if data['questionId'] == 0:
			title = data['title']
			body = data['body']
		else:
			response = requests.get(stackOverFlowApi.format(data['questionId']))
			if response.status_code is not 200 or not response.json()['items']:
				result = {'status': 404, 'result': "l'id {} n'existe pas sur l'api de stackoverflow".format(data['questionId'])}
				return Response(result, status=status.HTTP_404_NOT_FOUND)
			response = response.json()['items'][0]
			title = response['title']
			body = response['body']

		token = data['token']

		async_task("tagAPI.services.predict", token, title, body)

		#prediction = tagsClassifier.compute_prediction(title, body)

		result = {'status': 200, 'result': 'processing'}
		return JsonResponse(result, safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def result(request):
	token = request.data['token']
	prediction = Prediction.objects.get(token = token)
	jsonDec = json.decoder.JSONDecoder()
	if not prediction.predicted:
		result = {'status' : 200, 'result' : 'processing'}
	else:
		result = {'status' : 200, 'result' : jsonDec.decode(prediction.prediction)}
	return JsonResponse(result)
from rest_framework.views import APIView
from rest_framework.response import Response
from loki_app.models import MockEntry
import json
from cerberus import Validator
# Create your views here.
'''
class InjectView(APIView):
	mock_entries = {}

	def get(self, request):
		pass

	def post(self, request):
		request_body = request.data
		mock_entry = { **request_body }
		del mock_entry['url']
		if request_body['url'][1:] not in InjectView.mock_entries:
			InjectView.mock_entries[request_body['url'][1:]] = []
		InjectView.mock_entries[request_body['url'][1:]].append(mock_entry)
		return Response({})

class MockView(APIView):
	def get(self, request, url):
		pass

	def post(self, request, url=None):
		request_body = request.data
		matched_mock_entries = InjectView.mock_entries[url]
		for entry in matched_mock_entries:
			if Validator(entry['request']).validate(request_body):
				return Response(entry['response'])
		return Response({'message' : 'no matched mock found'})
'''
class InjectView(APIView):

	def post(self, request):
		request_body = request.data
		mock_entry = MockEntry(end_point=request_body['url'][1:], request=json.dumps(request_body['request']), response=json.dumps(request_body['response']))
		mock_entry.save()
		return Response({'status': 'OK', 'message': 'Mock inject success'})

class MockView(APIView):

	def post(self, request, url):
		if url:
			request_body = request.data
			mock_entries = MockEntry.objects.filter(end_point=url)
			for entry in mock_entries:
				try:
					if Validator(json.loads(entry.request)).validate(request_body):
						return Response(json.loads(entry.response))
				except Exception as e:
					entry.delete()
					print(e)
		return Response({'status': 'NOT_FOUND', 'message': 'There is no any matched mock found'})


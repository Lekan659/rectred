from rest_framework import serializers

class CaptchaSerializer(serializers.Serializer):
    token = serializers.CharField()

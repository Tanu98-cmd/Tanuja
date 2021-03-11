from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    img=serializers.ImageField()
    xml=serializers.FileField()


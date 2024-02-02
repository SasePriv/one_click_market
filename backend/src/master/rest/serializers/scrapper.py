from rest_framework import serializers


class ScrapSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=False)
    price = serializers.IntegerField()


class ScrapperSerializer(serializers.Serializer):
    scrap = serializers.ListField(child=ScrapSerializer())

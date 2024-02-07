from rest_framework import serializers


class ScrapSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=False)
    price = serializers.IntegerField(allow_null=False)
    image = serializers.CharField(allow_null=True)


class ScrapperSerializer(serializers.Serializer):
    list_items = serializers.ListField(child=ScrapSerializer())
    max_price = serializers.FloatField()
    min_price = serializers.FloatField()
    average_price = serializers.FloatField()

from rest_framework import serializers
from rest_framework.serializers import OrderedDict

class ItemSerializer(serializers.Serializer):
    item_number = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=15)
    type = serializers.CharField(max_length=30)
    group = serializers.CharField(max_length=30)
    standard = serializers.FloatField()
    standard_hc = serializers.FloatField()
    current = serializers.FloatField()
    current_hc = serializers.FloatField()

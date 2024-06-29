from rest_framework import serializers
class Aiquestserializers(serializers.Serializer):
    t_name = serializers.CharField(max_length=25)
    c_name = serializers.CharField(max_length=20)
    c_duration = serializers.IntegerField()
    seat = serializers.IntegerField()
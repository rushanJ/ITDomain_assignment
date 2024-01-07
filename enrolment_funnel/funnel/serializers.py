from rest_framework import serializers
from funnel.models import Funnel

# class FunnelSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     created = serializers.DateTimeField(read_only=True)
   
   
#     def create(self, validated_data):
#         """
#         Create and return a new `Funnel` instance, given the validated data.
#         """
#         return Funnel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Funnel` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance

class FunnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funnel
        fields = ['id', 'title', 'created']

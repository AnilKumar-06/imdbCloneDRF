from rest_framework import serializers
from .models import WatchList, StreamPlateform

    
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlateformSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='streamplateform-detail')
    watch_list = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlateform
        fields = "__all__"






# class WatchListSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     storyline = serializers.CharField(max_length=200)
#     #plateform = serializers.ForeignKey(StreamPlateform, on_delete=models.CASCADE)
#     active = serializers.BooleanField(default=True)
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return WatchList.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.created = validated_data.get('created', instance.created)
#         instance.save()
#         return instance


# class StreamPlateformSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length=100)
#     about = serializers.CharField(max_length=100)
#     website = serializers.URLField(max_length=100)

#     def create(self, validated_data):
#         return StreamPlateform.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.website = validated_data.get('website', instance.website)

#         instance.save()
#         return instance
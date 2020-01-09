from rest_framework import serializers

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


'''
Serializers -> JSON
Serializers -> validate data
'''

class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']
    
    # def validate_content(self, value):
    #     if len(value) > 1000:
    #         raise serializers.ValidationError("This is way too long.")
    #     return value

    def get_uri(self, obj):
        return "/api/users/{id}".format(id=obj.id)
    
    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("content or image is required.")
        return data

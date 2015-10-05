from rest_framework import serializers

from .models import Diff

class DiffSerializer(serializers.HyperlinkedModelSerializer):
    show = serializers.HyperlinkedIdentityField(view_name='diff-show', format='html')

    class Meta:
        model = Diff
        fields = ('url', 'old', 'new', 'show')

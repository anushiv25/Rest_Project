from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Snippet
		fields = ('url','owner', 'id', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url','id','username','snippets')
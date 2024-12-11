from rest_framework import serializers
from vocabularies.models import Vocabulary

class VocabularySerializer(serializers.ModelSerializer):

    class Meta():
        model = Vocabulary
        fields = ('id', 'name', 'description')

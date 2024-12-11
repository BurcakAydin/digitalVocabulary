from rest_framework.generics import ListCreateAPIView
from vocabularies.serializers import VocabularySerializer
from vocabularies.models import Vocabulary
from django.shortcuts import get_list_or_404
from profiles.models import Profile


# Create your views here.
class VocabularyListCreateView(ListCreateAPIView):
    serializer_class = VocabularySerializer
    
    def get_queryset(self):
        profile = self.request.user.profile #get_list_or_404(Profile, user=self.request.user)
        queryset = Vocabulary.objects.filter(profile=profile)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)
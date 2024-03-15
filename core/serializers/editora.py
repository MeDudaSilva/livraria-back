from rest_framework.serializers import ModelSerializer

from core.models import Editora

class EditoraSerialaizer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'
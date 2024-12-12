"""importes para criação das views"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import UserProfileExampleSerializer
from users.models import UserProfileExample


class UserProfileExampleViewSet(ModelViewSet):
    """cria uma viewset para o modelo UserProfileExample"""
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

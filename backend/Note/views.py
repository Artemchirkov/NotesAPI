from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

from Note.models import Note
from Note.serializers import NoteSerializer
from Note.permissions import IsOwnerOrReadOnly


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    # Явно указываем аутентификацию через JWT
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user

        # 1. Если пользователь АНОНИМ (не залогинен или без токена):
        if user.is_anonymous:
            return Note.objects.filter(is_public=True)

        # 2. Если пользователь АВТОРИЗОВАН:
        return Note.objects.filter(
            Q(owner=user) | Q(is_public=True)
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
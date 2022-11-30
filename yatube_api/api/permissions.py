from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import viewsets


class IsOwnerOrReadOnly(BasePermission):
    message = "Изменение чужого контента запрещено!"

    def has_object_permission(self,
                              request,
                              view: viewsets.ModelViewSet,
                              model):
        print(type(request))
        if request.method in SAFE_METHODS:
            return True

        return model.author == request.user

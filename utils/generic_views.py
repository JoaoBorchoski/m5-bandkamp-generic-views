from rest_framework.views import APIView, Request, Response
from .base_views import (
    DestroyBaseView,
    CreateBaseView,
    RetrieveBaseView,
    UpdateBaseView,
)


class GenericBaseView(APIView):
    view_queryset = None
    view_serializer = None
    url_params_name = "pk"


class CreateGenericView(CreateBaseView, GenericBaseView):
    def post(self, request) -> Response:
        return super().create(request)


class RetrieveGenericView(RetrieveBaseView, GenericBaseView):
    def get(self, request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)


class UpdateGenericView(UpdateBaseView, GenericBaseView):
    def patch(self, request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)


class DestroyGenericView(DestroyBaseView, GenericBaseView):
    def delete(self, request, *args, **kwargs) -> Response:
        return super().destroy(request, *args, **kwargs)

from rest_framework.views import Request, Response

from utils.base_views import (
    CreateBaseView,
    DestroyBaseView,
    RetrieveBaseView,
    UpdateBaseView,
)
from utils.generic_views import GenericBaseView


class RetrieveUpdateDestroyGenericView(
    RetrieveBaseView, UpdateBaseView, DestroyBaseView, GenericBaseView
):
    def get(self, request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> Response:
        return super().destroy(request, *args, **kwargs)

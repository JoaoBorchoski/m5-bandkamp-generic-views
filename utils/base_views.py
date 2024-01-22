from rest_framework.views import APIView, Request, Response, status

from django.shortcuts import get_object_or_404


class CreateBaseView:
    view_serializer = None

    def create(self, request) -> Response:
        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveBaseView:
    def retrieve(self, request, *args, **kwargs) -> Response:
        url_param = kwargs.get(self.url_params_name)
        obj = get_object_or_404(self.view_queryset, pk=url_param)
        serializer = self.view_serializer(obj)

        return Response(serializer.data, status.HTTP_200_OK)


class UpdateBaseView:
    def update(self, request, *args, **kwargs) -> Response:
        url_param = kwargs.get(self.url_params_name)
        obj = get_object_or_404(self.view_queryset, pk=url_param)

        serializer = self.view_serializer(obj, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class DestroyBaseView:
    def destroy(self, request, *args, **kwargs) -> Response:
        url_param = kwargs.get(self.url_params_name)

        obj = get_object_or_404(self.view_queryset, pk=url_param)
        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

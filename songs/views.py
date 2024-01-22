from songs.models import Song
from songs.serializers import SongSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from albums.models import Album


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 1


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = Album.objects.get(pk=self.kwargs["pk"])

        serializer.save(album=album)

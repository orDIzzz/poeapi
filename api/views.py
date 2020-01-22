from django.shortcuts import render
from .models import Item
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from api.serializers import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
# from api import dp

class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class CategoryView(ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


#
# class UpdateView(APIView):
#     def get(self, request):
#         return Response(dp.last_update)

class StatusView(APIView):
    def get(self, request):
        return Response(self.kwargs)
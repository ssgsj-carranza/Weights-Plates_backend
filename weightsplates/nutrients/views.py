from django.shortcuts import render
from .models import Nutrients
from .serializers import NutrientsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class NutrientsList(APIView):

    def get(self, request):
        nutrients = Nutrients.objects.all()
        serializer = NutrientsSerializer(nutrients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NutrientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NutrientsDetail(APIView):

    def get_object(self, pk):
        try:
            return Nutrients.objects.get(pk=pk)
        except Nutrients.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        nutrients = self.get_object(pk)
        serializer = NutrientsSerializer(nutrients)
        return Response(serializer.data)

from django.shortcuts import render
from .models import Supplements
from .serializers import SupplementSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

class SupplementList(APIView):

    def get(self, request):
        supplements = Supplements.objects.all()
        serializer = SupplementSerializer(supplements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplementDetail(APIView):

    def get_object(self, pk):
        try:
            return Supplements.objects.get(pk=pk)
        except Supplements.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        supplements = self.get_object(pk)
        serializer = SupplementSerializer(supplements)
        return Response(serializer.data)

from rest_framework.views import APIView
from .serializers import AboutusSerializer
from rest_framework.response import Response
from .models import *


class AboutusView(APIView):
    def get(self, request):
        queryset = Aboutus.objects.all()
        serializer = AboutusSerializer(queryset, many=True)
        return Response(serializer.data)


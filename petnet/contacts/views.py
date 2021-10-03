from rest_framework.views import APIView
from .serializers import ContactSerializer
from rest_framework.response import Response
from .models import *


class ContactView(APIView):
    def get(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

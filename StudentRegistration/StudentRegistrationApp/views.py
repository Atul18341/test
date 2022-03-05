from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializers
from .models import Registration
# Create your views here.
class RegistrationView(APIView):
    def get(self,request):
        queryset=Registration.objects.all()
        serializers=RegistrationSerializers(queryset,many=True)
        return Response(serializers.data)

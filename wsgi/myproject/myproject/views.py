from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from serializers import UserSerializer, GroupSerializer
from calculo.pago import Pago, PagoSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CalculoView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        return Response({'received data': request.data})


pagos = {1: Pago(id = 1, rfc='AAAA850101000', plaza=100, unidad='700', grupo='presupuestal', \
                nivel='N33', nombramiento='confianza', jerarquia='mando medio', \
                sueldo=8357.21, compensacion=40970.45, conceptospago='lista conceptos', \
                conceptospagados='lista conceptos', pensiones='lista pensiones', sobresueldo=0)}

def get_next_pago_id():
    return max(pagos) + 1

class PagoViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = PagoSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
        serializer = PagoSerializer(
            instance=pagos.values(), many=True)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            pago = serializer.save()
            pago.id = get_next_pago_id()
            #
            # CALCULAR PAGO
            #
            pagos[pago.id] = pago
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

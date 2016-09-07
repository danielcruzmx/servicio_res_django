from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from serializers import UserSerializer, GroupSerializer, IsptSerializer, ReglaSerializer, ConstanteSerializer
from calculo.pago import Pago, PagoSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from calculo.models import Ispt, Regla, Constante
from calculo.calc import calc

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

class IsptViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ispt.objects.all().order_by('-tipo', 'linferior')
    serializer_class = IsptSerializer

class ReglaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Regla.objects.all().order_by('id')
    serializer_class = ReglaSerializer
    
class ConstanteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Constante.objects.all()
    serializer_class = ConstanteSerializer    
    

pagos = {1: Pago(  id = 1, rfc='DATO  EXEMPLO', plaza=100, unidad='700', grupo='presupuestal', \
                   nivel='N33', nombramiento='confianza', jerarquia='mando medio', \
                   sueldo=8357.21, compensacion=40970.45, sobresueldo=0, \
                   conceptospago=[
                       {"tipo": "D", "concepto": "51", "valor": 275.13},\
                       {"tipo": "D", "concepto": "82", "valor": 10.0}
                   ], \
                   pensiones=[
                       {'numero':1, "beneficiario" : "NOMBRE BENEFICIARIO", "monto": 0, "porcentaje": 40.0, "conceptos": "P07|P06|D01|..." }
                   ],
                   conceptospagados=[] \
                )
        }

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
            x = calc(pago)
            pago.setconceptospagados(x)
            #
            #pagos[pago.id] = pago
            pagos[2] = pago
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

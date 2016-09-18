from rest_framework import serializers

JERARQUIAS = (
    'mando medio',
    'personal de mando',
    'personal de mando superior',
    'servidor publico superior',
    'superior',
    'personal operativo',
    'operativo',
    'personal de enlace',
    'enlace',
    'enlace alta responsabilidad',
    'honorarios',
    'personal de honorarios'
)

NOMBRAMIENTOS = (
    'base',
    'personal de base',
    'confianza',
    'personal de confianza'
    'honorarios',
    'personal de honorarios'
)

GRUPOS = (
    'presupuestal',
    'personal estructura',
    'estructura',
    'personal eventual',
    'eventual',
    'personal en el extranjero'
)

class Pago(object):

    def __init__(self, **kwargs):
        for field in ('id', 'rfc', 'plaza', 'unidad', 'grupo', 'nivel', 'nombramiento', \
                      'jerarquia','sueldo','compensacion','sobresueldo', 'conceptospago',\
                      'conceptospagados','pensiones'):
            setattr(self, field, kwargs.get(field, None))

    def setconceptospagados(self, conceptospagados):
	  self.conceptospagados = conceptospagados

class ConceptoSerializer(serializers.Serializer):
    tipo = serializers.CharField(max_length=2)
    concepto = serializers.CharField(max_length=4)
    valor = serializers.DecimalField(max_digits=10, decimal_places=5)

class ConceptoPagadoSerializer(serializers.Serializer):
    tipo = serializers.CharField(max_length=2)
    concepto = serializers.CharField(max_length=4)
    descripcion = serializers.CharField(max_length=40)
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)

class PensionSerializer(serializers.Serializer):
    numero = serializers.IntegerField()
    beneficiario = serializers.CharField(max_length=40)
    monto = serializers.DecimalField(max_digits=10, decimal_places=2)
    porcentaje = serializers.DecimalField(max_digits=10, decimal_places=2)
    conceptos = serializers.CharField(max_length=200)

class PagoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)    
    rfc = serializers.CharField(max_length=13)
    plaza = serializers.IntegerField()
    unidad = serializers.CharField(max_length=3)
    grupo=serializers.ChoiceField(choices=GRUPOS, default='presupuestal')
    nivel=serializers.CharField(max_length=20)
    nombramiento=serializers.ChoiceField(choices=NOMBRAMIENTOS, default='confianza')
    jerarquia=serializers.ChoiceField(choices=JERARQUIAS, default='mando medio')
    sueldo=serializers.DecimalField(max_digits=10, decimal_places=2)
    compensacion=serializers.DecimalField(max_digits=10, decimal_places=2)
    sobresueldo=serializers.DecimalField(max_digits=10, decimal_places=2)
    conceptospago=ConceptoSerializer(many=True)
    conceptospagados= serializers.ListField()
    #conceptospagados= ConceptoPagadoSerializer(many=True)
    #pensiones=serializers.CharField(max_length=20)
    pensiones=PensionSerializer(many=True)
    
    def create(self, validated_data):
        return Pago(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
    
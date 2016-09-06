from rest_framework import serializers

JERARQUIAS = (
    'mando medio',
    'superior',
    'operativo',
    'enlace'
)

NOMBRAMIENTOS = (
    'base',
    'confianza'
)

GRUPOS = (
    'presupuestal',
    'eventual'
)

class Pago(object):

    def __init__(self, **kwargs):
        for field in ('id', 'rfc', 'plaza', 'unidad', 'grupo', 'nivel', 'nombramiento', \
                      'jerarquia','sueldo','compensacion','sobresueldo', 'conceptospago',\
                      'conceptospagados','pensiones'):
            setattr(self, field, kwargs.get(field, None))

    def setconceptospagados(self, conceptospagados):
	  self.conceptospagados = conceptospagados

#class ConceptoSerializer(serializers.Serializer):
#    cve = serializers.CharField(max_length=13)
#    valor = serializers.DecimalField(max_digits=10, decimal_places=2)

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
    conceptospago=serializers.CharField(max_length=20)
    conceptospagados= serializers.DictField()
    pensiones=serializers.CharField(max_length=20)
    
    def create(self, validated_data):
        return Pago(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
    
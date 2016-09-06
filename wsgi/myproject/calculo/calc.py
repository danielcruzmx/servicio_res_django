__author__ = 'daniel_cruz'

from models import Ispt, Constante, Regla
import collections

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def is_number(s):
  n=0
  try:
     n=float(s)
     return n
  except ValueError:
     return n

def existe(clave, param):
    ret = False
    for p in param:
       if p == clave:
          ret = True
          break
    return ret

def validaconcepto(nivel, regla):
    ret =  False

    if regla.jerarquias == 'todos':
       ret = True
    elif nivel.jerarquia.upper() in regla.jerarquias.upper():
       ret = True
    else:
       ret = False

    if regla.nombramientos == 'todos':
       ret = True
    elif nivel.nombramiento.upper() in regla.nombramientos.upper():
       ret = True
    else:
       ret = False

    if regla.niveles == 'todos':
       ret = True
    elif nivel.nivel[:1] in regla.niveles:
       ret = True
    else:
       ret = False

    return ret

def evalua(expresion):
    try:
        valor = eval(expresion)
        return valor
    except (NameError, SyntaxError):
        print "Error: Al evaluar la expresion " + expresion
        return -1

def constantes():
    vars = {}
    res = Constante.objects.all()
    for r in res:
        vars.update({r.constante:r.valor})
    return vars

def calc(pago):

    # AGREGA CONSTANTES
    var_s = {}
    var_s.update(constantes())

    # AGREGA CONCEPTOS INICIALES
    var_s.update({'sueldo': pago.sueldo})
    var_s.update({'compensacion': pago.compensacion})
    var_s.update({'incentivo': pago.sobresueldo})

    lstreglas = Regla.objects.order_by('id').all()

    # EVALUA Y AGREGA CONCEPTOS FIJOS
    for r in lstreglas:
        if r.tipo_calculo == 'fijo':
            clave = r.variable
            ex = r.formula.format(**var_s)
            valor = evalua(ex)
            if valor == -1:
                valor = 0
                clave = clave + '.error'
            else:
                if not validaconcepto(pago, r):
                    valor = 0
            var_s.update({clave:valor})

    # RECUPERA LOS CONCEPTOS VARIABLES Y SU VALOR
    variables = {}
    #for c in pago.conceptospago:
    #    clave = c['tipocpto'] + c['cpto']
    #    if is_number(c['porcentaje']):
    #        if c['porcentaje'] > 0:
    #            valor = c['porcentaje'] / 100.00
    #        else:
    #            valor = 0
    #    else:
    #        valor = c['monto']
    #    variables.update({clave: valor})

    # EVALUA Y AGREGA CONCEPTOS VARIABLES
    for r in lstreglas:
        if r.tipo_calculo == 'variable':
            clavevariable = r.variable
            claveconcepto = r.tipo + r.concepto
            if existe(claveconcepto,variables):
                # EVALUA CONCEPTO
                var_s.update({'valor': variables[claveconcepto]})
                ex = r.formula.format(**var_s)
                valor = evalua(ex)
                if valor == -1:
                    valor = 0
                    clavevariable = clavevariable + '.error'
            else:
                valor = 0
            if not validaconcepto(pago, r):
                valor = 0
            var_s.update({clavevariable:valor})

    # EVALUA Y AGREGA CONCEPTOS DE CALCULO
    for r in lstreglas:
        if r.tipo_calculo == 'calculo':
            clavevariable = r.variable
            ex = r.formula.format(**var_s)
            valor = evalua(ex)
            if valor == -1:
                valor = 0
                clavevariable = clavevariable + '. error'
            else:
                if not validaconcepto(pago, r):
                    valor = 0
            var_s.update({clavevariable:valor})

    #print var_s

    # GUARDA RESULTADOS EN ARREGLO DE PAGADOS
    resul = {}
    n = 1
    for r in lstreglas:
        try:
            #print r.variable
            v = round(var_s[r.variable],2)
            #print r.descripcion
            if v > 0:
                resul.update({ n: {'Descripcion': r.descripcion, 'Valor':v, 'Concepto': r.codigo_salida}})
                n = n + 1
            #print resul
        except:
            pass
    return collections.OrderedDict(sorted(resul.items()))
    #print resul
    #return resul

def ispt(monto):
   res = 0.0
   rango = Ispt.objects.filter(\
            tipo='ispt', \
            fecha_fin='01/01/2099').\
            all().order_by('id')
   if rango:
      for r in rango:
         if float(r.linferior) <= monto and float(r.superior) >= monto:
            res = (monto-float(r.linferior))*float(r.excedente)/100.0+float(r.cuota)
            return res
   else:
      return res

def bruto(monto):
   res =0.0
   rango = Ispt.objects.filter(\
            tipo='bruto', \
            fecha_fin = '01/01/2099').\
            all().order_by('id')
   if rango:
      for r in rango:
         if float(r.linferior) <= monto and float(r.superior) >= monto:
            res = (monto-float(r.cuota))/float(r.bruto)
            return res
   else:
      return res

def ibruto(base, monto):
   isr = ispt(base)
   isrs = bruto(base-isr+monto)
   return isrs-base-monto

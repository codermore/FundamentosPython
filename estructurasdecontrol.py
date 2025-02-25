calificacion = 85


if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")


# Otra forma mas eficiente de esctructurar elif encadenados es la siguiente:

esUsuarioActivo = True
esUsuarioSubscripto = True
esUsuarioPago = True

def mala_estructura ():   
   if esUsuarioActivo:
      if esUsuarioSubscripto:
         if esUsuarioPago:
            print("respuesta satisfactoria")
         else:
            print("no es usuario pago")
      else:
         print("no es usuario subscripto")
   else:
      print("no es usuario activo")

mala_estructura()

#Ahora de una manera mas legible y escalable (?)

def buena_estructura():
   if not esUsuarioActivo:
      return print("no es usuario activo")
   
   if not esUsuarioSubscripto:
      return print ("no es usuario subscripto")
   
   if not esUsuarioPago:
      return print ("no es usuario pago")
   
   return print("respuesta satisfactoria")

buena_estructura()

       
            
from coche import Coche;
from bicicleta import Bicicleta;
from camioneta import Camioneta;
from motocicleta import Motocicleta

Vehiculos = []

c = Coche("azul", 4 , 150, 1200)
b = Bicicleta("verde", 2, "urbana")
cm = Camioneta("rojo", 4, 150, 1200,450)
m = Motocicleta("amarillo", 2,"urbana",150, 250)

Vehiculos.append(c)
Vehiculos.append(b)
Vehiculos.append(cm)
Vehiculos.append(m)

def catalogar(lista,ruedas=0):
  if(ruedas>0):
   listf =[ ]
   for i in lista:
     if(i.ruedas == ruedas):
       listf.append(i)
   print("Se han encontrado {} vehículos con {} ruedas:".format(len(listf),ruedas))
   for i in listf:
     print(type(i).__name__)
     print(i.ruedas) 
  else:
    for i in lista:
      print(type(i).__name__)
      print(i)


catalogar(Vehiculos)
print("----------------------------")
catalogar(Vehiculos,2)
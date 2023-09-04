a1 = input('Ingrese el nombre del arbitro a1: ')
a2 = input('Ingrese el nombre del arbitro a2: ')
a3 = input('Ingrese el nombre del arbitro a3: ')
a4 = input('Ingrese el nombre del arbitro a4: ')
cancha = input('Ingrese el nombre de la cancha: ')
dia = input('Ingrese el dia: ')

def imprimirArbitros(a1,a2,a3,a4):
 print("⚽⚽ARBITROS DESIGNADOS⚽⚽")
 print(a1)
 print(a2)
 print(a3)
 print(a4)
 print("⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽⚽")

def imprimirDatosCancha(cancha, dia):
  print("LUGAR")
  print(cancha)
  print("FECHA")
  print(dia)
def imprimircontactoliga():
  print("⚽⚽CONTACTO LIGA ⚽⚽")
  print("Tel. Liga: xxx-xxx-xxx 📞")
  print("Mail Liga: Liga@mail.com 📩")
imprimirArbitros(a1,a2,a3,a4)
imprimirDatosCancha(cancha,dia)
imprimircontactoliga()






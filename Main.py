
from eliminate import CircularLinkedList
respuesta=1
cl=CircularLinkedList()

while(respuesta==1):
    dat=int(input("Agregue el nodo "))
    cl.insert_at_beginning(dat)
    print("¿Desea agregar otro Nodo?")
    print("1. Sí        2.No")
    respuesta=int(input(""))
k=int(input("Ingrese el k "))
cl.elimin(k)
cl.display()
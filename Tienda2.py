
from typing import Dict, Any


class Product:
    und = {}

    def __init__(self, code, descripcion, precio):
        self.code = code
        self.descripcion = descripcion
        self.precio = precio



    def __str__(self):
        return "El codigo es  {} con la descripcion {} ".format(self.code, self.descripcion)

    def agregar_uni(self, code, descripcion, precio):
        self.und[code] = descripcion, precio



    def mostrar_todos(self):
        print("Las unidades  son: ")
        for i in self.und.keys():
            print("Code: " + str(i))
            print("Descripcion: " + str(self.und[i]))

    def __eq__(self, product):
        return self.code == product.code

    def __hash__(self):
        return hash(self._code)

class Catalogue(Product):
    def __init__(self,code, descripcion,precio):
        Product.__init__(self, code, descripcion, precio)


    def add_product(self, code, descripcion, precio):
        self.und[code] = descripcion, precio

    def remove_product(self, code):
            del self.und[code]
    def find_product(self, code):
        print("El Codigo es: "+code)

        if code in self.und.keys():
            print("El producto y su precio es: "+str(self.und[code]))

        else:
            print("El contacto no existe")


class Store(Catalogue):
    def __init__(self, code, descripcion, precio,cantidad):
        self.code = code
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad=0


    def añadir_tienda(self, code, descripcion, precio,cantidad+=1):

        self.und[code] = descripcion, precio,cantidad

    def remove_tienda(self, code):
        if cantidad > 0:
            del self.und[code]
        else:
            print("No se hay stoke")
    def find_prduct_store(self, code):
        print("El Codigo es: "+code)

        if code in self.und.keys():
            print("El producto y su precio es: "+str(self.und[code]))

        else:
            print("El contacto no existe")
    def mostrar_todos_tienda(self):
        print("Las unidades  son: ")
        for i in self.und.keys():
            print("Code: " + str(i))
            print("Descripcion: " + str(self.und[i]))
    def __str__(self):
        return "En la tienda hay {} unidades de {}, con un precio de {} ".format(self.cantidad, self.descripcion, self.precio)









    


t = Product(code="1", descripcion="Llaves Allen", precio="40€")
#print(t)
#print(t)
#t.agregar_uni("1", "LLave inglesa", "40€")

"""t.agregar_uni("2", "Llaves Allen", "40€")
t.agregar_uni("3", "destronillador", "20€")"""
#t.mostrar_todos()
"""cata= Catalogue(code="1", descripcion= "Llaves Allen", precio= "40€")
cata.add_product("4","tijeras", "20€")
cata.remove_product("4")
cata.mostrar_todos()
cata.find_product("3")"""
tienda = Store(code="4",descripcion="Tijeras", precio="20€",cantidad=0)

tienda.añadir_tienda("5","Martillo", "30€","3")
tienda.añadir_tienda("4","Martillo", "30€","5")

#print(tienda)
tienda.mostrar_todos_tienda()
#print("Tienda")




















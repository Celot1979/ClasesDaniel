
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
    """Lo que he realizado es una herencia de la clase padre. Aprovechando que existe un diccionario creado
    voy integrando los productos con los de la clase Product. Hasta la fecha que prové salían todos correctos."""
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
    """En está fase está lo más peliagudo, puesto que he de implemetar cantidad dentro del store para que se pueda
    is creando un stoke. En la comunidad que me recomiendan que lo añada directamente a la clase padre.... Se que cuando
    añado en el método (add_product_catalogue), y doy a mostrar, me salen todos los campos que quiero.. Lo que no sé
    como hacer es para sumar la cantidad..."""
    def __init__(self,code,descripcion,precio,cantidad=1):
        Catalogue.__init__(self,code,descripcion,precio)
        self.cantidad += 1
    def add_product_catalogue(self, code, descripcion, precio, cantidad):
        self.und[code] = descripcion,precio,cantidad
        self.cantidad += cantidad


    def remove_store(self, code, descripcion,):
        del self.und[code]

    def mostrar_todos_store(self):
        print("Las unidades  son: ")
        for i in self.und.keys():
            print("Code: " + str(i))
            for i in self.und.values():
                print("Descripcion: " + str(i[0]))
                print("Precio: " + str(i[1]))
                print("Cantidad: " + str(i[2]))





a = Product(code="1",descripcion="Llaves Allen",precio="12")
t = Catalogue(code="2", descripcion="Perchas",precio="12€")
s = Store(code="3",descripcion="clavos", precio="1€", cantidad=3)
s.add_product_catalogue(code="4",descripcion="Vaso", precio="5€",cantidad=2)
s.add_product_catalogue(code="5",descripcion="Copa", precio="3€",cantidad=5)
s.add_product_catalogue(code="6",descripcion="tenedor", precio="7€",cantidad=7)
s.mostrar_todos_store()

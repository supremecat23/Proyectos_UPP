
#1. Crear una clase usuarios
#2. Atributos: nombre, edad, CURP
#3. Validar que CURP sea de 18 caracteres exactamente
#4. definir un metodo que muestre los datos del usuario
#5. Definir un método que valide la edad que la edad del usuario sea mayot o igual a 18

class Usuario():
    def __init__(self, nombre, edad, curp):
        self.__nombre = nombre   #El doble guion hace privado al atributo
        if self.validar_edad(edad)== None:
         return "Necesitas ser mayor de edad"
        self.__edad = edad 
        if self.validar_curp(curp)== None:
         return "Curp Invalido"
        self.__curp = curp
        
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self,nombre):
        self.__nombre= nombre
        
    def get_edad(self):
        return self.__edad
        
    def set_edad(self, edad):
        if self.validar_edad(edad):
         self.__edad= edad
        else: 
         print("Invalida")
        

    def get_curp(self):
        return self.__curp
        
    def set_curp(self,curp):
        if self.validar_curp(curp):
         self.__curp= curp

    def validar_curp(self,curp):
        if len(curp)==18:
         return curp
    def mostrar_datos(self):
        return f"Nombre:{self.__nombre}\nEdad:{self.__edad}\nCurp:{self.__curp}"
    def validar_edad(self, edad):
        if edad >= 18:
         return edad

if __name__== "__main__":
    usuario_1 = Usuario("Ivan",30,"123456789012345678")
    # print(usuario_1.mostrar_datos())
    # usuario_1.set_edad(29)
    # print(usuario_1.mostrar_datos())
    print( usuario_1.get_curp)
    print(usuario_1.mostrar_datos())
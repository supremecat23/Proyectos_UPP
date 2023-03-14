#1.Crear clase cuenta
#2.Para poder crear una cuenta es necesario pasarle su respectivo usuario
#3.El depósito inicial de apertura es opcional
#4.Crear metodos de retiro y deposito de los atributos solo seran modificables atraves de los metodos
#5.Crear un metodo mostra_datos() que muestre los datos del usuario y balance total
from USUARIOS import Usuario
class Cuenta():
    def __init__(self,usuario:Usuario,balance=0):
     self.__usuario= usuario
     self.__balance= balance
     
    def retirar(self,retiro):
        if self.validar_retiro(retiro):
         self.__balance -= retiro
        else:
         print("No hay dinero suficiente")   
    
    def deposito():
        pass
    def validar_retiro(self, retiro):
        if retiro <= self.__balance:
         return True
    def mostrar_balance(self):
        return self.__balance
    
if __name__== "__main__":
     usuario_1=Usuario("Luis",20,"123456789012345678")
     cuenta_1= Cuenta(usuario_1, 1000)
     cuenta_1.retirar(1001)
     print(cuenta_1.mostrar_balance())
     
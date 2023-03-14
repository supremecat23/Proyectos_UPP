#Crear un método que le de bonificación al usuario
#Verificar que los usuarios sean menor de 25 años
# dEBEB MOSTRARSE la bonificación y que es una cuenta joven
from USUARIOS import Usuario
from Cuentas import Cuenta

class cuentas_joven(Cuenta):
    def __init__(self,usuario:Usuario,balance:Cuenta,bonificacion=0.12,edad=0):
        super().__init__(usuario,balance)
        self.__bonificacion = bonificacion
        self.__edad = edad
        
    def dar_bonificacion(self):
        self.__bonificacion *= super().mostrar_balance()
        print("¡Bonificación otorgada!")
        print(f"Tipo de cuenta: Cuenta joven\nBonificación: {self.__bonificacion}")
        print(f"Balance total: {self.mostrar_balance()}")
        
    def verificar_edad(self,edad):
        if edad <= 25:
            return edad

    def mostrar_balance(self):
        return f"{super().mostrar_balance()+self.__bonificacion}"

if __name__ == "__main__":
    usuario1 = Usuario("Juan", 25, "123456789012345678")
    cuenta_joven1 = cuentas_joven(usuario1, 1000)
    print(cuenta_joven1.mostrar_balance()) 
    
    cuenta_joven1.retirar(500)  
    print(cuenta_joven1.mostrar_balance())  
    
    cuenta_joven1.dar_bonificacion()  
    print(cuenta_joven1.mostrar_balance())  
    
    #usuario2 = Usuario("María", 26, "123456789012345679")
    #cuenta_joven2 = CuentaJoven(usuario2, 2000)  # Error, el titular es mayor de 25 años
    #cuenta_joven2.retirar(500)  # Retira 500 pesos
    #print(cuenta_joven2.mostrar_balance())
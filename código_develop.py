from abc import ABC, abstractmethod

# Definir la interfaz (Clase Base Abstracta)
class NotificadorInterface(ABC):
    
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        """Método abstracto que obliga su implementación"""
        pass

# Implementar la interfaz en una clase concreta
class CorreoNotificador(NotificadorInterface):
    
    def enviar(self, mensaje: str) -> None:
        print(f"Enviando correo electrónico: {mensaje}")

# Uso
notificador = CorreoNotificador()
notificador.enviar("¡Hola, esto es una prueba!")
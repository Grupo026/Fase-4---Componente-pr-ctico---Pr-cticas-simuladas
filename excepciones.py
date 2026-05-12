# Excepciones personalizadas del sistema


class ClienteInvalidoError(Exception):
    def __init__(self, mensaje="El cliente es inválido"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ServicioNoDisponibleError(Exception):
    def __init__(self, mensaje="El servicio no está disponible"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ReservaInvalidaError(Exception):
    def __init__(self, mensaje="La reserva es inválida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class DuracionInvalidaError(Exception):
    def __init__(self, mensaje="La duración ingresada no es válida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje) 
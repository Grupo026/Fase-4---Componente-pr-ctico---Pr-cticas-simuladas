class Reserva:

    def __init__(self,
                 cliente,
                 servicio,
                 duracion):

        if cliente is None:
            raise ValueError("Cliente inválido")

        if servicio is None:
            raise ValueError("Servicio inválido")

        if duracion <= 0:
            raise ValueError(
                "Duración debe ser mayor a 0"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def confirmar(self):

        if self.estado != "pendiente":
            raise Exception(
                "La reserva no se puede confirmar"
            )

        self.estado = "confirmada"

        print("Reserva confirmada")

    def cancelar(self):

        if self.estado == "cancelada":
            raise Exception(
                "La reserva ya está cancelada"
            )

        self.estado = "cancelada"

        print("Reserva cancelada")

    def procesar(self):

        if self.estado != "confirmada":
            raise Exception(
                "Debe confirmar la reserva"
            )

        costo = self.servicio.calcular_costo(
            self.duracion
        )

        print(f"Costo total: {costo}")
                
from abc import ABC, abstractmethod
from clientes import EntidadSistema

class ServicioNoDisponible(Exception):
    pass

class Servicio(EntidadSistema):
    def __init__(self, id_servicio: int, nombre: str, precio_base: float):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.precio_base
        self.validar()

    @abstractmethod
    def calcular_costo(self, duracion: int, descuento: float = 0, iva: bool = True) -> float:
        pass

    @abstractmethod
    def describir(self) -> str:
        pass

    def validar(self):
        if self.precio_base <= 0:
            raise ServicioNoDisponible("El precio base debe ser mayor a 0")
        if not self.nombre:
            raise ServicioNoDisponible("El servicio debe tener nombre")

class ReservaSala(Servicio):
    def __init__(self, id_servicio, nombre, precio_hora, capacidad, tiene_proyector):
        super().__init__(id_servicio, nombre, precio_hora)
        self.capacidad = capacidad
        self.tiene_proyector = tiene_proyector

    def calcular_costo(self, horas: int, descuento: float = 0, iva: bool = True) -> float:
        if horas <= 0: 
            raise ValueError("Las horas deben ser > 0")
        costo = self.precio_base * horas
        if self.tiene_proyector: 
            costo += 20000 * horas
        costo_descuento = costo * (1 - descuento)
        return costo_descuento * 1.19 if iva else costo_descuento

    def describir(self) -> str:
        proyector = "con proyector" if self.tiene_proyector else "sin proyector"
        return f"ReservaSala: '{self.nombre}' - Cap: {self.capacidad} - {proyector}"

class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, precio_dia, marca, stock):
        super().__init__(id_servicio, nombre, precio_dia)
        self.marca = marca
        self.stock = stock

    def calcular_costo(self, dias: int, descuento: float = 0, iva: bool = True) -> float:
        if dias <= 0: 
            raise ValueError("Los días deben ser > 0")
        if self.stock <= 0:
            raise ServicioNoDisponible("No hay stock disponible")
        costo = self.precio_base * dias
        costo_descuento = costo * (1 - descuento)
        return costo_descuento * 1.19 if iva else costo_descuento

    def describir(self) -> str:
        return f"AlquilerEquipo: '{self.nombre}' - Marca: {self.marca} - Stock: {self.stock}"

class Asesoria(Servicio):
    def __init__(self, id_servicio, nombre, precio_hora, especialista, area):
        super().__init__(id_servicio, nombre, precio_hora)
        self.especialista = especialista
        self.area = area

    def calcular_costo(self, horas: int, descuento: float = 0, iva: bool = True) -> float:
        if horas <= 0: 
            raise ValueError("Las horas deben ser > 0")
        costo = (self.precio_base * horas) + 50000
        costo_descuento = costo * (1 - descuento)
        return costo_descuento * 1.19 if iva else costo_descuento

    def describir(self) -> str:
        return f"Asesoria: '{self.nombre}' - Área: {self.area} - Esp: {self.especialista}"
    
    
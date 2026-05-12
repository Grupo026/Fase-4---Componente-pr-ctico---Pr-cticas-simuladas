from abc import ABC, abstractmethod


# Clase abstracta base del sistema
class Entidad(ABC):

    def __init__(self, id_entidad, nombre):
        self._id_entidad = id_entidad
        self._nombre = nombre

    # Método abstracto
    @abstractmethod
    def mostrar_informacion(self):
        pass

    # Getter para ID
    def get_id(self):
        return self._id_entidad

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

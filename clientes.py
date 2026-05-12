from abc import ABC
import re

class ClienteInvalido(Exception):
    pass

class EntidadSistema(ABC):
    def __init__(self, id_entidad: int):
        self._id = id_entidad
    
    def get_id(self) -> int:
        return self._id

class Cliente(EntidadSistema):
    def __init__(self, id_cliente: int, nombre: str, email: str, telefono: str):
        super()._init_(id_cliente)
        self.__nombre = ""
        self.__email = ""
        self.__telefono = ""
        self.set_nombre(nombre)
        self.set_email(email)
        self.set_telefono(telefono)

    def get_nombre(self) -> str: 
        return self.__nombre
    
    def get_email(self) -> str: 
        return self.__email
    
    def get_telefono(self) -> str: 
        return self.__telefono

    def set_nombre(self, nombre: str):
        if not nombre or len(nombre.strip()) < 3:
            raise ClienteInvalido("El nombre debe tener al menos 3 caracteres")
        self.__nombre = nombre.strip().title()

    def set_email(self, email: str):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, email):
            raise ClienteInvalido(f"Formato de email inválido: {email}")
        self.__email = email.lower()
    
    def set_telefono(self, telefono: str):
        if not telefono.isdigit() or len(telefono) != 10:
            raise ClienteInvalido("Teléfono debe tener exactamente 10 dígitos")
        self.__telefono = telefono

    def validar(self):
        if not all([self.__nombre, self.__email, self.__telefono]):
            raise ClienteInvalido("Cliente con datos incompletos")
        return True
    
    def _str_(self):
        return f"Cliente[{self.get_id()}]: {self.__nombre} - {self.__email}"
    
    
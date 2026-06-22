class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        return f"Cliente: {self.nombre} - Teléfono: {self.telefono}"

    def __str__(self):
        return self.mostrar_info()
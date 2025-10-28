class Veicolo:
    def __init__(self, marca, modello, carburante):
        self.marca = marca
        self.modello = modello
        self.carburante = carburante

    def descrizione(self):
        return f"{self.marca} {self.modello} - Carburante: {self.carburante}"

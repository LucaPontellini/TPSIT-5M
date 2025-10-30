class Veicolo:
    def __init__(self, marca: str, modello: str, carburante: str) -> None:
        self.marca = marca
        self.modello = modello
        self.carburante = carburante

    def descrizione(self) -> str:
        return f"Marca: {self.marca}\nModello: {self.modello}\nCarburante: {self.carburante}"
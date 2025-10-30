from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, marca, modello, carburante, porte):
        super().__init__(marca, modello, carburante)
        self.porte = porte

    def descrizione(self):
        return f"Auto: {super().descrizione()}, {self.porte} porte"
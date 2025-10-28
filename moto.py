from veicolo import Veicolo

class Moto(Veicolo):
    def __init__(self, marca, modello, carburante, cilindrata):
        super().__init__(marca, modello, carburante)
        self.cilindrata = cilindrata

    def descrizione(self):
        return f"Moto: {super().descrizione()}, {self.cilindrata}cc"
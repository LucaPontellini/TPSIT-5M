from veicolo import Veicolo

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, carburante: str, cilindrata: int) -> None:
        super().__init__(marca, modello, carburante)
        self.cilindrata = cilindrata

    def descrizione(self) -> str:
        return f"Moto:\n{super().descrizione()}\nCilindrata: {self.cilindrata}cc"
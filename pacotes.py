# Orientação a Objetos: Paradigma de Programação
# Classes e Objetos


class Veiculos:

    # Metodo init > Parametros necessarios para inicializar o objeto.
    def __init__(self, fabricante, modelo):
        # Para criar um atributo privado, digite dois __ (underscore) antes do parametro;
        # Encapsulamento
        self.__fabricante = fabricante
        # Atributo sem encapsulamento
        self.modelo = modelo
        # Podemos criar um atributo sem a necessidade de inicializar-lo.
        self.__placa_veiculo = None

    # Metodo especial para acessar atribulos privados (Encapsulados)
    # Getter

    def get_fabricante(self):
        print(f"Fabricante: {self.__fabricante}")

    # Metodo especial para gravar em atributos privados
    # Setter

    def set_placa(self, placa):
        self.__placa_veiculo = placa

    def get_placa(self):
        return self.__placa_veiculo

    def movimentar(self):
        print(f"Sou um veiculo em movimento...")


# Herança
class Carro(Veiculos):
    # Metodo __init__ será herdado
    def movimentar(self):
        print(f"Sou um CARRO em movimento...")


class Motocicleta(Veiculos):
    def movimentar(self):
        print("Sou uma MOTOCICLETA em movimento...")


class Aviao(Veiculos):
    # Foi acrescentado mais um parametro no __init__
    def __init__(self, fabricante, modelo, categoria):
        self.__categoria = categoria
        # Super é usado para referenciar a classe herdada, no caso a classe Veiculo;
        super().__init__(fabricante, modelo)

    def get_cat(self):
        print(f"Categoria: {self.__categoria}")

    def movimentar(self):
        print(f"Sou uma AERONAVE voando...")

# Orientação a Objetos: Paradigma de Programação
# Classes e Objetos


class Veiculos:

    # Metodo init > Parametros necessarios para inicializar o objeto.
    def __init__(self, fabricante, modelo):
        # Para criar um atributo privado, digite dois __ (underscore) antes do parametro;
        # Encapsulamento
        self.__fabricante = fabricante
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

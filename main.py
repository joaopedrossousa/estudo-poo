from pacotes import Veiculos, Carro, Motocicleta, Aviao

# Criação do Objeto
meu_veiculo = Veiculos("Chevrolet", "Astra")

# Apos criar o objeto, podemos invocar os seus metodos.
meu_veiculo.movimentar()

# Como acessar atributos contidos na classe (Não ideal)
print(meu_veiculo.modelo)

# Atributo acessado via Getter (Ideal)
meu_veiculo.get_fabricante()

# Objeto > Metodo > Parametro
# meu_veiculo.set_placa((input("Informe a placa do Veiculo: ")))
print(f"Placa do Veiculo: {meu_veiculo.get_placa()}")

# Ou
meu_veiculo.set_placa("MXD-876")
print(f"Placa Veiculo {meu_veiculo.get_placa()}")

print()
print("-" * 40)
print()

# Utilização de uma classe que possui heranças
meu_carro = Carro("Volkswagen", "Polo")
meu_carro.movimentar()
meu_carro.get_fabricante()
print(meu_carro.modelo)

print()

# Criando outro objeto com a mesma classe
seu_carro = Carro("Audi", "A5 Sportback")
seu_carro.movimentar()
seu_carro.get_fabricante()
print(seu_carro.modelo)

print()

motocicleta = Motocicleta("BMW", "GS-700")
motocicleta.movimentar()
motocicleta.get_fabricante()

print()
print("-" * 40)

aviao = Aviao("Boeing", "747", "Aeronave Civil")
aviao.get_cat()
aviao.movimentar()

print()
print("-" * 40)

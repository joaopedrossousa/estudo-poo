from pacotes import Veiculos

# Criação do Objeto
meu_veiculo = Veiculos("Chevrolet", "Astra")

# Apos criar o objeto, podemos invocar os seus metodos.
meu_veiculo.movimentar()

# Como acessar atributos contidos na classe (Não ideal)
print(meu_veiculo.modelo)

# Atributo acessado via Getter (Ideal)
meu_veiculo.get_fabricante()

# Objeto > Metodo > Parametro
meu_veiculo.set_placa((input("Informe a placa do Veiculo: ")))
print(f"Placa do Veiculo: {meu_veiculo.get_placa()}")

# Ou
meu_veiculo.set_placa("MXD-876")
print(f"Placa Veiculo {meu_veiculo.get_placa()}")

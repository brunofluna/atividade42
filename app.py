from modulo import *

if __name__ == "__main__":
    
    cliente1 = Cliente('','','','')

    cliente1.nome = input('Informe o nome do cliente: ')
    cliente1.cpf = input('Informe o CPF do cliente: ')
    cliente1.idade = input('Informe a idade do cliente: ')
    cliente1.telefone = input('Informe o telefone do cliente: ')

    cliente2 = Cliente('','','','')

    cliente2.nome = input('Informe o nome do cliente: ')
    cliente2.cpf = input('Informe o CPF do cliente: ')
    cliente2.idade = input('Informe a idade do cliente: ')
    cliente2.telefone = input('Informe o telefone do cliente: ')

    carro1 = Carro('Gol', 'Preto', '2011', 200.00)
    carro2 = Carro('Fusca', 'Vermelho', '1960', 550.00)

    cliente2.aluga_carro(carro2)
    cliente1.aluga_carro(carro1)

    print(f'\nCliente {cliente1.nome}, de idade {cliente1.idade} alugou os seguintes carros {cliente1.listar_carros()}.')
    print(f'\nCliente {cliente2.nome}, de idade {cliente2.idade} alugou os seguintes carros {cliente2.listar_carros()}.')
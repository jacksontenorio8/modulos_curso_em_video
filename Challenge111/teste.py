from utilidadesCev  import moeda
#from moeda import aumentar, diminuir

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10% teremos {moeda.aumentar(p, 10, True)}')
print(f'Diminuir em 13% teremos {moeda.diminuir(p, 13, True)}')  
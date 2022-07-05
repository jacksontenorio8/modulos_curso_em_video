import moeda
#from moeda import aumentar, diminuir

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando em 10% teremos {moeda.aumentar(p, 10)}')
print(f'Diminuir em 20% teremos {moeda.diminuir(p, 20)}')
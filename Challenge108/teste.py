import moeda
#from moeda import aumentar, diminuir

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando em 10% teremos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuir em 20% teremos {moeda.moeda(moeda.diminuir(p, 20))}')
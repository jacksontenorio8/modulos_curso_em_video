"""
Create a package called utilitiesCev that has two modules called moeda and dados. Transfer all the functions used in challenges 107, 108 and 109 to the first package and keep everything running.
"""

def aumentar(preco = 0, taxa = 0, formato=False):
    res= preco + (preco * taxa/100)
    return res if formato is False else moeda(preco)
    
def diminuir(preco = 0, taxa = 0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(preco)


def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(preco)

    
def metade(preco = 0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(preco)


def moeda(preco = 0, moeda = 'R$', formato=False):
    return f'{moeda}{preco:>.2f}'.replace('.',',')
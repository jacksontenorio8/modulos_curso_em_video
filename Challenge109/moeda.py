"""
Modify the functions that were created in challenge 107 so that they accept one more parameter, informing whether or not the value returned by them will be formatted by the moeda() function, developed in challenge 108.
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
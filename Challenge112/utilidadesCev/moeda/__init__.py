"""
Inside the utilidadesCeV package that we created in challenge 111, we have a module called data. Create a function called leiaDinheira() that is capable of working with the input() function, but with data validation to only accept monetary values.
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
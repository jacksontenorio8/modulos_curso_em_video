"""
Create a module called moeda.py that has built-in functions aumentar(), diminuir(), dobro() and metade(). Also make a program to import these modules and use some functions.
"""

def aumentar(preco, taxa):
    res= preco + (preco * taxa/100)
    return res
    
def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco):
    res = preco * 2
    return res

    
def metade(preco):
    res = preco / 2
    return res  
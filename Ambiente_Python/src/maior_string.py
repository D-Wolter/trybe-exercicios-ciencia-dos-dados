lista = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def count_str(lista_strings):
    maior_nome = ""
    for nome in lista_strings:
        if len(nome) > len(maior_nome):
            maior_nome = nome
    return print(maior_nome)


count_str(lista)
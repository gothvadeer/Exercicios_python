#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

def n(*notas, sit=False):
    """
    Leitor de notas
    :param notas: ler as notas informadas
    :param sit: Se True mostra situação do aluno, se False, é ignorado.
    :return: retorna um dicionário com a maior nota, a menor nota, a média e a situação (ou não)
    """
    media = (sum(notas)) / len(notas)
    notas_dict = {"Total": len(notas), "Maior": max(notas), "Menor": min(notas), "Média": media}
    resp = ' '
    if sit:
        if 6 <= media < 7:
            resp = 'Razoável'
        elif media >= 7:
            resp = 'Boa'
        else:
            resp = 'Ruim'
    if sit:
        notas_dict["Situação"] = resp
    return notas_dict


print(n(4.4, 3, 1, 10, sit=True))
help(n)
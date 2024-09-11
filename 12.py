# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.
nota = int(input("nota do aluno"))
if nota >= 7:
    print("aprovado")
if nota <= 6:
    print("reprovado")
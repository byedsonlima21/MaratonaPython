notas = []
alunos = []
turma = []

while True:
    alunos.append(input("Nome do aluno: ").strip().title())
    for i in range(2):
        notas.append(float(input(f'Qual a {i+1}ª nota do aluno? ')))

    alunos.append(notas[:])
    turma.append(alunos[:])
    alunos.clear()
    notas.clear()

    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('=' * 40)
print(f"{'N°':<10}{'Aluno':<20}{'Média':>10}")
print('=' * 40)

for num, aluno in enumerate(turma):
    media = sum(aluno[1]) / 2
    print(f"{num+1:<10}{aluno[0]:<20}{media:>10.2f}")
print('=' * 40)

while True:
    mostrar = int(input("Mostar nota de qual aluno? [digite 999 para parar] "))
    if mostrar in range(0, len(turma)):
        print("=" * 40)
        print(f"As notas do/da {turma[mostrar-1][0]} são {turma[mostrar-1][1]}.")
    elif mostrar == 999:
        break
    elif mostrar not in range(0, len(turma)):
        print("Aluno não encontrado tente novamente\n")
print("FINALIZANDO...")
print("<<<< VOLTE SEMPRE >>>>")
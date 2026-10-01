aluno = dict()

aluno['nome'] = str(input('Nome: ')).title()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

print(f'O aluno em análise é o {aluno["nome"]}.')
print(f'O {aluno["nome"]} tem {aluno["media"]} na média.')
if aluno['media'] >= 7:
    print(f'{aluno['nome']} está aprovado!')
elif 5 <= aluno['media'] < 7:
    print(f'{aluno["nome"]} está de recuperação.')
else:
    print(f'Infelizmente {aluno['nome']} não foi aprovado')
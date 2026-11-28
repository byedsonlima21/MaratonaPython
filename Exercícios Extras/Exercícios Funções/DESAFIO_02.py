"""Desafio 2 – Gerador de Logs:
Crie uma fábrica de mensagens que receba o nível
do alerta (ex: "ERRO", "AVISO") e retorne uma função
que receba o texto, devolvendo a frase formatada
(ex: [ERRO] Falha no sistema). Teste criando duas
funções para níveis diferentes e exibindo mensagens com elas."""

def nivel_alerta(nivel):
    def mensagem(msg):
        return f'[{nivel}]: {msg}'
    return mensagem

aviso1 = nivel_alerta("Aviso")
print(aviso1("Erro de login"))

#TESTE 2

aviso2 = nivel_alerta("Critico")
ba = aviso2("Senhas Vazadas")
print(ba)
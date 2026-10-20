from urllib import request, error

# Verificar se um site está acessível

# Site pudim não deu certo, mas do Whatsapp sim
try:
    site = request.urlopen("https://web.whatsapp.com/")
except error.URLError:
    print("\033[0:31mO site não está acessível nesse momento...\033[m")
else:
    print("\033[0:32mO site com acesso...!\033[m")
# Importa uma bibliorteca para colorir o texto no terminal 
from colorama import Fore, Style, init

# Inicializa o colorama e reserta as cores após cada impressão
init(autoreset=True)

# Lista os níveis do reservatório de água
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Define a cor com base no nível em status diferentes
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação dos níveis do reservatório "i" serve para contar do 1 ao inves do 0
for i in range(len(niveis)):
    nivel_atual = i + 1
    mensagem = niveis[i]
    
    cor = definir_cor(nivel_atual)
    
    print(cor + f"Nível {nivel_atual}: {mensagem}" + Style.RESET_ALL)
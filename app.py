from colorama import Fore, Style, init


niveis = [(1, "Muito baixo"), (2, "Baixo"), (3, "Médio"), (4, "Alto"), (5, "Muito alto")]


#Função
def definir_cor(nivel):
 if nivel == 1 :
  return Fore.RED
 if nivel == "Baixo":
  return Fore.YELLOW
 if nivel == "Médio":
  return Fore.GREEN
 if nivel == "Alto":
  return Fore.CYAN
 if nivel == "Muito alto":
  return Fore.BLUE
 else:
  return Fore.WHITE


print ("CONTROLE DE NÍVEIS DA ÁGUA")

nivel = input("Digite o nível da água:")
cor = definir_cor(nivel)

print("Nível informado:", nivel)

if nivel in niveis:
 print( cor + "Alerta: nível de água " + nivel + Style.RESET_ALL)
else:
 print(Fore.WHITE + "Nível inválido!" + Style.RESET_ALL)
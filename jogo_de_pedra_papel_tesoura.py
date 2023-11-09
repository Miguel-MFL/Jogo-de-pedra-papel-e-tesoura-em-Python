# Importar a biblioteca random para gerar números aleatórios
import random

# Definir as opções possíveis do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Definir uma função para verificar o resultado do jogo
def verificar_resultado(jogador, computador):
  # Se o jogador e o computador escolherem a mesma opção, é um empate
  if jogador == computador:
    return "Empate"
  # Se o jogador escolher pedra e o computador escolher tesoura, o jogador ganha
  elif jogador == "pedra" and computador == "tesoura":
    return "Você ganhou"
  # Se o jogador escolher papel e o computador escolher pedra, o jogador ganha
  elif jogador == "papel" and computador == "pedra":
    return "Você ganhou"
  # Se o jogador escolher tesoura e o computador escolher papel, o jogador ganha
  elif jogador == "tesoura" and computador == "papel":
    return "Você ganhou"
  # Em qualquer outro caso, o computador ganha
  else:
    return "Você perdeu"

# Iniciar um laço para repetir o jogo até que o usuário queira sair
while True:
  # Pedir ao usuário para escolher uma opção ou digitar sair para terminar o jogo
  jogador = input("Escolha uma opção (pedra, papel ou tesoura) ou digite sair para terminar: ")
  # Se o usuário digitar sair, encerrar o laço e o jogo
  if jogador == "sair":
    break
  # Se o usuário escolher uma opção válida, continuar o jogo
  elif jogador in opcoes:
    # Gerar uma opção aleatória para o computador
    computador = random.choice(opcoes)
    # Mostrar as escolhas do jogador e do computador
    print(f"Você escolheu {jogador} e o computador escolheu {computador}.")
    # Chamar a função para verificar o resultado do jogo e mostrar na tela
    resultado = verificar_resultado(jogador, computador)
    print(resultado)
  # Se o usuário digitar algo inválido, mostrar uma mensagem de erro e pedir novamente
  else:
    print("Opção inválida. Por favor, tente novamente.")

# Agradecer ao usuário por jogar e encerrar o programa
print("Obrigado por jogar. Até a próxima!")
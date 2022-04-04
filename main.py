import random
import time

def play():
  opcao = ['pedra', 'papel', 'tesoura']
  
  player = int(input("[0] pedra, [1] papel, [2] tesoura: "))
  machine = random.choice([0, 1, 2])

  print(f"Você escolheu {opcao[player]}...")
  time.sleep(1.5)
  print(f"A máquina escolheu {opcao[machine]}...")
  time.sleep(1.5)
  if player == machine:
    print("Empate!")
  elif is_win(player, machine):
    print("Parabéns, você venceu!")
  else:
    print("Uh oh, você perdeu!")

def is_win(player, machine):
  if (player == 0 and machine == 2) or (player == 1 and machine == 0) or (player == 2 and machine == 1):
    return True

play()
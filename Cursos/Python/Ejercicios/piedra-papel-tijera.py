#Juego de piedra, papel o tijera
import random

options = ("piedra", "papel", "tijera")
computer_wins = 0
user_wins = 0
rounds = 1

while True:

  print("*" * 3 + " Bienvenido al juego Piedra, Papel o Tijera🪨 📄✂️ " + "*" * 3)
  print("ROUND", rounds)
  print("*" * 10)

  print("Computer wins =>", computer_wins)
  print("User wins =>", user_wins)

  user_option = input('Elige entre piedra, papel o tijera => ')
  user_option = user_option.lower()

  rounds += 1
  
  if not user_option in options:
    print("Esa opción no es válida.")
    continue
  
  computer_option = random.choice(options)
  
  print("User option =>", user_option )
  print("Computer option =>", computer_option)
  
  if user_option == computer_option: #Se evalúa el empate
    print("Empate!")
  
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Ganaste. Piedra le gana a tijera.")
      user_wins += 1
    else:
      print("Perdiste. Papel le gana a piedra.")
      computer_wins += 1
  
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Ganaste. Papel le gana a piedra.")
      user_wins += 1
    else:
      print("Perdiste. La tijera le gana al papel.")
      computer_wins += 1
  
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Ganaste. La tijera le gana al papel.")
      user_wins += 1
    else:
      print("Perdiste. La piedra le gana a la tijera.")
      computer_wins += 1

  if computer_wins == 2:
    print("🎖️ El ganador es la computadora.🎖️")
    break

  if user_wins == 2:
    print("🎖️ El ganador es el usuario.🎖️")
    break
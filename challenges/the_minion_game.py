def menu():
      print("Bem vindo ao Minion Game!!")
      print("Selecione qual modo você gostaria de jogar")
      print("1- 1 v 1")
      print("2- 1 V BOT")
      op = int(eval(input()))
      print(op)

op=0
menu()
while(op<2 and op>0):
      if(op==1):
            word = str(eval(input("selecione uma palavra")))

      elif(op==2):
            print("jogo Contra bot")
      else:
            print("Opção invalida")

      break

import random

cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
cards = cards*4
dealerValue = 0
yourValue = 0

#to pick a card
def pickCard():
  value = 0
  card = random.choice(cards)
  cards.remove(card)
  if card == "king":
    value = 10
  elif card == "queen":
    value = 10
  elif card == "jack":
    value = 10
  elif card == "10":
    value = 10
  elif card == "9":
    value = 9
  elif card == "8":
    value = 8
  elif card == "7":
    value = 7
  elif card == "6":
    value = 6
  elif card == "5":
    value = 5
  elif card == "4":
    value = 4
  elif card == "3":
    value = 3
  elif card == "2":
    value = 2
  else:
    value = 1
  return card, value


#start
cardNow = pickCard()
cardNow2 = pickCard()
dealerValue = cardNow[1] + cardNow2[1]
hiddenCard = cardNow2
print("The dealer has a " + cardNow[0] + " showing.")
cardNow = pickCard()
cardNow2 = pickCard()
yourValue = cardNow[1] + cardNow2[1]
print("You have a "  + cardNow[0] + " and a " + cardNow2[0] + ". You have a total of " + str(yourValue) + ".")


finish = True
playing = True
dealerGo = True
while playing:
  print("")
  choice = str(input("Do you want to hit or stay? (h/s) "))
  if choice == "h":
    cardNow = pickCard()
    yourValue = yourValue + cardNow[1]
    print("The card is " + cardNow[0] + ". You have a total of " + str(yourValue) + ".")
    if yourValue > 21:
      print("You busted!")
      print("The dealer wins!")
      dealerGo = False
      playing = False
      finish = False
  else:
    print("You choose to stay with " + str(yourValue)+ ".")
    playing = False

print("")

if dealerGo:
  print("The dealer reveals his hidden card. It is a " + hiddenCard[0] + ".")
while dealerGo:
  print("")
  print("Dealer has a total of " + str(dealerValue) + ".")
  if dealerValue > 21:
    print("The dealer busted!")
    print("You win!")
    dealerGo = False
    finish = False
  elif dealerValue > 16:
    dealerGo = False
    print("Dealer has passed 16 and stopped.")
  else:
    cardNow = pickCard()
    print("The dealer hit and got " + cardNow[0]+ ".")
    dealerValue = dealerValue + cardNow[1]

#FINISH
if finish:
  if yourValue > dealerValue:
    print("")
    print("You win!!")
  elif dealerValue > yourValue:
    print("")
    print("You lose!")
  else:
    print("")
    print("You tied in score, so the dealer wins (You Lose!)")

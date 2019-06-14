import random, string

money = 100

#Write your game of chance functions here
def cointoss(choice, bet):
  coin = random.randint(0, 1)
  choice = ''.join(choice.split()).lower()
  if bet <= 0:
  	print("Bet must be more than zero")
  if coin == 0:
    coin = "heads"
  else:
    coin = "tails"
  print("The coin landed " + coin)
  if choice == coin:
    print("You won $" + str(bet) + "!")
    return bet
  else:
    print("You lost $" + str(bet) + "!")
    return -bet

def cho_han(choice, bet):
  summ = random.randint(1, 6) + random.randint(1, 6)
  if summ%2 == 0:
    summ = "even"
  else:
    summ = "odd"
  print("The sum is " + summ)
  if choice == summ:
    print("You won $" + str(bet) + "!")
    return bet
  else:
    print("You lost $" + str(bet) + "!")
    return -bet

def card_hipick_v2(bet):
  list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  cards = random.sample(list0, 2)
  if cards[0] > cards[1]:
    print("Your card is " + card_mod(0) + random.choice(card))
    print("Player 2s card is " + card_mod(1) + random.choice(card))
    print("You win $" + str(bet) + "!")
    return bet
  else:
    print("Your card is " + card_mod(0) + random.choice(card))
    print("Player 2s card is " + card_mod(1) + random.choice(card))
    print("You lose $" + str(bet) + "!")
    return -bet

  def card_mod(i):
    card = [" of Diamonds", " of Spades", "of Hearts", "of Clubs"]
    if cards[i] == 1:
      cards[i] = "Ace"
    elif cards[i] == 11:
      cards[i] = "Jack"
    elif cards[i] == 12:
      cards[i] = "Queen"
    elif cards[i] == 13:
      cards[i] == "King"
    return (str(cards[i]) + random.choice(card))


def euro_roulette(bet, choice):
  # For Roulette number
  num = random.randint(0, 36)
  red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
  
  # For color
  for n in red:
    if n == num:
      setcolor = "red "
      break
    else:
      setcolor = "black "
      break
  if num == 0:
  	setcolor = ""
  print("The number is " + setcolor + str(num))
  if str(choice).isalpha():
    choice = ''.join(choice.split()).lower()
    bet*=2
    # For color betting
    if choice == "red" or choice == "black":
      if setcolor == choice:
        print("You win $" + str(bet) + "!")
        return bet
      else:
        print("You lose $" + str(bet) + "!")
        return -bet

    # For Even, Odd betting
    else:
      if num == 0:
        print("You lose $" + str(bet) + "!")
        return -bet
      elif num%2 == 0:
        if choice == "even":
          print("You win $" + str(bet) + "!")
          return bet
        else:
          print("You lose $" + str(bet) + "!")
          return -bet
      else:
        if choice == "odd":
          print("You win $" + str(bet) + "!")
          return bet
        else:
       	  print("You lose $" + str(bet) + "!")
          return -bet

      
  # For single number betting
  else:
    bet*=35
    if choice == num:
      print("You win $" + str(bet) + "!")
      return bet
    else:
      print("You lose $" + str(bet) + "!")
      return -bet

#Remove/Add comment as per requirement
#money += cointoss("Heads",60)
#money += cho_han("Even", 60)
#money += card_hipick_v2(60)
#money += euro_roulette(20,"Even")
#money += euro_roulette(20,5)

if money >= 0:
  print("You are left with: $" + str(money))
else:
  money = -money
  print("You are in a debt of: $" + str(money))




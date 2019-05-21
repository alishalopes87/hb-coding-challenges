import random 

suits = ["Hearts","Spades","Clubs","Diamonds"]
values = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]

class Card(object):

	def __init__(self,value,suit):
		self.value = value
		self.suit = suit



class Deck(object):

	def _init__(self,cards=None):
		self.cards = []

	def build(self,card):
		self.cards.append(card)

	def shuffle(self):
		i = len(self.cards)
		while i > 1:
			i = i -1
			j = random.randrange(i)
			items[j], items[i] = items[i], items[j]

deck = Deck()

for suit in suits:
	for value in values:
		temp_card = Card(value,suit)
		deck.build(temp_card)

print(deck)
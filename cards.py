from random import choice
"""
class Cards:
	def __init__(self,deck=[],hand=[]):
		self.deck = deck
		self.hand = hand
		

	def create_deck(self):
		suits = "SHCD"
		cards = list(range(2,15))
		for i in suits:
			for s in cards:
				self.deck.append([s,i])

	def shuffle(self):
		self.create_deck()
		shuffled_deck = []
		temp_deck = self.deck
		for i in range(len(self.deck)):
			card = choice(temp_deck)
			shuffled_deck.append(card)
			temp_deck.remove(card)
		return shuffled_deck

	def add_card(self,cards_added=1):
		for i in range(cards_added):
			if len(self.deck) < 0:
				self.deck = self.shuffle()
			self.hand.append(self.deck[0])
			self.deck.remove(self.deck[0])
		return self.hand
"""
class Card:
	def __init__(self,value=0,suit="",face=""):
		self.value = value
		self.suit = suit
		self.face = face
		self.make_face()

	def make_face(self):
		if self.value == 1: self.face = "A"
		elif self.value == 11: self.face = "J"
		elif self.value == 12: self.face = "Q"
		elif self.value == 13: self.face = "K"

class Deck:
	def __init__(self,cards=[],no_cards=13,suits="SCHD"):
		self.cards = cards
		for i in suits:
			for s in range(1,no_cards+1):
				self.cards.append(Card(s,i))
		self.shuffle()

	def shuffle(self):
		shuffled_deck = []
		for i in range(len(self.cards)):
			card = choice(self.cards)
			shuffled_deck.append(card)
			self.cards.remove(card)
		self.cards = shuffled_deck
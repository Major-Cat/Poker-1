from random import choice
class Cards:
	def __init__(self,deck=[],hand=[]):
		self.deck = deck
		self.hand = hand
	

	def create_deck(self):
		suits = "SHCD"
		cards = list(range(1,11)) + ["J","Q","K"]
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
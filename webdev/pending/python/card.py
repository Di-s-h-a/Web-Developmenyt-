# Pythonic card desk __getitem__ and __len__
import collections
card = collections.namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [card(rank,suit) for suit in self.suits 
                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
beer_card = card('7','diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
# print(choice(deck))
from random import choice
print(choice(deck))           
print(choice(deck))           
print(choice(deck))           
print(choice(deck))           

for card in reversed(deck):
    print(card)
for card in deck:
    print(card)

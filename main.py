import random

class Player:
    hand_list = []
    tomb_list = []
    
    def __init__(self, name):
        self.name = name
        
    def drawCard(self, newCard):
        self.hand_list.append(newCard)
        
    def winCard(self, winCard):
        self.tomb_list.append(winCard)
        
class Card:
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number
        
    def showMe(self):
        return (self.symbol, self.number)
    
class SpecialCard:
    symbol = 'special'
    
    def __init__(self, number):
        self.number = number
        
    def showMe(self):
        return (self.symbol, self.number)
        
class Deck:
    def __init__(self, total_list):
        self.deck_list = total_list
        
    def showTotalCardLen(self):
        return len(self.deck_list)
    
    def showAllCard(self):
        for i in self.deck_list:
            print(i.showMe())
            
    def shuffleAllCard(self):
        random.shuffle(self.deck_list)
            
def init_deck():
    card_list = []
    color_list = ['green', 'red', 'blue', 'black']
        
    for color in color_list:
        for i in range(2, 11):
            card_list.append(Card(color, i))
        
        card_list.append(Card(color, 'J'))
        card_list.append(Card(color, 'Q'))
        card_list.append(Card(color, 'K'))
        
    special_list = ['bird', 'pheonix', 'dragon', 'dog']
    
    for symbol in special_list:
        card_list.append(SpecialCard(symbol))
        
    return sorted(card_list, key=lambda card: card.symbol)

def main():
    
    list = init_deck()
    
    deck = Deck(list)
    
    print('\n before')
    deck.showAllCard()
    deck.shuffleAllCard()
    
    print('\n after')
    deck.showAllCard()
    
    assert deck.showTotalCardLen() == 52, "deck count not 52"
    
if __name__ == "__main__":
    main()
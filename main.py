from card import Card
from card import all_cards
def printLogo():
    print(f'#################################')
    print(f'#################################')
    print(f'#### Welcome in WarCardsGame ####')
    print(f'#################################')
    print(f'#################################')
if __name__ == '__main__':
    printLogo()
for Card in all_cards:
    print(Card.value, Card.kind, Card.power)

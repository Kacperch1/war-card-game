from card import Card


def printLogo():
    print(f'#################################')
    print(f'#################################')
    print(f'#### Welcome in WarCardsGame ####')
    print(f'#################################')
    print(f'#################################')


if __name__ == '__main__':
    printLogo()
    print(Card.all_cards())

class Card:
    def __init__(self, kind: str, value: str, power: int):
        self.kind = kind
        self.value = value
        self.power = power
two_hearts = Card("hearts", "two", 1)
three_hearts = Card("hearts", "three", 2)
four_hearts = Card("hearts", "four", 3)
five_hearts = Card("hearts", "five", 4)
six_hearts = Card("hearts", "six", 5)
seven_hearts = Card("hearts", "seven", 6)
eight_hearts = Card("hearts", "eight", 7)
nine_hearts = Card("hearts", "nine", 8)
ten_hearts = Card("hearts", "ten", 9)
j_hearts = Card("hearts", "jack", 10)
q_hearts = Card("hearts", "queen", 11)
k_hearts = Card("hearts", "king", 12)
a_hearts = Card("hearts", "ace", 13)

two_clubs = Card("clubs", "two", 1)
three_clubs = Card("clubs", "three", 2)
four_clubs = Card("clubs", "four", 3)
five_clubs = Card("clubs", "five", 4)
six_clubs = Card("clubs", "six", 5)
seven_clubs = Card("clubs", "seven", 6)
eight_clubs = Card("clubs", "eight", 7)
nine_clubs = Card("clubs", "nine", 8)
ten_clubs = Card("clubs", "ten", 9)
j_clubs = Card("clubs", "jack", 10)
q_clubs = Card("clubs", "queen", 11)
k_clubs = Card("clubs", "king", 12)
a_clubs = Card("clubs", "ace", 13)

two_diamonds = Card("diamonds", "two", 1)
three_diamonds = Card("diamonds", "three", 2)
four_diamonds = Card("diamonds", "four", 3)
five_diamonds = Card("diamonds", "five", 4)
six_diamonds = Card("diamonds", "six", 5)
seven_diamonds = Card("diamonds", "seven", 6)
eight_diamonds = Card("diamonds", "eight", 7)
nine_diamonds = Card("diamonds", "nine", 8)
ten_diamonds = Card("diamonds", "ten", 9)
j_diamonds = Card("diamonds", "jack", 10)
q_diamonds = Card("diamonds", "queen", 11)
k_diamonds = Card("diamonds", "king", 12)
a_diamonds = Card("diamonds", "ace", 13)

two_spades = Card("spades", "two", 1)
three_spades = Card("spades", "three", 2)
four_spades = Card("spades", "four", 3)
five_spades = Card("spades", "five", 4)
six_spades = Card("spades", "six", 5)
seven_spades = Card("spades", "seven", 6)
eight_spades = Card("spades", "eight", 7)
nine_spades = Card("spades", "nine", 8)
ten_spades = Card("spades", "ten", 9)
j_spades = Card("spades", "jack", 10)
q_spades = Card("spades", "queen", 11)
k_spades = Card("spades", "king", 12)
a_spades = Card("spades", "ace", 13)

hearts = [a_hearts, k_hearts, q_hearts, j_hearts, ten_hearts, nine_hearts, eight_hearts, seven_hearts, six_hearts, five_hearts,
         four_hearts, three_hearts, two_hearts]
hearts.reverse()
clubs = [a_clubs, k_clubs, q_clubs, j_clubs, ten_clubs, nine_clubs, eight_clubs, seven_clubs, six_clubs, five_clubs,
         four_clubs, three_clubs, two_clubs]
clubs.reverse()
diamonds = [a_diamonds, k_diamonds, q_diamonds, j_diamonds, ten_diamonds, nine_diamonds, eight_diamonds, seven_diamonds,
           six_diamonds, five_diamonds, four_diamonds, three_diamonds, two_diamonds]
diamonds.reverse()
spades = [a_spades, k_spades, q_spades, j_spades, ten_spades, nine_spades, eight_spades, seven_spades, six_spades,
          five_spades,  four_spades, three_spades, two_spades]
spades.reverse()

all_cards = hearts + clubs + diamonds + spades

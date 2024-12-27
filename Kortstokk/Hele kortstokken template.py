from pylab import randint

n = int(input("Hvor mange kort vil du trekke? "))

two_of_hearts = 0
three_of_hearts = 0
four_of_hearts = 0
five_of_hearts = 0
six_of_hearts = 0
seven_of_hearts = 0
eight_of_hearts = 0
nine_of_hearts = 0
ten_of_hearts = 0
jack_of_hearts = 0
queen_of_hearts = 0
king_of_hearts = 0
ace_of_hearts = 0

two_of_diamonds = 0
three_of_diamonds = 0
four_of_diamonds = 0
five_of_diamonds = 0
six_of_diamonds = 0
seven_of_diamonds = 0
eight_of_diamonds = 0
nine_of_diamonds = 0
ten_of_diamonds = 0
jack_of_diamonds = 0
queen_of_diamonds = 0
king_of_diamonds = 0
ace_of_diamonds = 0

two_of_clubs = 0
three_of_clubs = 0
four_of_clubs = 0
five_of_clubs = 0
six_of_clubs = 0
seven_of_clubs = 0
eight_of_clubs = 0
nine_of_clubs = 0
ten_of_clubs = 0
jack_of_clubs = 0
queen_of_clubs = 0
king_of_clubs = 0
ace_of_clubs = 0

two_of_spades = 0
three_of_spades = 0
four_of_spades = 0
five_of_spades = 0
six_of_spades = 0
seven_of_spades = 0
eight_of_spades = 0
nine_of_spades = 0
ten_of_spades = 0
jack_of_spades = 0
queen_of_spades = 0
king_of_spades = 0
ace_of_spades = 0

for i in range(n):
    kortstokk = randint(1, 53)
    
    if kortstokk == 1:
        two_of_hearts = two_of_hearts + 1
    elif kortstokk == 2:
        three_of_hearts = three_of_hearts + 1
    elif kortstokk == 3:
        four_of_hearts = four_of_hearts + 1
    elif kortstokk == 4:
        five_of_hearts = five_of_hearts + 1
    elif kortstokk == 5:
        six_of_hearts = six_of_hearts + 1
    elif kortstokk == 6:
        seven_of_hearts = seven_of_hearts + 1
    elif kortstokk == 7:
        eight_of_hearts = eight_of_hearts + 1
    elif kortstokk == 8:
        nine_of_hearts = nine_of_hearts + 1
    elif kortstokk == 9:
        ten_of_hearts = ten_of_hearts + 1
    elif kortstokk == 10:
        jack_of_hearts = jack_of_hearts + 1
    elif kortstokk == 11:
        queen_of_hearts = queen_of_hearts + 1
    elif kortstokk == 12:
        king_of_hearts = king_of_hearts + 1
    elif kortstokk == 13:
        ace_of_hearts = ace_of_hearts + 1

    elif kortstokk == 14:
        two_of_diamonds = two_of_diamonds + 1
    elif kortstokk == 15:
        three_of_diamonds = three_of_diamonds + 1
    elif kortstokk == 16:
        four_of_diamonds = four_of_diamonds + 1
    elif kortstokk == 17:
        five_of_diamonds = five_of_diamonds + 1
    elif kortstokk == 18:
        six_of_diamonds = six_of_diamonds + 1
    elif kortstokk == 19:
        seven_of_diamonds = seven_of_diamonds + 1
    elif kortstokk == 20:
        eight_of_diamonds = eight_of_diamonds + 1
    elif kortstokk == 21:
        nine_of_diamonds = nine_of_diamonds + 1
    elif kortstokk == 22:
        ten_of_diamonds = ten_of_diamonds + 1
    elif kortstokk == 23:
        jack_of_diamonds = jack_of_diamonds + 1
    elif kortstokk == 24:
        queen_of_diamonds = queen_of_diamonds + 1
    elif kortstokk == 25:
        king_of_diamonds = king_of_diamonds + 1
    elif kortstokk == 26:
        ace_of_diamonds = ace_of_diamonds + 1

    elif kortstokk == 27:
        two_of_clubs = two_of_clubs + 1
    elif kortstokk == 28:
        three_of_clubs = three_of_clubs + 1
    elif kortstokk == 29:
        four_of_clubs = four_of_clubs + 1
    elif kortstokk == 30:
        five_of_clubs = five_of_clubs + 1
    elif kortstokk == 31:
        six_of_clubs = six_of_clubs + 1
    elif kortstokk == 32:
        seven_of_clubs = seven_of_clubs + 1
    elif kortstokk == 33:
        eight_of_clubs = eight_of_clubs + 1
    elif kortstokk == 34:
        nine_of_clubs = nine_of_clubs + 1
    elif kortstokk == 35:
        ten_of_clubs = ten_of_clubs + 1
    elif kortstokk == 36:
        jack_of_clubs = jack_of_clubs + 1
    elif kortstokk == 37:
        queen_of_clubs = queen_of_clubs + 1
    elif kortstokk == 38:
        king_of_clubs = king_of_clubs + 1
    elif kortstokk == 39:
        ace_of_clubs = ace_of_clubs + 1

    elif kortstokk == 40:
        two_of_spades = two_of_spades + 1
    elif kortstokk == 41:
        three_of_spades = three_of_spades + 1
    elif kortstokk == 42:
        four_of_spades = four_of_spades + 1
    elif kortstokk == 43:
        five_of_spades = five_of_spades + 1
    elif kortstokk == 44:
        six_of_spades = six_of_spades + 1
    elif kortstokk == 45:
        seven_of_spades = seven_of_spades + 1
    elif kortstokk == 46:
        eight_of_spades = eight_of_spades + 1
    elif kortstokk == 47:
        nine_of_spades = nine_of_spades + 1
    elif kortstokk == 48:
        ten_of_spades = ten_of_spades + 1
    elif kortstokk == 49:
        jack_of_spades = jack_of_spades + 1
    elif kortstokk == 50:
        queen_of_spades = queen_of_spades + 1
    elif kortstokk == 51:
        king_of_spades = king_of_spades + 1
    elif kortstokk == 52:
        ace_of_spades = ace_of_spades + 1

print("two of hearts:", two_of_hearts, two_of_hearts / n * 100, "%")
print(three_of_hearts, three_of_hearts / n * 100, "%")
print(four_of_hearts, four_of_hearts / n * 100, "%")
print(five_of_hearts, five_of_hearts / n * 100, "%")
print(six_of_hearts, six_of_hearts / n * 100, "%")
print(seven_of_hearts, seven_of_hearts / n * 100, "%")
print(eight_of_hearts, eight_of_hearts / n * 100, "%")
print(nine_of_hearts, nine_of_hearts / n * 100, "%")
print(ten_of_hearts, ten_of_hearts / n * 100, "%")
print(jack_of_hearts, jack_of_hearts / n * 100, "%")
print(queen_of_hearts, queen_of_hearts / n * 100, "%")
print(king_of_hearts, king_of_hearts / n * 100, "%")
print(ace_of_hearts, ace_of_hearts / n * 100, "%")

print(two_of_diamonds, two_of_diamonds / n * 100, "%")
print(three_of_diamonds, three_of_diamonds / n * 100, "%")
print(four_of_diamonds, four_of_diamonds / n * 100, "%")
print(five_of_diamonds, five_of_diamonds / n * 100, "%")
print(six_of_diamonds, six_of_diamonds / n * 100, "%")
print(seven_of_diamonds, seven_of_diamonds / n * 100, "%")
print(eight_of_diamonds, eight_of_diamonds / n * 100, "%")
print(nine_of_diamonds, nine_of_diamonds / n * 100, "%")
print(ten_of_diamonds, ten_of_diamonds / n * 100, "%")
print(jack_of_diamonds, jack_of_diamonds / n * 100, "%")
print(queen_of_diamonds, queen_of_diamonds / n * 100, "%")
print(king_of_diamonds, king_of_diamonds / n * 100, "%")
print(ace_of_diamonds, ace_of_diamonds / n * 100, "%")

print(two_of_clubs, two_of_clubs / n * 100, "%")
print(three_of_clubs, three_of_clubs / n * 100, "%")
print(four_of_clubs, four_of_clubs / n * 100, "%")
print(five_of_clubs, five_of_clubs / n * 100, "%")
print(six_of_clubs, six_of_clubs / n * 100, "%")
print(seven_of_clubs, seven_of_clubs / n * 100, "%")
print(eight_of_clubs, eight_of_clubs / n * 100, "%")
print(nine_of_clubs, nine_of_clubs / n * 100, "%")
print(ten_of_clubs, ten_of_clubs / n * 100, "%")
print(jack_of_clubs, jack_of_clubs / n * 100, "%")
print(queen_of_clubs, queen_of_clubs / n * 100, "%")
print(king_of_clubs, king_of_clubs / n * 100, "%")
print(ace_of_clubs, ace_of_clubs / n * 100, "%")

print(two_of_spades, two_of_spades / n * 100, "%")
print(three_of_spades, three_of_spades / n * 100, "%")
print(four_of_spades, four_of_spades / n * 100, "%")
print(five_of_spades, five_of_spades / n * 100, "%")
print(six_of_spades, six_of_spades / n * 100, "%")
print(seven_of_spades, seven_of_spades / n * 100, "%")
print(eight_of_spades, eight_of_spades / n * 100, "%")
print(nine_of_spades, nine_of_spades / n * 100, "%")
print(ten_of_spades, ten_of_spades / n * 100, "%")
print(jack_of_spades, jack_of_spades / n * 100, "%")
print(queen_of_spades, queen_of_spades / n * 100, "%")
print(king_of_spades, king_of_spades / n * 100, "%")
print(ace_of_spades, ace_of_spades / n * 100, "%")
answers = []
questions = []
correct_answers = []

try:
    AS = int(input("Hvor Mange Spørsmål vil du stille? "))  # Antall Spørsmål
    print(AS, "Spørsmål godkjent")
except ValueError:
    print("Please enter a valid number")
    exit()

for i in range(AS):
    question = input(f"Spørsmål {i+1}: ") 
    questions.append(question)
    
    num_options = int(input("Hvor Mange Svarmuligheter? "))
    options = []
    
    for j in range(num_options):
        option_text = input(f"Skriv inn svaralternativ {j+1}: ")
        options.append(option_text)
    
    answers.append(options)
    
    correct_option = int(input("Hvilket svaralternativ er riktig? (Oppgi nummeret) ")) - 1
    correct_answers.append(correct_option)

score = 0
print("\nLa oss starte quizen!")

for i in range(AS):
    print(f"\nSpørsmål {i+1}: {questions[i]}")
    for j, option in enumerate(answers[i]):
        print(f"{j+1}. {option}")
    
    try:
        user_answer = int(input("Velg ditt svar (skriv inn nummeret): ")) - 1
        
        if user_answer == correct_answers[i]:
            print("Riktig svar!")
            score += 1
        else:
            print("Feil svar.")
    except (ValueError, IndexError):
        print("Ugyldig svar. Dette spørsmålet blir hoppet over.")

# Resultat
print(f"\nQuizen er ferdig! Du fikk {score} av {AS} riktige.")

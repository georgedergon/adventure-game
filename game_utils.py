# Funktion zur Präsentation und Überprüfung eines Rätsels
def solve_riddle(riddle):
    print(f"rätsel:{riddle}")
    answer= input("Deine Antwort:").lower()

# Beispiel: Das Rätsel könnte eine bestimmte Antwort erfordern
    if answer == "Zwei":
       print("Richtig")

def end_game():
    print("end_game THX for playing")        
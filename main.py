from game_utils import solve_riddle, end_game


# Begrüßung des Spielers und Spielregeln erklären
def greeting():
    print("Willkommen bei Die verlorene Schatzsuche!")
    print("Dein Ziel ist es den verlorenen Schatz zu finden.")
    print("Du wirst in verschiedene Räume gehen um die rätsel zu lösen")
    print("Viel Glück!\n")

    # Betreten eines Raumes und Beschreibung der verfügbaren Aktionen
def enter_room(room):
    if room == "Eingangshalle":
        print("Du befindest dich in der Eingangshalle ,es gibt Türen nach Norden,Süden,Weste,Osten.")
        print("Welche Tür möchtest du öffnen?")
    elif room == "Westen":
        print("Du hast 5 Äpfel und 3 Äpfel wurden von dir weggenommen , wieviel bleiben noch für dich übrig?.")
        while True:
            user_input=input("Gib deine Aktion ein (Norden,Süden,Osten,Westen)")
        print("Das Rätsel ist gelöst! Eine Tür zur Schatzkammer öffnet sich.") 


end_game()
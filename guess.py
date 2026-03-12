import random

beste_score = float('inf')

while True:
    print("\nVælg din sværhedsgrad:")
    print("1 = Let (1-50)")
    print("2 = Medium (1-200)")
    print("3 = Svær (1-500)")

    valg = input("Indtast 1, 2 eller 3: ")

    if valg == "1":
        max_tal = 50
    elif valg == "2":
        max_tal = 200
    else:
        max_tal = 500

    hemmeligt_tal = random.randint(1, max_tal)
    forsøg = 0

    print("Velkommen til gæt tallet spillet")
    print(f"Jeg har valgt et tal mellem 1 og {max_tal}")
    print("Lavet af Cilius Timm")
    print("Alvin er TUFF")

    while True:
        try:
            gæt = int(input("Indtast dit gæt: "))
            forsøg += 1

            if gæt < hemmeligt_tal:
                print("For lavt, prøv igen")
            elif gæt > hemmeligt_tal:
                print("For højt, prøv igen")
            else:
                print(f"\nTillykke! Du gættede tallet {hemmeligt_tal} på {forsøg} forsøg.")
                if forsøg < beste_score:
                    beste_score = forsøg
                break

        except ValueError:
            print("Du kan kun skrive tal.")

    # efter man vinder:

    print(f"Highscore er stadig {beste_score} forsøg.")

    print("NY RUNDE!")
    spil_igen = input("Vil du spille igen? (ja/nej): ")

    if spil_igen.lower() != "ja":
        print("GG Tak for spillet, vi ses næste gang!")
        break
    else:
        # Loop back to play again
        continue

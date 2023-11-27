geheimzahl = 15
eingabe = 0
zaehler = 0

while eingabe != geheimzahl:
	eingabe = int(input("Bitte eine Ganzzahl eingeben: "))

	if eingabe < geheimzahl:
		print("Ihre Eingabe war zu klein")
		zaehler = zaehler +1
	if eingabe > geheimzahl:
		print("Ihre Eingabe war zu groß")

print("Sie haben die Zahl erraten")

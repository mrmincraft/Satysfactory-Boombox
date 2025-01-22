import RPi.GPIO as GPIO

# Initialisation de la numerotation et des E/S
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

# Si on detecte un appui sur le bouton, on allume la LED 
# et on attend que le bouton soit relache
while True:
    state = GPIO.input(8)
    if not state:
        # on a appuye sur le bouton connecte sur la broche 8
        print("Bouton appuyé")
        while not state:
            state = GPIO.input(8)
        print("Le bouton n'est pas appuyé")

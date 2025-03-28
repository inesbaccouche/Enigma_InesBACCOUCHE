import random

# Fonction pour faire tourner un rotor d'un nombre donné de positions
def rotate_rotor(rotor, steps):
    return rotor[steps:] + rotor[:steps]

# Fonction pour chiffrer un message avec la machine Enigma
def enigma_encrypt(message, rotors, positions):
    encrypted_message = ""
    
    # Parcours chaque lettre du message
    for i, letter in enumerate(message.upper()):
        if letter.isalpha():  # Si la lettre est une lettre de l'alphabet
            # Passage à travers les 3 rotors
            for j in range(3):
                index = (ord(letter) - ord('A') + positions[j]) % 26
                letter = rotors[j][index]  # On remplace la lettre par la lettre correspondante dans le rotor
            
            encrypted_message += letter  # On ajoute la lettre chiffrée au message
            # Les rotors tournent après chaque lettre
            positions[0] = (positions[0] + 1) % 26
            if i % 26 == 0:
                positions[1] = (positions[1] + 1) % 26
            if i % (26 * 26) == 0:
                positions[2] = (positions[2] + 1) % 26
        else:
            encrypted_message += letter  # Si ce n'est pas une lettre, on la garde telle quelle
    
    return encrypted_message

# Fonction pour déchiffrer un message
def enigma_decrypt(encrypted_message, rotors, positions):
    decrypted_message = ""
    
    # Parcours chaque lettre du message chiffré
    for i, letter in enumerate(encrypted_message.upper()):
        if letter.isalpha():  # Si la lettre est une lettre de l'alphabet
            # Passage inverse à travers les rotors
            for j in range(2, -1, -1):
                index = rotors[j].index(letter)
                letter = chr((index - positions[j]) % 26 + ord('A'))
            
            decrypted_message += letter  # On ajoute la lettre déchiffrée au message
            # Les rotors tournent après chaque lettre
            positions[0] = (positions[0] + 1) % 26
            if i % 26 == 0:
                positions[1] = (positions[1] + 1) % 26
            if i % (26 * 26) == 0:
                positions[2] = (positions[2] + 1) % 26
        else:
            decrypted_message += letter  # Si ce n'est pas une lettre, on la garde telle quelle
    
    return decrypted_message

# Fonction principale
def main():
    print("\nBienvenue dans le simulateur de la machine Enigma !")
    print("Prêt à découvrir la magie du chiffrement ? Allons-y !\n")
    
    # Définition des rotors utilisés dans la machine Enigma
    rotors = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",  # Rotor 1
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",  # Rotor 2
        "BDFHJLCPRTXVZNYEIWGAKMUSQO"   # Rotor 3
    ]
    
    # Demande à l'utilisateur d'entrer les positions des rotors
    positions = [
        int(input("Entrez la position du rotor 1 (1-25) : ")),
        int(input("Entrez la position du rotor 2 (1-25) : ")),
        int(input("Entrez la position du rotor 3 (1-25) : "))
    ]
    
    # Affiche les positions des rotors choisies par l'utilisateur
    print(f"\nPositions des rotors choisies : {positions[0]}, {positions[1]}, {positions[2]}\n")
    
    # Demande à l'utilisateur d'entrer un message à chiffrer
    message = input("Entrez votre message à chiffrer (les lettres uniquement) : \n")
    print("\nChiffrement en cours...")

    # Chiffre le message
    encrypted_message = enigma_encrypt(message, rotors, positions.copy())
    print(f"\nMessage chiffré : {encrypted_message}\n")
    
    print("Déchiffrement en cours...\n")

    # Déchiffre le message
    decrypted_message = enigma_decrypt(encrypted_message, rotors, positions.copy())
    print(f"Message déchiffré : {decrypted_message}\n")
    
    print("Fin du programme. Merci d'avoir utilisé Enigma ! À bientôt.")

# Exécution de la fonction principale
if __name__ == "__main__":
    main()

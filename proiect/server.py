import socket
import threading

s = socket.socket()
port = 12345

s.bind(('', port))
s.listen(2)

player = 0
event_player1= threading.Event()
event_word_update=threading.Event()

word=""
description=""
word_to_guess=""

spanzuratori=[
    "-",
    " - \n  O",
    " - \n  O \n  |",
    " - \n  O \n /|   ",
    " - \n  O \n /|\   ",
    " - \n  O \n /|\ \n /      ",
    " - \n  O \n /|\ \n / \     "
]
mistakes=0
won=0 
letters=[]
letter=""
def valid_player1(string):
    return string.isalpha()

def valid_player2(string):
    return string.isalpha() and len(string) == 1

def repetitive_letter(string):
    global letters
    if string in letters:
        return True
    else:
        letters.append(string)
        return False

def create_word_to_guess(string):
    global word_to_guess
    length=len(string)
    while length:
        word_to_guess+="_"
        length-=1

def modify_word_to_guess(string):
    global word_to_guess,mistakes,word
    if string in word:
        string_list=list(word_to_guess)
        for i in range(0,len(word)):
            if word[i] == string:
                string_list[i]=word[i]
        word_to_guess = ''.join(string_list)
    else:
        mistakes+=1 

def current_state_of_game():
    global word_to_guess,mistakes,spanzuratori,letter
    return f'Current word guessed: {word_to_guess} \n Letter tried: {letter} \n Mistakes: {mistakes} \n {spanzuratori[mistakes]}'

def verify_end_game_reached():
    global won,word_to_guess,mistakes
    if "_" not in word_to_guess:
        won=1
        return True
    else:
        if mistakes==6:
            won=0
            return True
        else:
            return False
def on_new_client(clientsocket, addr,player):
    global word,description,won,word_to_guess,mistakes,letter,letters
    word=""
    description=""
    word_to_guess=""
    mistakes=0
    won=0
    letters=[]
    letter=""
    try:
        if player % 2 != 0:
            nr=2
            clientsocket.send('Welcome player 1, choose a word: '.encode())
            while nr:
                string1 = clientsocket.recv(1024).decode()
                string = string1.lower()
                print(string)
                if nr==2:
                    valoare = valid_player1(string)
                    if valoare:
                        word=string
                        clientsocket.send('Now choose a description: '.encode())
                        nr-=1
                    else:
                        clientsocket.send('Bad word, try again'.encode())
                else:
                    description=string
                    clientsocket.send('Game begins'.encode())
                    nr-=1
                    event_player1.set()
                    while True:
                        event_word_update.wait()
                        event_word_update.clear()
                        if verify_end_game_reached()==True:
                            if won == 1:
                                clientsocket.send(f'{current_state_of_game()} \n Game finished - player won!'.encode())
                            else:
                                clientsocket.send(f'{current_state_of_game()} \n Game finished - player lost!'.encode())
                            break
                        else:
                            clientsocket.send(current_state_of_game().encode())
        else:
            event_player1.wait()
            event_player1.clear()
            create_word_to_guess(word)
            clientsocket.send(f'Welcome player 2! \n The word is: {word_to_guess} \n The description is: {description} \n Start guessing: '.encode())
            while True:
                string1 = clientsocket.recv(1024).decode()
                letter = string1.lower()
                print(letter)
                valoare = valid_player2(letter)
                if valoare:
                    if repetitive_letter(letter)==False:
                        modify_word_to_guess(letter)
                        event_word_update.set()
                        if verify_end_game_reached():
                            if won==1:
                                clientsocket.send(f'{word_to_guess} \n mistakes:{mistakes} \n {spanzuratori[mistakes]}\n You won!'.encode())
                            else:
                                clientsocket.send(f'{word_to_guess} \n mistakes:{mistakes} \n {spanzuratori[mistakes]}\n You lost!'.encode())
                            break
                        else:
                            clientsocket.send(f'{word_to_guess} \n mistakes:{mistakes} \n You make {6-mistakes} mistakes and you lose! \n {spanzuratori[mistakes]}'.encode())
                    else:
                        clientsocket.send(f'Letter already tried'.encode())
                        event_word_update.set()
                else:
                    clientsocket.send('Invalid letter'.encode())
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print(f"Player {player} disconnected")
        clientsocket.close()

while True:
    c, addr = s.accept()
    player += 1
    t = threading.Thread(target=on_new_client, args=(c, addr,player))
    t.start()

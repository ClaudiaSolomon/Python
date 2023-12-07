import socket
import threading

s = socket.socket()
port = 12345

s.bind(('', port))
s.listen(2)

player = 0
players = []
event_player1= threading.Event()
event_player2=threading.Event()

word=""
description=""
word_to_guess=""

spanzuratori=[
    "",
    "O",
    "O \
     |",
    "O \
    /|   ",
    "O \
    /|\   ",
    "O \
    /|\ \
    /      ",
    "O \
    /|\ \
    / \     "
]
mistakes=0
won=0 

def valid_player1(string):
    return string.isalpha()

def valid_player2(string):
    return string.isalpha() and len(string) == 1

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
    global word,description,won,word_to_guess
    try:
        players.append(clientsocket)
        if player % 2 != 0:
            nr=2
            clientsocket.send('Welcome player 1, choose a word: '.encode())
            while nr:
                string = clientsocket.recv(1024).decode()
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
                    event_player2.wait()
                    break
            if verify_end_game_reached():
                if won == 1:
                    clientsocket.send('Game finished - player won!'.encode())
                else:
                    clientsocket.send('Game finished - player lost!'.encode())
                event_player2.clear() 
        else:
            event_player1.wait()
            create_word_to_guess(word)
            clientsocket.send(f'Welcome player 2! \n The word is: {word_to_guess} \n The description is: {description} \n Start guessing: '.encode())
            while True:
                string = clientsocket.recv(1024).decode()
                print(string)
                valoare = valid_player2(string)
                if valoare:
                    modify_word_to_guess(string)
                    if verify_end_game_reached():
                        if won==1:
                            clientsocket.send(f'{word_to_guess} \n {spanzuratori[mistakes]} \n You won!'.encode())
                        else:
                            clientsocket.send(f'{word_to_guess} \n {spanzuratori[mistakes]} \n You lost!'.encode())
                        event_player2.set()
                        break
                    else:
                        clientsocket.send(f'{word_to_guess} \n {spanzuratori[mistakes]}'.encode())
                else:
                    clientsocket.send('Invalid letter'.encode())
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print(f"Player {player} disconnected")
        players.remove(clientsocket)
        # clientsocket.close()
        # if players==[]:
        #     s.close()

while True:
    c, addr = s.accept()
    player += 1
    t = threading.Thread(target=on_new_client, args=(c, addr,player))
    t.start()

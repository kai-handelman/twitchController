import socket
import sys
import threading
import time


###################################
# CONSTANTS
# Twitch Contants
SERVER = "irc.twitch.tv"
PORT = 6667
# Name of Personal Acc/Acc that is acting as "BOT"
name = "nan"
# Do not share - Our Idenifier Key
password = "nan
# Channel the clinet is observing
channelName = "stanz"

###################################
# CONNECTING TO TWITCH
# Connects socket client to Twitch
client = socket.socket()
client.connect((SERVER, PORT))
# Confirm to twitch by verification
client.send(("PASS "+ password+"\n").encode())
client.send(("NICK "+ name+"\n").encode())
client.send(("JOIN #"+ channelName+"\n").encode())

###################################

def escape():
    global run 
    run = True
    while run:
        cmd = input()
        if cmd != "":
            run = False
            print("**********SHUTTING DOWN**********")
            sys.exit()

def chatInputManager():
    global run
    def startChat():
        print("***********************************************************")
        print("**** ENTER ANY COMMNAD IN THE LINE TO STOP THE PROGRAM ****")
        print("***********************************************************")
        time.sleep(1)
        while True: #Waits for the client to officially enter
            bufferMessage = client.recv(1024).decode()
            print(bufferMessage)
            for line in bufferMessage.split('\n')[0:-1]:
                if("End of /NAMES list" in line):
                    print('Sucessfully to Twitch!\nCurrently in ' + channelName + '\'s chat')
                    time.sleep(1)
                    return
    startChat()
    #**Might be useful down the line
    #client.send("CAP REQ :twitch.tv/tags\r\n".encode())
    
    #Continues to run and motinor the chat unless specified
    def userMessageParse(message):
        c = message.count(":")
        user = (message.split(":",c))[1].split("!",1)[0]
        mes = (message.split(":",c))[c]
        return user, mes

    while run:
        try:
            logM = client.recv(2048).decode()
        except:
            logM = ""
        for line in logM.split("\r\n"):
            if line == "":
                continue
            elif line == "PING :tmi.twitch.tv":
                print("Received Ping")
                client.send(("PONG :tmi.twitch.tv").encode())
                print("Sent Pong")
                continue
            else:
                try:
                    # Get the USER and MESSAGE
                    user, command = userMessageParse(line)
                    print("User " + user + " said: " + command)
                    # print(line)
                except Exception:
                    pass
    print("**********Program Stopped**********")

def gameOutput(message):
    if message[0] != "!":
        return
    command = message.split("!").lower()
    if command == "up":
        pass
    elif command == "down":
        pass
    elif command == "left":
        pass
    elif command == "right":
        pass
    elif command == "jump":
        pass
    elif command == "itemplace":
        pass
    elif command == "switchitem":
        pass
    elif command == "absorb":
        pass    

def main():
    if __name__ == "__main__":
        # Implement Thread System
        threadOne = threading.Thread(target = chatInputManager)
        threadOne.start()
        threadTwo = threading.Thread(target = escape)
        threadTwo.start()


main()



#3) Get info about users
#4) Find a parser
#5) Find a controller

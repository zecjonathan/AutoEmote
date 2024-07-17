import socket
import collections
import time

server = "irc.chat.twitch.tv"
port = 6667
nickname = input("Username?: ")
token = input("Twitch token (get here: https://twitchapps.com/tmi/)?: ") # get here https://twitchapps.com/tmi/ 
channel = "#" + input("Channel to chat on?: ")

# Connect to Twitch IRC
sock = socket.socket()
sock.connect((server, port))

# Perform IRC handshake
sock.send(f"PASS {token}\n".encode("utf-8"))
sock.send(f"NICK {nickname}\n".encode("utf-8"))
sock.send(f"JOIN {channel}\n".encode("utf-8"))

# List to keep track of last messages
last_messages = collections.deque(maxlen=10)

def check_last_five_logs_for_message(message):
    count = 0
    for msg in last_messages:
        if message == msg:
            count += 1
    return count

def send_chat(chat):
    message = chat.strip()  # Remove leading/trailing whitespace
    if message:  # Check if the message is not empty
        command = f"PRIVMSG {channel} :{message}\n"
        sock.send(command.encode("utf-8"))
        print(f"Sent message to {channel}: {message}")
        time.sleep(50)  # Pause for 50 seconds after sending a message

# Main loop to receive messages
while True:
    resp = sock.recv(2048).decode("utf-8")
    if resp.startswith("PING"):
        sock.send("PONG\n".encode("utf-8"))
    elif len(resp) > 0:
        message = resp.split(":")[-1].rstrip()

        # Add message to last_messages
        last_messages.append(message)

        if check_last_five_logs_for_message(message) > 2:
            send_chat(message)

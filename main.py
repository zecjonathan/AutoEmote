import socket
import logging
import collections
import time

server = "irc.chat.twitch.tv"
port = 6667
nickname = "cvcjonathan"
token = "oauth:authcode hier hin" # get here https://twitchapps.com/tmi/
channel = "#LetsHugoTV"

# Connect to Twitch IRC
sock = socket.socket()
sock.connect((server, port))

# Perform IRC handshake
sock.send(f"PASS {token}\n".encode("utf-8"))
sock.send(f"NICK {nickname}\n".encode("utf-8"))
sock.send(f"JOIN {channel}\n".encode("utf-8"))

# Configure logging to a file
logging.basicConfig(
    filename='chat.log',  # Specify the filename here
    level=logging.INFO,       # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(message)s',  # Define the format of the log messages
)

def check_last_five_logs_for_message(message):
    logfile = 'chat.log'
    with open(logfile, 'r') as file:
        # Read the last 10 lines from the file
        last_lines = collections.deque(file, 10)
        
    count = 0
    for line in last_lines:
        if message == line.strip():
            count += 1

    return count

def send_chat(chat):
    message = chat.strip()  # Remove leading/trailing whitespace
    if message:  # Check if the message is not empty
        command = f"PRIVMSG {channel} :{message}\n"
        sock.send(command.encode("utf-8"))
        print(f"Sent message to {channel}: {message}")
        time.sleep(20)  # Pause for 20 seconds after sending a message

# Main loop to receive messages
while True:
    resp = sock.recv(2048).decode("utf-8")
    if resp.startswith("PING"):
        sock.send("PONG\n".encode("utf-8"))
    elif len(resp) > 0:
        message = resp.split(":")[-1].rstrip()

        logging.info(message)  # Logs all chat messages

        if check_last_five_logs_for_message(message) > 2:
            send_chat(message)

# AutoEmote

token hier bekommen (bekommt ihr hier https://twitchapps.com/tmi/)

## Setup-Anleitung

1. **Repository klonen**
   - Klone dieses Repository auf deine lokale Maschine mit Git:
     ```
     git clone https://github.com/dein/repository.git
     cd repository-name
     ```

2. **Abhängigkeiten installieren**
   - Stelle sicher, dass du Python 3.x auf deinem System installiert hast.
   - Installiere die erforderlichen Python-Pakete mit pip:
     ```
     pip install collections logging socket time
     ```

## Verwendung

1. **Skript ausführen**
   - Starte das Python-Skript in deiner Konsole oder deinem Terminal:
     ```
     python twitch_bot.py
     ```
     ```
     python3 twitch_bot.py
     ```
   - Folge den Anweisungen, um deinen Twitch-Benutzernamen, das Token und den Kanal einzugeben, dem du beitreten möchtest.

2. **Interaktion im Twitch-Chat**
   - Sobald verbunden, wird der Bot dem angegebenen Kanal auf Twitch beitreten.
   - Alle Chat-Nachrichten werden in `chat.log` im gleichen Verzeichnis wie das Skript protokolliert.
   - Wenn der Bot feststellt, dass eine Nachricht mehr als dreimal innerhalb der letzten 10 protokollierten Nachrichten wiederholt wurde, sendet er diese automatisch in den Chat. Das passiert meißtens, wenn der ganze Chat emotes spamt.

3. **Ausgabe verwalten**
   - Es wird max. alle 20s eine Nachricht gesendet.


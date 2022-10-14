# Arduino-buzzer-music
### A set of python Script and Arduino code to create music out of a Midi file.
![](https://img.shields.io/pypi/pyversions/mido?style=flat-square)
![](https://img.shields.io/github/license/SuhJae/arduino-buzzer-music?style=flat-square)

## Introduction
This project allows you to easily create a sequence of notes from a Midi file and play it on a buzzer.

## Requirements
* [Python 3.6+](https://www.python.org/downloads/)

**Python packages**
* [Mido](https://pypl.org/project/mido/) (`pip install mido`)

## Setup
1. Clone/download this repository.
2. You can upload the `buzzer.ino` to your Arduino to test the default music (Super Mario Bros Theme).
3. You can create your music by changing the `music.mid` file to your own.
4. After changing the `music.mid` file, run `python3 main.py`, which will print out the sequence of notes and their duration.
5. Edit the `buzzer.ino` file to change the notes' sequence and duration.
    ```
   //list of notes
    int notes[] = {330, 330, 330, 262, 330, ... }
    //list of delay
    int duration[] = {161, 324, 324, 161, 324, ... }
   ```
6. Upload the `buzzer.ino` to your Arduino and enjoy your music!

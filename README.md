# A-Pi-Christmas

### Overview
This is a Christmas-themed project featuring 18 flowing LEDs, four buzzers playing Christmas tunes, and a Pygame-based holiday-themed animation; all done on the Raspberry Pi 4 Model B. Credit for the "buzzer_music.py" code goes to james1236 via the buzzer_music repository, and credit for the Snowflake class at animation.py goes to EruditeCode via "class_Snowflake.py" from the snow_simulator repository. Check out (https://github.com/james1236/buzzer_music) and (https://github.com/EruditeCode/snow_simulator) respectively for more information. 

If you do not have a Raspberry Pi 4 Model B, I recommend you buy the Raspberry Pi 4 desktop kit at (https://www.raspberrypi.com/products/raspberry-pi-4-desktop-kit/). The kit comes with a microSD card pre-loaded with Raspberry Pi OS, a keyboard, a mouse, a power supply, HDMI cables, an instruction manual, and a case for the Raspberry Pi. Follow the manual, set up the Pi, and then come back to this project.

### Components
1) 1 Raspberry Pi 4 Model B
2) 2 solderless breadboards
3) 18 LEDs (6 reds, 6 greens, 6 whites)
4) 18 330 Ω resistors
5) 4 buzzers (active or passive)

![image](https://github.com/mvinza34/A-Pi-Christmas/assets/89809703/fe967c6f-7c30-490a-afb0-8f094cf3486d)
![image](https://github.com/mvinza34/A-Pi-Christmas/assets/89809703/f9b7748c-cbdf-4863-9a52-ab4172356a34)
![image](https://github.com/mvinza34/A-Pi-Christmas/assets/89809703/e0cc6d3f-5641-47a1-af2b-bcce1920f391)
![image](https://github.com/mvinza34/A-Pi-Christmas/assets/89809703/1d06ce5e-34ec-4a39-b381-84ea7ed043e5)
![image](https://github.com/mvinza34/A-Pi-Christmas/assets/89809703/deaca4b2-57be-469d-a687-e3fa8ded298d)

### Instructions
1) Design the circuit based on the provided breadboard image and schematic below:

![Pi4_Christmas_bb](https://github.com/mvinza34/A-Pi-Christmas/assets/89809703/e19bd6b7-8da3-49e8-9fa1-e589f132ca03)
![Pi4_Christmas_schem](https://github.com/mvinza34/A-Pi-Christmas/assets/89809703/a8b7ba40-de1d-4967-aeb9-59c298127f77)

2) Plug in the Raspberry Pi 4 Model B.
3) Copy the files in this repository to the Pi.
4) Go to 'Terminal' and install pygame - Community Edition using the command 'pip install pygame-ce'.
5) Open main.py and settings.py
6) To add more holiday-themed music, go to onlinesequencer.net and pick a song. Click edit, select all notes with CTRL + A, and then copy them with CTRL + C.
7) Go to settings.py and paste the string. Make sure to remove "Online Sequencer:120233:" from the start and ";:" from the end, or else you will get an error when running main.py 
8) Run main.py
9) Enjoy the music, lights, and a nice little animation at the end, and have a wonderful Happy Holidays! 

   
Code and other files underway...

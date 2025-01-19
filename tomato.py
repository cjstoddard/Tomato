from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
import time
import RPi.GPIO as GPIO
import os
import random

# OLED and GPIO setup
i2c_port = 1
OLED_address = 0x3c
LEDpin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDpin, GPIO.OUT)

serial = i2c(port=i2c_port, address=OLED_address)
device = ssd1306(serial)

# Paths
pi_parent_dir = os.path.dirname(os.path.abspath(__file__))
picdir = os.path.join(pi_parent_dir, "pics")

# Font setup
try:
    fontdir = os.path.join(pi_parent_dir, "fonts")
    font24 = ImageFont.truetype(os.path.join(fontdir, "Font.ttc"), 24)
    font16 = ImageFont.truetype(os.path.join(fontdir, "Font.ttc"), 16)
    font12 = ImageFont.truetype(os.path.join(fontdir, "Font.ttc"), 12)
except IOError:
    font24 = ImageFont.load_default()
    font16 = ImageFont.load_default()
    font12 = ImageFont.load_default()

# Main function
def main():
    GPIO.output(LEDpin, GPIO.HIGH)
    print("\nGood morning.")
    print("LED on")

    try:
        while True:
            mood = roll_1d24()
            new_face = get_face(mood)

            # Displaying the face
            face_path = os.path.join(picdir, new_face)
            if os.path.exists(face_path):
                face = Image.open(face_path)
                with canvas(device) as draw:
                    draw.bitmap((0, 0), face, fill=255)
            else:
                print(f"Error: Image '{new_face}' not found!")

            print(f"Mood: {mood}, Displaying: {new_face}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nGood night.")
        print("LED off")
        GPIO.output(LEDpin, GPIO.LOW)
        GPIO.cleanup()
        exit()

# Function to get the face path based on mood
def get_face(mood):
    faces = {
        1: "ANGRY.png", 2: "AWAKE.png", 3: "BORED.png", 4: "BROKEN.png",
        5: "COOL.png", 6: "DEBUG.png", 7: "DEMOTIVATED.png", 8: "EXCITED.png",
        9: "FRIEND.png", 10: "GRATEFUL.png", 11: "HAPPY.png", 12: "INTENSE.png",
        13: "LONELY.png", 14: "LOOK_L_HAPPY.png", 15: "LOOK_L.png",
        16: "LOOK_R_HAPPY.png", 17: "LOOK_R.png", 18: "MOTIVATED.png",
        19: "SAD.png", 20: "SLEEP2.png", 21: "SMART.png", 22: "UPLOAD1.png",
        23: "UPLOAD2.png", 24: "UPLOAD.png"
    }
    return faces.get(mood, "UNKNOWN.png")  # Default to UNKNOWN.png if mood is invalid

# Function to roll a 1d24 dice
def roll_1d24():
    return random.randint(1, 24)

if __name__ == "__main__":
    main()

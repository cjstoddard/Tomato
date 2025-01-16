from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
import RPi.GPIO as GPIO
import os

i2c_port = 1
OLED_address = 0x3C
pinLED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinLED, GPIO.OUT)

serial = i2c(port=i2c_port, address=OLED_address)
device = ssd1306(serial)

pi_parent_dir = os.path.dirname(os.path.abspath(__file__))

try:
    fontdir = os.path.join(pi_parent_dir, "fonts")
    font24 = ImageFont.truetype(os.path.join(fontdir, "Font.ttc"), 24)
    font16 = ImageFont.truetype(os.path.join(fontdir, "Font.ttc"), 16)
    font12 = ImageFont.truetype(os.path.join(fontdir, "Font.ttc"), 12)
except IOError:
    font24 = ImageFont.load_default()
    font16 = ImageFont.load_default()
    font12 = ImageFont.load_default()

look_r = "( ⚆_⚆)"
look_l = "(☉_☉ )"
look_r_happy = "( ◕‿◕)"
look_l_happy = "(◕‿◕ )"
sleep1 = "(⇀‿‿↼)"
sleep2 = "(≖‿‿≖)"
awake = "(◕‿‿◕)"
bored = "(-__-)"
intense = "(°▃▃°)"
cool = "(⌐■_■)"
happy = "(•‿‿•)"
excited = "(ᵔ◡◡ᵔ)"
grateful = "(^‿‿^)"
motivated = "(☼‿‿☼)"
demotivated = "(≖__≖)"
smart = "(✜‿‿✜)"
lonely = "(ب__ب)"
sad = "(╥☁╥ )"
angry = "(-_-')"
friend = "(♥‿‿♥)"
broken = "(☓‿‿☓)"
debug1 = "(#__#)"
upload = "(1__0)"
upload1 = "(1__1)"
upload2 = "(0__1)"
upload3 = "(0__0)"

def main():

    while True:
        GPIO.output(pinLED, GPIO.HIGH)
        print("LED on")
        time.sleep(1)  
        with canvas(device) as draw:
            draw.text((25, 5), intense, font=font24, fill=255)
            draw.text((30, 40), "Tomato", font=font16, fill=255)
        GPIO.output(pinLED, GPIO.LOW)
        print("LED off")
        time.sleep(1)       

if __name__ == "__main__":
    main()
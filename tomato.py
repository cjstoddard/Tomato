import logging
import RPi.GPIO as GPIO
import time
import os
import psutil
import math
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageFont

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# GPIO setup
LEDpin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDpin, GPIO.OUT)

# OLED setup
i2c_port = 1
OLED_address = 0x3c
serial = i2c(port=i2c_port, address=OLED_address)
device = ssd1306(serial)

# Paths
pi_parent_dir = os.path.dirname(os.path.abspath(__file__))
picdir = os.path.join(pi_parent_dir, "pics")

# Font setup
try:
    fontdir = os.path.join(pi_parent_dir, "fonts")
    font14 = ImageFont.truetype(os.path.join(fontdir, "Font.ttc"), 14)  # Smaller font size
except IOError:
    font14 = ImageFont.load_default()
    logging.warning("Custom fonts not found. Using default fonts.")

# Thresholds for CPU temperature, load, and memory
TEMP_THRESHOLD = 60.0  # Celsius
LOAD_THRESHOLD = 75.0  # Percentage
MEMORY_LOW = 25.0  # Below 25%: Low memory
MEMORY_HIGH = 75.0  # Above 75%: High memory

# Function to blink the LED a specific number of times and stay on
def blink_led(times):
    for _ in range(times):
        GPIO.output(LEDpin, GPIO.LOW)  # Turn LED off
        time.sleep(0.2)  # LED off for 0.2 seconds
        GPIO.output(LEDpin, GPIO.HIGH)  # Turn LED on
        time.sleep(0.2)  # LED on for 0.2 seconds
    GPIO.output(LEDpin, GPIO.HIGH)  # Ensure the LED stays on after blinking

# Function to display an image with additional text
def display_image_with_text(image_name, text, duration=2):
    face_path = os.path.join(picdir, image_name)
    if os.path.exists(face_path):
        face = Image.open(face_path)
        with canvas(device) as draw:
            # Draw image
            draw.bitmap((0, 0), face, fill=255)
            # Draw text slightly higher on the screen
            text_x = device.width - 80
            text_y = device.height - 20  # Moved up slightly
            draw.text((text_x, text_y), text, font=font14, fill=255)
        time.sleep(duration)
    else:
        logging.error(f"Image not found: {image_name}")

# Startup animation
def startup_animation():
    logging.info("Running startup animation.")
    display_image_with_text("AWAKE.png", "Boot", duration=2)
    display_image_with_text("LOOK_L_HAPPY.png", "Boot", duration=1)
    display_image_with_text("LOOK_R_HAPPY.png", "Boot", duration=1)
    logging.info("Startup animation complete.")

# Function to check and display CPU temperature
def display_cpu_temperature():
    try:
        # Blink LED once
        blink_led(1)
        
        # Call Looking Around function before checking CPU temp
        looking_around()

        # Get the CPU temperature
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp_file:
            cpu_temp = int(temp_file.read()) / 1000.0  # Convert to Celsius
            cpu_temp_rounded = math.floor(cpu_temp)  # Round down the temperature

        logging.info(f"CPU Temperature: {cpu_temp_rounded}°C")

        # Display image and temperature
        if cpu_temp > TEMP_THRESHOLD:
            display_image_with_text("ANGRY.png", f"Temp: {cpu_temp_rounded}°C", duration=2)
        else:
            display_image_with_text("COOL.png", f"Temp: {cpu_temp_rounded}°C", duration=2)

    except Exception as e:
        logging.error(f"Error checking CPU temperature: {e}")

# Function to check and display CPU load
def display_cpu_load():
    try:
        # Blink LED twice
        blink_led(2)

        # Call Looking Around function before checking CPU load
        looking_around()

        # Get CPU load percentage
        cpu_load = psutil.cpu_percent(interval=1)

        logging.info(f"CPU Load: {cpu_load:.2f}%")

        # Display image and load percentage
        if cpu_load > LOAD_THRESHOLD:
            display_image_with_text("INTENSE.png", f"Load: {cpu_load:.1f}%", duration=2)
        else:
            display_image_with_text("HAPPY.png", f"Load: {cpu_load:.1f}%", duration=2)

    except Exception as e:
        logging.error(f"Error checking CPU load: {e}")

# Function to check and display free memory
def display_free_memory():
    try:
        # Blink LED three times
        blink_led(3)

        # Call Looking Around function before checking free memory
        looking_around()

        # Get memory stats
        memory = psutil.virtual_memory()
        free_memory_percentage = (memory.available / memory.total) * 100

        logging.info(f"Free Memory: {free_memory_percentage:.2f}%")

        # Display image and memory percentage
        if free_memory_percentage < MEMORY_LOW:
            display_image_with_text("LONELY.png", f"Mem: {free_memory_percentage:.1f}%", duration=2)
        elif MEMORY_LOW <= free_memory_percentage <= MEMORY_HIGH:
            display_image_with_text("HAPPY.png", f"Mem: {free_memory_percentage:.1f}%", duration=2)
        else:
            display_image_with_text("EXCITED.png", f"Mem: {free_memory_percentage:.1f}%", duration=2)

    except Exception as e:
        logging.error(f"Error checking free memory: {e}")

# Function for the "Looking around" animation
def looking_around():
    logging.info("Looking around...")
    display_image_with_text("LOOK_L.png", "Looking", duration=2)
    display_image_with_text("LOOK_R.png", "Looking", duration=2)

# Main function
def main():
    GPIO.output(LEDpin, GPIO.HIGH)
    logging.info("Good morning. LED is ON.")

    # Run startup animation
    startup_animation()

    try:
        while True:
            # Call functions to display system status and then call "Looking around"
            display_cpu_temperature()
            time.sleep(30)  # Check every 30 seconds

            display_cpu_load()
            time.sleep(30)  # Check every 30 seconds

            display_free_memory()
            time.sleep(30)  # Check every 30 seconds

    except KeyboardInterrupt:
        logging.info("Good night. LED is OFF.")
        GPIO.output(LEDpin, GPIO.LOW)
        GPIO.cleanup()
        exit()

if __name__ == "__main__":
    main()

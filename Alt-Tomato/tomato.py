import logging
import pygame
import time
import psutil  # For system monitoring
import math  # For rounding down
import os

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pics")

# Screen dimensions
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# Thresholds for CPU temperature, load, and memory
TEMP_THRESHOLD = 60.0  # Celsius
LOAD_THRESHOLD = 75.0  # Percentage
MEMORY_LOW = 25.0  # Below 25%: Low memory
MEMORY_HIGH = 75.0  # Above 75%: High memory

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 100, 35)
YELLOW = (255, 255, 0)
GREEN = (50, 220, 0)
BLUE  = (20, 50, 200)
INDIGO = (35, 0, 100)
VIOLET = (50, 0, 70)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("System Monitor")
font_small = pygame.font.SysFont("monospace", 8)
font_large = pygame.font.SysFont("monospace", 14)

def draw_text(text, x, y, font, color=RED):
    """Utility function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def display_image(image_name, text):
    """Display an image with text in the graphical window."""
    image_path = os.path.join(IMAGE_DIR, image_name)
    try:
        # Load and scale the image
        image = pygame.image.load(image_path).convert_alpha()  # Use convert_alpha for transparency
        image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Display the image with a yellow background
        screen.fill(YELLOW)  # Set the background color to yellow (RGB)
        screen.blit(image, (0, 0))  # Draw the image on the screen
        
        # Draw the text at the lower right side of the screen with red color
        text_surface = font_large.render(text, True, RED)  # Red color (RGB) with larger font
        text_width, text_height = text_surface.get_size()
        text_x = SCREEN_WIDTH - text_width - 5  # 5px margin from the right
        text_y = SCREEN_HEIGHT - text_height - 5  # 5px margin from the bottom
        screen.blit(text_surface, (text_x, text_y))  # Draw the text
        pygame.display.flip()  # Update the display
        time.sleep(2)  # Pause for 2 seconds

    except pygame.error as e:
        logging.error(f"Error loading image '{image_path}': {e}")
        screen.fill((255, 255, 0))  # Ensure the screen is filled with yellow on error
        draw_text(f"Error: {image_name} not found!", 5, 5, font_small)
        pygame.display.flip()
        time.sleep(2)

def startup_animation():
    """Display the startup sequence."""
    logging.info("Running startup animation.")
    display_image("AWAKE.png", "Booting...")
    display_image("LOOK_L_HAPPY.png", " ")
    display_image("LOOK_R_HAPPY.png", " ")
    logging.info("Startup animation complete.")

def display_cpu_temperature():
    """Check and display CPU temperature."""
    try:
        # Get the CPU temperature
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp_file:
            cpu_temp = int(temp_file.read()) / 1000.0  # Convert to Celsius
            cpu_temp_rounded = math.floor(cpu_temp)  # Round down the temperature

        logging.info(f"CPU Temperature: {cpu_temp_rounded}°C")

        # Display image and temperature
        if cpu_temp > TEMP_THRESHOLD:
            display_image("ANGRY.png", f"Temp: {cpu_temp_rounded}°C")
        else:
            display_image("COOL.png", f"Temp: {cpu_temp_rounded}°C")

    except Exception as e:
        logging.error(f"Error checking CPU temperature: {e}")

def display_cpu_load():
    """Check and display CPU load."""
    try:
        # Get CPU load percentage
        cpu_load = psutil.cpu_percent(interval=1)

        logging.info(f"CPU Load: {cpu_load:.2f}%")

        # Display image and load percentage
        if cpu_load > LOAD_THRESHOLD:
            display_image("INTENSE.png", f"Load: {cpu_load:.1f}%")
        else:
            display_image("HAPPY.png", f"Load: {cpu_load:.1f}%")

    except Exception as e:
        logging.error(f"Error checking CPU load: {e}")

def display_free_memory():
    """Check and display free memory."""
    try:
        # Get memory stats
        memory = psutil.virtual_memory()
        free_memory_percentage = (memory.available / memory.total) * 100

        logging.info(f"Free Memory: {free_memory_percentage:.2f}%")

        # Display image and memory percentage
        if free_memory_percentage < MEMORY_LOW:
            display_image("LONELY.png", f"Mem: {free_memory_percentage:.1f}%")
        elif MEMORY_LOW <= free_memory_percentage <= MEMORY_HIGH:
            display_image("HAPPY.png", f"Mem: {free_memory_percentage:.1f}%")
        else:
            display_image("EXCITED.png", f"Mem: {free_memory_percentage:.1f}%")

    except Exception as e:
        logging.error(f"Error checking free memory: {e}")

def looking_around():
    """Display the 'Looking around' animation."""
    logging.info("Looking around...")
    display_image("LOOK_L.png", " ")
    display_image("LOOK_R.png", " ")

def main():
    """Main function."""
    logging.info("System Monitor Started.")

    # Run startup animation
    startup_animation()

    try:
        while True:
            # Call functions to display system status
            looking_around()
            display_cpu_temperature()
            time.sleep(30)  # Check every 30 seconds

            looking_around()
            display_cpu_load()
            time.sleep(30)  # Check every 30 seconds

            looking_around()
            display_free_memory()
            time.sleep(30)  # Check every 30 seconds

    except KeyboardInterrupt:
        logging.info("Exiting System Monitor.")
        pygame.quit()
        exit()

if __name__ == "__main__":
    main()

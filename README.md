# Tomato
Building a Radical Edward Computer

Here little program that displayes the face of Tomato, Radical Edwards computer from the Cowboy Bebop series, on an SSD 1306 OLED, The program checks CPU Temperature, CPU Load and Free Memory. The program is a system monitor that displays different faces depending on what it finds. I developed this on a Rasperry Pi 2 W Zero, but should work on any Rasperry Pi. This program is not a serious system monitor and  its main purpose is to give your Rasperry a Pi a bit of personality.

I got the Avatar Custom Faces for Tomato from [CyberSpaceManMike](https://cyberspacemanmike.com/product/radical-edwards-avatar-custom-faces-for-the-custom-faces-mod-and-radical-edward-pwnagotchi-cyberdeck/), the bundle is a free download. These images were designed for use with a Pwnagothi, but works well for this project. It was [his blog](https://cyberspacemanmike.com/2024/01/18/radical-edwards-pwnagotchi-cyberdeck/) post that inspired me to do this, so creative credit must be given to CyberSpaceManMike.

If you have never used an SSD 1306 with a Raspberry Pi, here is a good guide for setting one up.

https://robu.in/raspberry-pi-zero-2w-how-to-enable-i2c/

I used the same wiring used in this guide, so you should not need to make any changes if you followed it. Additionally, I have an LED attached attached to GPIO pin 21 with a 100 ohm resistor and ground. If you have never made an LED blink on a Rasperry PI, take a look at this [tutorial](https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/). Just keep in mind, tomato.py as is, uses GPIO pin 21 and if you followed that tutorial, you will have to change either the wiring of the pi to match the program or change the program to match the wiring.

Once you have the SSD 1306 and the LED are configured, you can download and run this project.

> sudo apt install -y python3-dev python3-smbus i2c-tools python3-pil python3-setuptools python3-venv libjpeg-dev zlib1g-dev python3-av libfreetype6-dev liblcms2-dev libopenjp2-7 git

> git clone https://github.com/cjstoddard/Tomato.git

> cd Tomato

> python3 -m venv venv

> source venv/bin/activate

> pip install --upgrade luma.oled psutil

> python3 tomato.py

There are two easy changes to the code you can make, first is the thresholds for the three things the program monitors. These numbers reflect my own comfort levels. Look for these lines in the code and change them to suit your needs.

> TEMP_THRESHOLD = 60.0  # Celsius
>
> LOAD_THRESHOLD = 75.0  # Percentage
>
> MEMORY_LOW = 25.0  # Below 25%: Low memory
>
> MEMORY_HIGH = 75.0  # Above 75%: High memory

Second, I have the program set to run each check 30 seconds apart in a loop. If you want to shorten this timing, look for these lines towards the bottom of the program under the  "def main():" function and change the time.sleep(30) to what you want it to be.

> display_cpu_temperature()
>
> time.sleep(30)  # Check every 30 seconds
>
> display_cpu_load()
>
> time.sleep(30)  # Check every 30 seconds
>
> display_free_memory()
>
> time.sleep(30)  # Check every 30 seconds

Once you are done testing Tomato and making sure it works, edit the tomato.sh file and change the path of this program for your environment. Then to run this program at startup, do the following;

> sudo cp tomato.sh /usr/local/bin/
>
> sudo chown root:root /usr/local/bin/tomato.sh
>
> sudo chmod +x /usr/local/bin/tomato.sh
>
> sudo crontab -e

and add this line to the file;

> @reboot /usr/local/bin/tomato.sh >&1

Save and exit the file and reboot the system, you should be good.

Ideas for the future:

It might be interesting to add some randomness to the program by adding a function that every so often displays a random face.

Setup a mood system based on the state of CPU Temp, CPU Load and Free Memory. Prehaps 1 (sad) - 10 (happy), and each time it checks CPU Temp, CPU Load and Free Memory, it adds a +1, 0 or -1 for each one to the mood rating, so the programs mood would change gradually over time depending on what was happening with the system.

Have the program search the running processes looking for common programs and display a specific face when it finds one of those programs running.

Add a list of comments to be displayed with the faces. Maybe have different word lists for different personality types.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

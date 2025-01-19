# Tomato
Building a Radical Edward Computer

Here is a useless little program that displayes the face of Tomato, Radical Edwards computer from the Cowboy Bebop series, on an SSD 1306 OLED, The program checks CPU Temperature, CPU Load and Free Memory and displays different faces depending on what it finds. I developed this on a Rasperry Pi 2 W Zero, but should work on any Rasperry Pi. This program does not serve much of a purpose beyond giving your Rasperry a Pi a bit of personality. If I get bored at some point, I may do a version for the Waveshare 2.13 e-ink hat.

I got the Avatar Custom Faces for Tomato from [CyberSpaceManMike](https://cyberspacemanmike.com/product/radical-edwards-avatar-custom-faces-for-the-custom-faces-mod-and-radical-edward-pwnagotchi-cyberdeck/), the bundle is a free download. These images were designed for use with a Pwnagothi, but works well for this project. It was [his blog](https://cyberspacemanmike.com/2024/01/18/radical-edwards-pwnagotchi-cyberdeck/) post that inspired me to do this, so creative credit must be given to CyberSapceManMike.


Start here for hooking up your OLED SSD 1306.

https://robu.in/raspberry-pi-zero-2w-how-to-enable-i2c/

> sudo apt install -y python3-dev python3-smbus i2c-tools python3-pil python3-setuptools python3-venv libjpeg-dev zlib1g-dev python3-av libfreetype6-dev liblcms2-dev libopenjp2-7 git

> git clone https://github.com/cjstoddard/Tomato.git

> cd Tomato

> python3 -m venv venv

> source venv/bin/activate

> pip install --upgrade luma.oled psutil

> python3 tomato.py

There are two easy changes to the code you can make is first the thresholds for the three things the program monitors. These numbers reflect my own comfort levels. Look for these lines in the code and change them to suit your needs.

> TEMP_THRESHOLD = 60.0  # Celsius
> LOAD_THRESHOLD = 75.0  # Percentage
> MEMORY_LOW = 25.0  # Below 25%: Low memory
> MEMORY_HIGH = 75.0  # Above 75%: High memory

Second, I have the program set to run each check 30 seconds apart in a loop. If you want to shorten this timing, look for these lines towards the bottom of the program under the  "def main():" function and change the time.sleep(30) to what you want it to be.

> display_cpu_temperature()
> time.sleep(30)  # Check every 30 seconds
>
> display_cpu_load()
> time.sleep(30)  # Check every 30 seconds
>
> display_free_memory()
> time.sleep(30)  # Check every 30 seconds

Once you are done testing Tomato and making sure it works, edit the tomato.sh file and change the path of this program for your environment. Then to run this program at startup, do the following;

> sudo cp tomato.sh /usr/local/bin/
> sudo chown root:root /usr/local/bin/tomato.sh
> sudo chmod +x /usr/local/bin/tomato.sh
> sudo crontab -e

and add this line to the file;

> @reboot /usr/local/bin/tomato.sh >&1

Save and exit the file and you should be good.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

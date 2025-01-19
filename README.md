# Tomato
Building a Radical Edward Computer

I got the Avatar Custom Faces for Tomato from [CyberSpaceManMike](https://cyberspacemanmike.com/product/radical-edwards-avatar-custom-faces-for-the-custom-faces-mod-and-radical-edward-pwnagotchi-cyberdeck/), the bundle is a free download. These images were designed for use with a Pwnagothi, but works well for this project.


Start here for hooking up your OLED SSD 1306.

https://robu.in/raspberry-pi-zero-2w-how-to-enable-i2c/

sudo apt install -y python3-dev python3-smbus i2c-tools python3-pil python3-setuptools python3-venv libjpeg-dev zlib1g-dev python3-av libfreetype6-dev liblcms2-dev libopenjp2-7 git

git clone https://github.com/cjstoddard/Tomato.git

cd Tomato

python3 -m venv venv

source venv/bin/activate

pip install --upgrade luma.oled

python3 tomato.py

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

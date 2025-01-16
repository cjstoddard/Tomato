# Tomato
Building a Radical Edward Computer

sudo apt install -y python3-dev python3-smbus i2c-tools python3-pil python3-setuptools python3-venv libjpeg-dev zlib1g-dev python3-av libfreetype6-dev liblcms2-dev libopenjp2-7 git

git clone https://github.com/cjstoddard/Tomato.git

cd Tomato

python3 -m venv venv

source venv/bin/activate

pip install --upgrade luma.oled

python3 tomato.py

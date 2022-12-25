# Waveshare UPS hat web Gui

## The story.

So, I bought a [waveshare ups hat (type A)](https://www.waveshare.com/wiki/UPS_HAT) for my raspberry pi, but the example code was a simple python I2C reader for the [ina219](https://www.ti.com/lit/gpn/ina219) chip. Inspired from pisgugar's 3 [web gui](https://github.com/PiSugar/PiSugar/wiki/PiSugar2) and build my own simpler interface that you can see in the screenshot bellow: 

<br>

<img width="509" alt="image" src="https://user-images.githubusercontent.com/106091011/209480409-c412165a-3581-4c5b-98da-97be07c0b300.png">

As you can see there is info about the battery voltage, current (if it's negative it means that the pi is taking power and if it's positive it means that the batteries are charging) , power and battery status. Also you can set the safe shutdown parameter (you can add a custom one by just adding a line in app/templates/index.html).

## Installing

To install the app just run these 3 commands your terminal:

```sh
git clone https://github.com/raspberrydeveloper/waveshare-upshat-gui.git
cd waveshare-upshat-gui
python3 -m pip install django
```

Then got to app/templates/index.html and update this line ```r.open("get", "http://100.88.54.69:1414/api/sv" + selectedValue.toString());``` with your raspberry pi ip address. For example if your ip address is 10.0.0.1 make this line look like this: ```r.open("get", "http://10.0.0.1:1414/api/sv" + selectedValue.toString());``` Note that this is a key component for the safe shutdown function to work.

## Running

To run cd into the waveshare-upshat-gui direcotry and run the following command:

```sh
sudo python3 manage.py runserver 127.0.0.1:1414
```

**Warning:** The script **requires** root privleges in order for the safe shutdown function to work, so make sure to use sudo.

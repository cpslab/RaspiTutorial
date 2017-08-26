# Sensing base and control programming
## About Sense Hat
The Sense Hat is an add-on board with various sensors and LEDs.
Sensors included in the Sense Hat are as follows.
- Gyroscope
- Accelerometer
- Magnetometer
- Temperature
- Barometric pressure
- Humidity

There is also a Python Library that gives easy access to everything on the board.

## About Python
Python is a dynamic typed programming language used in various applications. It is widely used in various fields such as machine learning, statistical analysis, sensor control.
Python has the following features.
- Easy to learn.
- Blocks are indicated by the number of indents.
- It is a dynamic typed language in which all integers and character strings are also as objects.
- Many libraries available for scientific computing and machine learning are prepared.
- The implementation of Python is available as an open source license that you can freely use, freely distribute, and can also use for commercial use.
etc.

## Python Tutorial
1. Open Python Shell
[Menu]→[Programming]→[Python3(IDLE)]
2. Write code  `print("Hello World!")` .

  ![shell](./image/shell.png)

## Let's light the LED
- Things to prepare
bread board, 50Ω Resistor, LED, Jumper wire
  1. Connect as shown.
  ![pin_asign](./image/gpio.png)
  ↑Raspberry Pi3's pin assignment.

    ※Bread board is the substrate used for prototyping, experimentation, evaluation. An electric signal flows in the direction of the arrow line in the following figure.

    This time connect to GPIO21 and GND.
  ![LED](./image/LED.png)

  2. Open Python3 IDLE [Menu]→[Programming]→[Python3(IDLE)]→[File]→[New File]

  3. Write the following code.

  ```
   1  import RPi.GPIO as GPIO #O isn't zero(0).
   2  import time
   3
   4  GPIO.cleanup()
   5  GPIO.setmode(GPIO.BCM)
   6  GPIO.setup(21, GPIO.OUT)
   7  while True:
   8    GPIO.output(21, GPIO.HIGH)
   9    time.sleep(1)
  10    GPIO.output(21, GPIO.LOW)
  11    time.sleep(1)
  ```
  4. [Run]→[Run Module] or push F5 key on keyboard.

    ※Warnings may be issued, but if the LEDs are blinking, you can ignore this time.

## Running The Sense Hat Emulator
1. Open Raspberry Pi Configuration
[Menu]→[Programming]→[Sense Hat Emulator]
![SHE](./image/SHE.png)
2. Open Sample Code. (about humidity.py)
[File]→[Open example]→[Simple]→[humidity.py]
![humidity](./image/humidity.png)
3. Run humidity.py
[Run]→[Run Module] or Press the F5 key.
![Run_module](./image/run_module.png)
4. Result screen
![SHE_result](./image/SHE_result.png)
By changing the value by raising or lowering the Humidity bar, how the LEDs shine also changes.

※If you want to run with the real Sense Hat, change `from sense_emu import SenseHat` on program to `from sense_hat import SenseHat`.
![real_SHE](./image/real_sense.JPG)

## Obtaining values of sensor data
As an example, let's get the value of the humidity sensor.
1. Open Python3 IDLE [Menu]→[Programming]→[Python3(IDLE)]→[File]→[New File]
2. Writing program. And run the program with [Run]→[Run Module].

  ```
   1  from sense_hat import SenseHat
   2  
   3  sense = SenseHat()
   4  humidity = sense.get_humidity()
   5  print("humidity: " humidity)
  ```

  ![humidity2](./image/humidity3.png)

3. Humidity value is displayed on Shell.

※Refer to Sense Hat official document for how to get the values of other sensors, so please see.

## about ThingSpeak
ThingSpeak is one of the IoT Platforms.
As a similar platform there are Kibana and Milkcocoa. These platforms can accumulate, analyze, and visualize data.

### Sign up ThingSpeak
1. Open sign up page from ThingSpeak's homepage.
<https://thingspeak.com/users/sign_up>
 ![sign_up](./image/Thingspeak.png)
2. Follow the instructions to create an account.

### Send sensor data to ThingSpeak.
1. Login to ThingSpeak.
2. Click to Channels on Menu tab. And push [New Channel] button.
 ![newchannel](./image/new_channel.png)
3. Open [API Keys] tab. And confirm API key.
 ![apikey](./image/apikey.png)
4. Open Python3 IDLE on raspberry pi and open [File] tab → [New file].
5. Write the following code. Insert the Write API Key confirmed above into the Write_API_KEY below.
  ```
   1  from sense_hat import SenseHat
   2  import urllib.parse
   3  import urllib.request
   4  import time
   5
   6  sleep = 7 #Send a value every 7 seconds
   7  key = "Write_API_KEY" #This White_API_KEY is your API Key
   8  sense = SenseHat()
   9  def send_data():
  10    while True:
  11      humidity = sense.get_humidity()
  12      params = urllib.parse.urlencode({'api_key': key, 'field1': humidity})
  13      url = 'https://api.thingspeak.com/update?' + params
  14      try:
  15        f = urllib.request.urlopen(url)
  16      except:
  17        print("connection failed")
  18      break
  19
  20  if __name__ == "__main__": #two "_"
  21    while True:
  22      send_data()
  23      time.sleep(sleep)
  ```
6. Set and save the file name.
7. [Run]　→　[Run Module] or push F5 key.
8. Confirm Private view on ThingSpeak.
 You can see that the current humidity is plotted.
 ![result](./image/result.png)

## Work
Let's try other sensor data obtained by Sense Hat.

### Raspberry pi's pin assignment
<https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/>
### Python tutorial
<https://docs.python.org/3.6/tutorial/index.html#the-python-tutorial>
### Sense Hat official document
<https://pythonhosted.org/sense-hat/api/#sense-hat-api-reference>
### ThingSpeak tutorial
<https://jp.mathworks.com/help/thingspeak/update-channel-feed.html>

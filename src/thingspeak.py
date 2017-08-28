from sense_hat import SenseHat
import urllib.parse
import urllib.request
import time

sleep = 15
key = "Write_API_KEY" 
sense = SenseHat()

def send_data():
    humidity = sense.get_humidity()
    params = urllib.parse.urlencode({'api_key': key, 'field1': humidity})
    url = 'https://api.thingspeak.com/update?' + params
    try:
        f = urllib.request.urlopen(url)
    except:
        print("connection failed")

if __name__ == '__main__':
    while True:
        send_data()
        time.sleep(sleep)

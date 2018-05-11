import RPi.GPIO as GPIO
from time import sleep
#import http.client
#import urllib.parse
import sys
import Adafruit_ADS1x15
from time import sleep


def get_dict_ranges():
        dict_values = {1 : range(18000, 19000),
                        2 : range(16000, 18000),
                        3 : range(15000, 16000),
                        4 : range(13000, 15000),
                        5 : range(12000, 13000),
                        6 : range(10000, 11000),
                        7 : range(9000, 10000),
                        8 : range(7000, 8000),
                        9 : range(6000, 7000) }

        return dict_values


def check_dict_values(data):

        range_dict = get_dict_ranges()
        for key,value in range_dict.items():
                if data in value:
                        return key


def get_key():

        adc = Adafruit_ADS1x15.ADS1115()
        GAIN = 1

        value = adc.read_adc(0, gain=GAIN)
        data = check_dict_values(value)
        if data is not None:
		return data


def send_to_server(data):
        try:
                params = urllib.parse.urlencode({'data' : data})
                headers = {'Content-type' : 'application/x-www-form-urlencoded',
                           'Accept' : 'text/plain'}
                conn = http.client.HTTPConnection('localhost')
                conn.request('POST', '/server_tpsi/index.php', params, headers)
                response = conn.getresponse()
                _response = response.read().decode('UTF-8')
                print _response
                return
        except Exception as msg:
		print str(msg)
        
        
def main():
	try:
		while True:
                	key = get_key()
                	if key is not None:
				print "e stato premuto il tasto : " + str(key)
			sleep(0.5)
                #print ('valore : ' + str(prev_input))
	except KeyboardInterrupt as msg:
		print "\nchiusura"

if __name__ == '__main__':
	main()
	










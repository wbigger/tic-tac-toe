#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
#import Adafruit_ADS1x15
import sys
#import ADS1x15
#import urllib.parse


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

   #FUNZIONE CERCHI
   # def zero():
#	return DrawCircle(canvas,6,6,3,blue)
 #   def one():
#	return DrawCircle(canvas,16,6,3,blue)
 #   def two():
#	return DrawCircle(canvas,26,6,3,blue)
 #   def three():
#	return DrawCircle(canvas,6,16,3,blue)
 #   def four():
#	return DrawCircle(canvas,16,16,3,blue)
 #   def five():
#	return DrawCircle(canvas,26,16,3,blue)
 #   def six():
#	return DrawCircle(canvas,6,26,3,blue)
 #   def seven():
#	return DrawCircle(canvas,16,26,3,blue)
 #   def eight():
#	return DrawCircle(canvas,26,26,3,blue)
 #   def numbers_to_positions(a):
#	switcher = {
#		0: zero,
#		1: one,
#		2: two,
#		3: three,
#		4: four,
#		5: five,
#		6: six,
#		7: seven,
#		8: eight
#	       }
#	func = switcher.get(a)
#	print func(a)


    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../.font.LoadFont("../../../fonts/7x13

        red = graphics.Color(180, 0, 0)
        green = graphics.Color(0, 180, 0)
        blue = graphics.Color(0, 0, 180)
	white = graphics.Color(180, 180, 180)

	#griglia
	graphics.DrawLine(canvas,11,2,11,30,white) 
        graphics.DrawLine(canvas,21,2,21,30,white)
        graphics.DrawLine(canvas,2,11,30,11,white)
        graphics.DrawLine(canvas,2,21,30,21,white)

	graphics.DrawLine(canvas,31,1,31,31,white)
	graphics.DrawLine(canvas,1,31,31,31,white)
	graphics.DrawLine(canvas,1,1,31,1,white)
	graphics.DrawLine(canvas,1,1,1,31,white)
	

	#o
	graphics.DrawCircle(canvas,6,16,3,blue)
	graphics.DrawCircle(canvas,26,26,3,blue)
	
	#x
	graphics.DrawLine(canvas,3,3,9,9,red)       
	graphics.DrawLine(canvas,9,3,3,9,red)

	graphics.DrawLine(canvas,13,3,19,9,red)
	graphics.DrawLine(canvas,13,9,19,3,red)

        time.sleep(60)   # show display for 10 seconds before exit

#def check_number(data):

def x_sign(n_sign, type_sign):
	graphicsTest = GraphicsTest()
	canvas = self.matrix
	font = graphics.Font()
	
	x_position = {
			0 : 


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


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
    main()


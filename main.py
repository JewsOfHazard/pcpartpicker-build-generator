import urllib.request
import json
from enum import Enum
import argparse

call_outline = "https://pcpartpicker.com/products/{0}/fetch/{1}&mode=list&xslug=&search="



def get_json_object(data):
	json_string = str(data[data.index(b'\"data\"')+7:data.index(b'\"html\"')-2])
	return json.dumps(json_string)

class WebcallType(Enum):
	memory = "memory"
	motherboard = "motherboard"
	graphics_card = "video-card"
	power_supply = "power-supply"
	case = "case"
	cpu = "cpu"

class GlobalUrlParameters(Enum):
	price = "X={0},{1}"
	rating = "R={}"

def get_json_from_url(url):
	with urllib.request.urlopen(url) as response:
		html = response.read()
	return get_json_object(html)

def build_url_options(options):
	options_list = "#"
	for index,option in enumerate(options):
		if index is not 0:
			options_list = options_list + "&" + option
		else:
			options_list = options_list + option

	return options_list


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Process price... Anything else?")
	parser.add_argument('-p', '--price', nargs=1, dest="price", type=int,
						help="This defines the price for your computer.",
						default=1000)

	args = parser.parse_args()
	print(args)
	#print(get_json_from_url(str(call_outline).format(WebcallType.graphics_card.value, build_url_options([GlobalUrlParameters.price.value.format(10*100, 300*100), GlobalUrlParameters.rating.value.format(3)]))))

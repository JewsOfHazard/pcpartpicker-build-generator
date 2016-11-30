import urllib.request
import json
from enum import Enum

call_outline = "https://pcpartpicker.com/products/{0}/fetch/{1}&mode=list&xslug=&search="

def get_json_object(data):
	jsonString = str(data[data.index(b'\"data\"')+7:data.index(b'\"html\"')-2])
	return json.dumps(jsonString)

class WebcallType(Enum):
	memory = "memory"
	motherboard = "motherboard"
	graphicsCard = "video-card"
	powerSupply = "power-supply"
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
	optionsList = "#"
	for index,option in enumerate(options):
		if index is not 0:
			optionsList = optionsList + "&" + option
		else:
			optionsList = optionsList + option

	return optionsList


if __name__ == "__main__":
	print(get_json_from_url(str(call_outline).format(WebcallType.graphicsCard.value, build_url_options([GlobalUrlParameters.price.value.format(10*100, 300*100), GlobalUrlParameters.rating.value.format(3)]))))

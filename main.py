import urllib.request
import json
from enum import Enum

callOutline = "https://pcpartpicker.com/products/{0}/fetch/{1}&mode=list&xslug=&search="

def getJsonObject(data):
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

def getJsonFromUrl(url):
	with urllib.request.urlopen(url) as response:
		html = response.read()
	return getJsonObject(html)

def buildUrlOptions(options):
	optionsList = "#"
	for index,option in enumerate(options):
		if index is not 0:
			optionsList = optionsList + "&" + option
		else:
			optionsList = optionsList + option

	return optionsList


if __name__ == "__main__":
	print(getJsonFromUrl(str(callOutline).format(WebcallType.graphicsCard.value, buildUrlOptions([GlobalUrlParameters.price.value.format(10*100, 300*100), GlobalUrlParameters.rating.value.format(3)]))))

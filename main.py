import urllib.request
import json




def getJsonObject(data):
	jsonString = str(data[data.index(b'\"data\"')+7:data.index(b'\"html\"')-2])
	return json.dumps(jsonString)
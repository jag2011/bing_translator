import urllib2, urllib, json, sys

languageCodes = ["de","fr","es","it","ru","ja","pl","pt"]
bingClientID = "" # YOUR CLIENT ID
bingClientSecret = "" # YOUR CLIENT SECRET

# -------------------------------------

apiTokenUrl = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"
apiUrl = "http://api.microsofttranslator.com/V2/HTTP.svc/"

bingScope = "http://api.microsofttranslator.com"
bingGrantType = "client_credentials"

def request_access_token():	
	req = urllib2.Request(apiTokenUrl)
	tokenRequestParams = {
		'client_id' : bingClientID,
		'client_secret' : bingClientSecret,
		'scope' : bingScope,
		'grant_type' : bingGrantType
	}
	req.add_data(urllib.urlencode(tokenRequestParams))
	result = urllib2.urlopen(req);
	data = result.read()
	jsonData = json.loads(data)
	accessToken = jsonData["access_token"];
	return accessToken

def translate(text,fromLang,to,access_token):
	requestParams = {		
		"text" : text,
		"from" : fromLang,
		"to" : to,
		"contentType" : "text/html"
	}
	req = urllib2.Request(apiUrl + 'Translate?' + urllib.urlencode(requestParams))
	req.add_header('Authorization','Bearer ' + access_token)
	result = urllib2.urlopen(req);
	data = result.read()	
	data = data[data.index(">")+1:-9] #remove xml shit
	return data;

if (len(sys.argv) != 2):
	print "Error: Specify File"
	sys.exit(0)

f = open(sys.argv[1])
source = f.read()
f.close()

# to preseve line breaks
source = source.replace('\n','<br>')

access_token = request_access_token()

for lang in languageCodes:
	translated = translate(source,"en",lang,access_token)

	# dont know why we get them back urlencoded
	translated = translated.replace('&lt;br&gt;','\n')
	print(translated)

	f = open("output_"+lang+".txt", "w")    
	f.write(translated)
	f.close()

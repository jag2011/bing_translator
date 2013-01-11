Bing Translator
===============

Translates text files quick and easy using Bing Translate Api. Useful for translating iOS App descriptions into lots of languages.


###Preparation:

1. Get a Bing Translate API Account
2. Open **bing.py**, fill in `bingClientID` and `bingClientSecret` on top of the file.
3. You may also want to adjust desired output languages in `languageCodes`

###Usage:


`python bing.py sourcefile`

**IMPORTANT: Sourcefile needs to be English**

###Output:

Files will be created for each specified language in `languageCodes`, e.g.:

	output_de.txt
	output_es.txt
	output_fr.txt
	...	




 

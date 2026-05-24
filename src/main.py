import re
import json

inputText = '../input/raw-text.txt'
outputFile = '../output/sample-output.json'

result={}

def extractEmails(input):
     # This regex searches for emails by looking for texts that follows the pattern
     # characters@characters.characters and possibly more .characters endings
     matches = re.findall('[a-zA-z0-9+._%]+@[a-zA-z-+%]+\.[a-z.]{2,}',input)
     result['emails:']=matches


def extractCreditCardNr(input):
     # The regex uses the common format of credit card numbers to look for input that follows the pattern of 
     # 3-4 groups of four digits minimum  each separated by space or hyphen
     matches = re.findall('[0-9]{4,}[- ]?[0-9]{4,}[- ]?[0-9]{4,}[- ]?[0-9]{4,}?',input);
     result['Credit card numbers:']=matches


def extractUrls(input):
     # This regex looks for text that starts with http/https, forward slashes and atleast two more sections
     # separated by literal dots
     matches = re.findall('(http[s]?:\/\/[a-z]+\.[a-z]+\.[a-z09-]+[\S]*)',input);
     result['urls:']=matches


def extractHashtags(input):
     # This regex extracts hashtags by looking for inputs that start with # followed by at least one more character
     matches = re.findall('#[A-Za-z0-9]+',input);
     result['hashtags:']=matches


def extractOfficialEmail(input):
     # This regex searches for alu official emails by looking for emals with @alueducation\.com
     matches = re.findall('[a-zA-z0-9\.]+@alueducation\.com',input)
     result['ALU official emails:']=matches

     
def extractAlumniEmail(input):
     # This regex searches for alu alumni emails by looking for emals with @alumni.alueducation\.com
     matches = re.findall('[a-zA-z0-9\.]+@alumni\.alueducation\.com',input)
     result['ALU Alumni emails:']=matches


def extractSiEmail(input):
     # This regex searches for alu si emails by looking for emals with @si.alueducation\.com
     matches = re.findall('[a-zA-z0-9\.]+@si\.alueducation\.com',input)
     result['ALU Si emails:']=matches


with  open(inputText,'r') as file:
    content = file.read() 
    extractEmails(content)
    extractCreditCardNr(content)
    extractHashtags(content)
    extractUrls(content)
    extractOfficialEmail(content)
    extractAlumniEmail(content)
    extractSiEmail(content)

with open(outputFile,'w') as file:
     json.dump(result,file,indent=4)

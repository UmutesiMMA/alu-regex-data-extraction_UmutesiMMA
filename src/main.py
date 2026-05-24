import re
import json

inputText = '../input/raw-text.txt'
outputFile = '../output/sample-output.json'

result={}

def extractEmails(input):
     matches = re.findall('[a-zA-z0-9+._%]+@[a-zA-z-+%]+\.[a-z.]{2,}',input)
     result['emails:']=matches


def extractCreditCardNr(input):
     matches = re.findall('[0-9]{4,}[- ]?[0-9]{4,}[- ]?[0-9]{4,}[- ]?[0-9]{4,}?',input);
     result['Credit card numbers:']=matches


def extractUrls(input):
     matches = re.findall('(http[s]?:\/\/[a-z]+\.[a-z]+\.[a-z09-]+[\S]*)',input);
     result['urls:']=matches


def extractHashtags(input):
     matches = re.findall('#[A-Za-z0-9]+',input);
     result['hashtags:']=matches


def extractOfficialEmail(input):
     matches = re.findall('[a-zA-z0-9\.]+@alueducation\.com',input)
     result['ALU official emails:']=matches

     
def extractAlumniEmail(input):
     matches = re.findall('[a-zA-z0-9\.]+@alumni\.alueducation\.com',input)
     result['ALU Alumni emails:']=matches


def extractSiEmail(input):
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

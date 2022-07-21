from subprocess import check_output
import json
import requests
import sys

target = sys.argv[1]

a = check_output("who "+target,shell=True).decode()
a.strip()
a = a.replace('\n', '').replace('\r', '').replace('	','').replace(' ','')

ch='{'
listOfWords = a.split(ch, 1)
if len(a) > 0: 
    b = listOfWords[1]
b = "{" + b
#print(b)
j = json.loads(b)
print(j['registrar'])


a = check_output("dig +noall +answer "+target,shell=True).decode()
aa = a.split('\n')
bb = aa[0].split('\t')
ip = bb[-1].strip()
print(ip)

url = "http://ip-info.monster/"+ip+"/asn"
response = requests.get(url)
actualPayload = response.text
print(actualPayload)
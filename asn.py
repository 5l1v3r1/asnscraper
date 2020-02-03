import requests
from bs4 import BeautifulSoup
import subprocess, sys, re
import os

    
url_base = 'http://ipinfo.io/'
as_base = 'AS'

output = open('ranges.txt', 'w')
with open('asns.txt') as f:
    lines = f.read().splitlines()
    for asn in lines:
        ASN = as_base + asn
        page = requests.get(url_base+ASN)
        html_doc = page.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        for link in soup.find_all('a'):
            if asn in link.get('href'):
                auxstring = '/'+as_base+asn+'/'
                line = re.sub(auxstring, '', link.get('href'))
                printstring = line+'\n'
                if 'AS' not in printstring:
                    output.write(printstring)
        print(as_base+asn+'\n')
        os.system("cat ranges.txt | grep -v h >> ranges.lst") 
        os.system("rm -rf ranges.txt") 
        os.system("touch ranges.txt") 
print ('All results has been saved to: ranges.lst')
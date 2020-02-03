import requests
from bs4 import BeautifulSoup
import subprocess, sys, re
import os, time

if len(sys.argv) < 2:
    sys.exit("\033[91mUsage: python3 "+sys.argv[0]+" [asn list]\033[0m")
    
url_base = 'http://ipinfo.io/'
as_base = 'AS'

print("\033[94mASN Scraper Has Been Started. Developed By UN5T48L3\033[0m")
time.sleep(1);
print("")
print("\033[93mPlease wait... This will take less than a minute.\033[0m") 
print("")
time.sleep(1);

output = open('ranges.txt', 'w')
with open(sys.argv[1], "r") as f:
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
print ("\033[95mAll results has been saved to: \033[92mranges.lst\033[0m")
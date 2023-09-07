import sys
from colorama import Fore, init
import scapy.all
from scapy.all import * #sr1,IP,ICMP
import os
import subprocess
import re
import json
init()
'''
themes - temas
BrightTheme()
RastaTheme()
ColorOnBlackTheme()
BlackAndWhite()
HTMLTheme() mustra el contenido con etiquetas HTML
LatexTheme()
'''

conf.color_theme = RastaTheme()
def detector_iface():
	ip_description = subprocess.getoutput('ipconfig /all')
	desc = ip_description.split(':')
	lista_desc = list()
	for iface in desc:
		sep = iface.split('\n')
		if len(sep)==1:
			lista_desc.append(sep)
		else:
			sep0,sep1=sep[0],sep[1]
			lista_desc.append(sep0)
			lista_desc.append(sep1)
	indexes = []
	realItem = str()
	word = 'Descrip'
	for item in lista_desc:	
		if re.search(word, str(item)):
			index = lista_desc.index(str(item))
			realItem=str(item)
	for x in range(len(lista_desc)):
		if lista_desc[x]==realItem:
			indexes.append(x)
	print(Fore.GREEN,'IFACE: ',lista_desc[indexes[-1]+1])
	return lista_desc[indexes[-1]+1]
iface = detector_iface().strip()

package = sr1(IP(dst='192.168.1.56'))
#package.show()
#package = sniff(iface=iface,count=2,prn=lambda x:x.show()) prn=lambda x:x.summary(), # muestra los paquetes en tiempo real detalladamente
#package = sniff(iface=iface,count=2,prn=lambda x:x.summary()) # muestra los pacquetes en tiempo real
package = sniff(iface=iface, filter="host 192.168.1.56", count=10)

c = 1
arr = []
for packet in package:
    p = {
        'idx': c,
        'src': packet[IP].src,
        'dst': packet[IP].dst
    }
    if not isinstance(packet[TCP].payload, scapy.packet.NoPayload):
        payload = json.loads(bytes(packet[TCP].payload).decode('utf-8'))
        p.update(payload)
        p['_data'] = base64.b64decode(payload['data']).decode('utf-8')
        p.__delitem__('data')
    arr.append(p)
    c += 1
print(arr)
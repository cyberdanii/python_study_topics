import requests
import json
import io
from scapy.all import *
import pyshark


url = "https://api.tidex.com/api/3/ticker/eth_btc"
respuesta = requests.get(url)
result = json.loads(respuesta.content)
cont_response = respuesta.headers

#for a,b in cont_response.items():
#	print(a,b)


pkts = pyshark.LiveCapture(interface='1x1 11bgn Wireless LAN PCI Express Half Mini Card Adapter',
 bpf_filter='host 192.168.1.11')
pkts.sniff(packet_count=10)

lenp=len(pkts)
for i in range(lenp):
	pkts[i].tcp.data
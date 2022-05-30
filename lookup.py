import requests
import sys

def check():
    req = requests.get("https://ipqualityscore.com/api/json/ip/KEY/" + ip) # Replace "KEY" with your own ipqualityscore.com api key.
    return req.json()
    
def lookup(ip):
    global result
    vpn = check()
    req = requests.get("http://ip-api.com/json/{0}".format(ip)).json()
  
    if req["status"] == "success":  
        result = '''
-----------------------------
| IP:      {0} 
|  
| Address: {1}, {2} ({3}) 
|
| Region:  {4}                        
| T-zone:  {6}                
| Coords:                     
|     LAT:  {7}               
|     LON:  {8}  
|
| ISP:     {9}                
| ORG:     {10}
| ASN:     {16}
| 
| Vpn:     {11}  Active: {14}
| Proxy:   {12}  
| Tor:     {13}  Active: {15}      
|
-----------------------------'''
        
    try: 
        result = result.format(req['query'], req['city'], req['country'], req['countryCode'], req['region'],
        req['zip'], req['timezone'], req['lat'], req['lon'], req['isp'], req['org'],
        vpn['vpn'], vpn['proxy'], vpn['tor'], vpn['active_vpn'], vpn['active_tor'], req['as'])
        
    except: result = " \_> That IP is not valid!"

    print(result)

    ip = input("\n\_> Do you want to look up another ip? ")
    if ip == "exit":
        exit()
    lookup(ip)

if __name__ == "__main__":
	ip = sys.argv[1] if len(sys.argv) > 1 else str(input("\_> Please enter the IP: "))
	lookup(ip)

import urllib.request
import json

url = "https://coinswitch.co/proxy/in/api/v1/fixed/top-coins-rate"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 ''Safari/537.17 '}
request = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(request)
source = resp.read()
data = json.loads(source)
print(str(data['data'][15]['buy_rate']))

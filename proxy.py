import random
import requests
from lxml import etree
# 在免费网址上获取的ip地址有，有2类：http、https
https_ip = ['180.173.70.40:9797', '117.80.147.48:808']
http_ip = ['125.46.0.62:53281', '101.68.73.54:53281']
hs = random.choice(https_ip)
hp = random.choice(http_ip)
# 因为不知道是http还是https开头，所以都设置一个地址
proxy_ip ={
    'https':hs,
    'http':hp,
}
url = 'http://ip.filefab.com/index.php' # 一个可以查看ip地址的网站
response = requests.get(url, proxies = proxy_ip)

html = etree.HTML(response.text)

ip = html.xpath('//h1[@id="ipd"]/span/text()') # 用xpath获取ip地址
print(ip)
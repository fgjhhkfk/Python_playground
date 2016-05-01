addy = 'http://www.finanzen.net/index/DAX/Dividenden@intpagenr_1'



from lxml import html
import requests
import urllib


page = requests.get(addy)
tree = html.fromstring(page.content)
html.tostring(tree)
#print type(tree)

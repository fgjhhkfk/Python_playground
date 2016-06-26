import urllib
import urllib2
import re

  
def Connect2Web(adr, idx):
    try:  
        aResp = urllib2.urlopen(adr);
        web_pg = aResp.read();

        pattern = "Joghurt"
        m = re.search(pattern, web_pg)
        if m:
            print adr
        else:
            print str(idx) + ": Nothing found"
    except:
        pass
##adr = "https://marleyspoon.de/menu/4746"    
for i in range(4700, 4800, 1):
    adr = "https://marleyspoon.de/menu/" + str(i);
    Connect2Web(adr, i)

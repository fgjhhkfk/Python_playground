import charcount as cc


dEng = cc.chardistribution(cc.readfile('english.txt'))
dGer = cc.chardistribution(cc.readfile('german.txt'))
dEsp = cc.chardistribution(cc.readfile('spanish.txt'))
dFra = cc.chardistribution(cc.readfile('french.txt'))
Languages = [dEng, dGer, dEsp, dFra]

##dCheck = cc.chardistribution(cc.readfile('nyt.txt'))
##dCheck = cc.chardistribution(cc.readfile('zeit.txt'))
##dCheck = cc.chardistribution(cc.readfile('elpais.txt'))
##dCheck = cc.chardistribution(cc.readfile('lemonde.txt'))
dCheck = cc.chardistribution(cc.readfile('repubblica.txt'))

##delta = {key: [Language for Language in Languages][key] - dCheck[key] for key in dCheck.keys()}
for refLang in Languages:
    delta = {key: refLang[key] - dCheck[key] for key in dCheck.keys()}

    print sum([abs(val) for val in delta.values()])

import charcount as cc

#%% 
dEng = cc.chardistribution(cc.readfile('/home/hjk/Documents/english.txt').lower())
dGer = cc.chardistribution(cc.readfile('/home/hjk/Documents/german.txt').lower())
dEsp = cc.chardistribution(cc.readfile('/home/hjk/Documents/spanish.txt').lower())
dFra = cc.chardistribution(cc.readfile('/home/hjk/Documents/french.txt').lower())
Languages = {'Eng':dEng, 'Ger':dGer, 'Esp':dEsp, 'Fra':dFra}
#%%
#dCheck = cc.chardistribution(cc.readfile('/home/hjk/Documents/nyt.txt').lower())
#dCheck = cc.chardistribution(cc.readfile('/home/hjk/Documents/zeit.txt').lower())
#dCheck = cc.chardistribution(cc.readfile('/home/hjk/Documents/elpais.txt').lower())
#dCheck = cc.chardistribution(cc.readfile('/home/hjk/Documents/lemonde.txt').lower())
dCheck = cc.chardistribution(cc.readfile('/home/hjk/Documents/repubblica.txt').lower())

##delta = {key: [Language for Language in Languages][key] - dCheck[key] for key in dCheck.keys()}
print 'Je kleiner der Wert, desto wahrscheinlicher entspricht der untersuchte Text der Sprache.'
for refLang in Languages.keys():
    delta = {key: Languages[refLang][key] - dCheck[key] for key in dCheck.keys()}
    #print dCheck.keys()
    print refLang + ': ' + str(sum([abs(val) for val in delta.values()]))

def charcount(text, char):
    count = 0
    for c in text:
        if c == char:
            count +=1
    return count

def readfile(filename):
    with open(filename) as f:
        text = f.read()
    return text

def chardistribution(text):
    dctnry = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        c = charcount(text, char)
        perc = 100.0*c/len(text)
##        print("{0} - {1}% - {2}".format(char, round(perc, 2), c))
        dctnry[char] = round(perc, 2)
    return dctnry


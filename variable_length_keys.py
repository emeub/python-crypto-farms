# Assignment 1
# Program written by E. Eubanks.

message = 'c fwvvroh xhtvkrp rh wjh edgvcu elrkgu ylno prv pcng wjh ehcvgu elrkgu cq0 vgfwug rpfg wjh cwvdengu hlpg qxv ddrww vkg qgz elrkgu wvkqi ugyguuh gqilphgukqi dpg eu0svdpdn1ulu'
key = 2
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz0123456789'
i = 2
# store encrypted/decyprted message
translated = ''

for charItem in message:
    if charItem in SYMBOLS:
        symbolIndex = SYMBOLS.find(charItem)
        if i % 2:
            translatedIndex = symbolIndex - (key+1)
        else:
            translatedIndex = symbolIndex - key
        translated = translated + SYMBOLS[translatedIndex]
        i += 1
    else:
        # if space then just append
        translated = translated + charItem

# output the translated string:
print(translated)
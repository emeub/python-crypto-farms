# Caesar Cipher
# from class on 09/11
# this code is from Al Seigward's "Cracking Codes with Python"
# https://nostarch.com/crackingcodes

# store string to be encrypted/decrypted
message = 'usw!s9 u07zw9 0! s @.7w 6x s !#t!@0@#@065 u07zw9 69 4656s37zstw@0u u07zw9 %zw9w w$w9. 3w@@w9 05 @zw 4w!!syw 0! 9w73suwv t.!64w 6@zw9 3w@@w9 x0/wv 5#4tw9 6x 76!0@065! v6%5 @zw s37zstw@r @zw 5#4tw9 6x !z0x@ 76!0@065! 0! @zw 2w.r'

# encryption/decryption Key
key = 18

# set program mode
mode = 'decrypt' # set mode to encrypt or decrypt

# store all possible symbols
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%/.'

# store encrypted/decyprted message
translated = ''

for symbol in message:
    # note: only symbols in the SYMBOLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # perform encryption or decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # append the symbol wihout encrypting/decrypting:
        translated = translated + symbol

# output the translated string:
print(translated)
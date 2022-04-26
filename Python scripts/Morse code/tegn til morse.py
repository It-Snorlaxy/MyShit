#morseCode er et dictonary vi refere til for at oversætte begge veje
morseCode = {
"A":".-",
"B":"-...",
"C":"-.-.",
"E":".",
"F":"..-.",
"G":"--.",
"H":"....",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--..",
"Æ":".-.-",
"Ø":"---.",
"Å":".--.-",
"1":".----",
"2":"..---",
"3":"...--",
"4":"....-",
"5":".....",
"6":"-....",
"7":"--...",
"8":"---..",
"9":"----.",
"0":"-----",
" ":" "}

letter=input(str("letter? "))
code=morseCode

#oversætter et bogstav
def translate(letter,code):
    if str(letter) in code:
        return code[letter]
    else:
        return "?"

#oversætter fra bogstaver
def encodeMessage(message,code):
    oversat=""
    for b in message:
        oversat=oversat+translate(b,code)+"/"
    return oversat

def reverse(aDict):
    reversed={}
    for key in aDict.keys():
        reversed[aDict[key]]=key
    return reversed

#oversætter fra morse
def decodeMessage(message, code):
    msg=message.split('/')
    oversat=''
    for m in msg:
        oversat=oversat+translate(m,code)
    return oversat

print(translate(letter, morseCode))



#nice!

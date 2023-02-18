keyEserom =  {"A":"10","B":"0111","C":"0101","D":"011",
        "E":"1", "F":"1101", "G":"001","H":"1111",
        "I":"11", "J":"1000", "K":"01", "L":"1011",
        "M":"00", "N":"01", "O":"000", "P":"1001",
        "Q":"0010", "R":"101", "S":"111", "T": "0",
        "U":"110", "V":"1110", "W":"100", "X":"0110",
        "Y":"0100", "Z":"0011",
        "1":"10000", "2":"11000", "3":"11100", "4":"11110",
        "5":"11111", "6":"01111", "7":"00111", "8":"00011",
        "9":"00001","0":"00000", " ":"  ", "":" "}

invKeyEserom = {val:key for key, val in keyEserom.items()}

def EseromDecode(msg):
    words = msg.split("  ") #split words
    out = []
    for word in words: #decode each word
        wordOut = []
        wordOut += [invKeyEserom[char] for char in word.split(" ")] #char translation
        
        out.append(''.join(wordOut))# join decoded characters and append to out as a word

    return ' '.join(out) # join words as a string

if __name__ == "__main__":
    inputMSG = input("Enter the phrase to be decoded: \n")
    print(EseromDecode(inputMSG))
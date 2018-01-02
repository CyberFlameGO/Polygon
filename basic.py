from sys import *

def open_file(filename):
    data = open(filename, "r").read()
    return data

#some general usage for debugging
def lex(data):
    data = list(data)
    sate = 0
    string = ""#yeah kinda fucking useless
    for char in data:
        tok += char #yeah this looks a little bit stupid in the print
        if tok == " ":
            if state == 0:
                tok = ""
                else:
                    tok = " "
            elif tok == "PRINT" or tok == "print":
                tokens.appand("PRINT")
                tok = ""
            elif tok = "\n": #useless cunt
                tok = ""
            elif tok == "\"":
                if state == 0:
                    state = 1
                elif state == 1:
                    print("FOUND: " + string)
                    tokens.appand("STRING: " + string)
                    string = ""
                    state = 0
            elif state == 1:
                string += tok 
                tok = ""
            print(tokens)

#idk if this will be used but fuck it
def parse(toks):
    i = 0
    while(i < len(toks)):
        print(i)#debug
        print(tok[i] + toks[i + 1])#more debug
        if toks[i] + " " + toks[i + 1][0:len(toks)] == "STRING":#shitty logic but really fuck it
            print("FOUND STR")
            print(toks[i + 1][6:])
            i+=2

def run():
    data =open_file(arg[1])
    toks = lex(data)
run()
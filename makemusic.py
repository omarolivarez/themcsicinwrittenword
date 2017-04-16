import pysynth as ps
import time
import random

def main():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    # create a header
    print("WELCOME TO ______")
    # delay the next screen
    time.sleep(.5)
    print()
    print()
    print("POEM'S LIST:")
    print("1. The Cat in the Hat")
    print("2. Project For a Fainting")
    print("3. Because I Could Not Stop for Death")
    print("4. One Art")
    print("5. Wedding")
    print("6. Rain")
    print("7. Speaking in Tongues")
    print("8. And Utpictura Poeses is Her Name")
    print("9. Dry Salvages")
    print("10. Directive")
    print("11. The Idea of Order at Key West")
    print("12. Green Eggs and Ham")
    print()
    # get the user input for the text they want to convert to music
    userinput = int(input("Which poem would you like to convert to music? " ))
    print("")
    # map the user input to certain text files
    if userinput == 1:
        text = open("./the_cat_in_the_hat.txt", 'r')
    elif userinput ==2:
        text = open("./projectforafainting.txt", 'r')
    elif userinput ==3:
        text = open("./becauseicouldnotstopfordeath.txt", 'r')
    elif userinput ==4:
        text = open("./oneart.txt", 'r')
    elif userinput ==5:
        text = open("./wedding.txt", 'r')
    elif userinput ==6:
        text = open("./rain.txt", 'r')
    elif userinput ==7:
        text = open("./speakingtongues.txt", 'r')
    elif userinput ==8:
        text = open("./andutpicturapoesisishername.txt", 'r')
    elif userinput ==9:
        text = open("./dry salvages.txt", 'r')
    elif userinput ==10:
        text = open("./directive.txt", 'r')
    elif userinput ==11:
        text = open("./theideaoforderatkeywest.txt", 'r')
    elif userinput ==12:
        text = open("./greeneggsandham.txt", 'r')
    else:
        print("You entered the wrong value.")
    allwords = list()
    for line in text:
        line = line.split()
        for word in line:
            newword = checkword(word)
            allwords.append(newword)
    uniquewords = set(allwords)
    #for word in uniquewords:
        #print(word)
    mapdict = {}
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    for word in uniquewords:
        random.shuffle(notes)
        mapdict[word] = notes[0]
    if userinput == 1:
        text2 = open("./the_cat_in_the_hat.txt", 'r')
    elif userinput ==2:
        text2 = open("./projectforafainting.txt", 'r')
    elif userinput ==3:
        text2 = open("./becauseicouldnotstopfordeath.txt", 'r')
    elif userinput ==4:
        text2 = open("./oneart.txt", 'r')
    elif userinput ==5:
        text2 = open("./wedding.txt", 'r')
    elif userinput ==6:
        text2 = open("./rain.txt", 'r')
    elif userinput ==7:
        text2 = open("./speakingtongues.txt", 'r')
    elif userinput ==8:
        text2 = open("./andutpicturapoesisishername.txt", 'r')
    elif userinput ==9:
        text2 = open("./dry salvages.txt", 'r')
    elif userinput ==10:
        text2 = open("./directive.txt", 'r')
    elif userinput ==11:
        text2 = open("./theideaoforderatkeywest.txt", 'r')
    elif userinput ==12:
        text2 = open("./greeneggsandham.txt", 'r')   
    else:
        print("You entered the wrong value.") 
    test = []    
    for line in text2:
        line = line.split()
        for word in line:
            word = word.lower()
            testaddition = []
            notetoadd = ""
            count = 0
            if "!" in word or "." in word or "," in word or "?" in word or ";" in word or "(" in word or ")" in word or ":" in word or '''"''' in word or "-" in word or "_" in word:
                count += 1
            if count != 0:
                letterlist = []
                for letter in word:
                    if letter not in ["!", ".", ",", "?", ";", ")", "(", ":", '''"''', "-", "_"]:
                        letterlist.append(letter)
                newword = ""
                for letter in letterlist:
                    newword+= letter
                if newword =='':
                    continue
                notetoadd = mapdict[newword]
                testaddition.append(notetoadd)
                testaddition.append(8)
                testaddition = tuple(testaddition)
                test.append(testaddition)
                restaddition = ('r', 4)
                test.append(restaddition)
            else:
                newword = word
                print(newword)
                notetoadd = mapdict[newword]
                testaddition.append(notetoadd)
                testaddition.append(8)
                testaddition = tuple(testaddition)
                test.append(testaddition)
    test = tuple(test)
    songname = ""
    if userinput == 1:
        songname = "catinthehat"
    elif userinput ==2:
        songname = "projectforafainting"
    elif userinput == 3:
        songname = "becauseicouldnotstopfordeath"
    elif userinput ==4:
        songname = "oneart"
    elif userinput ==5:
        songname = "wedding"
    elif userinput ==6:
        songname = "rain"
    elif userinput ==7:
        songname = "speakingintongues"
    elif userinput ==8:
        songname = "andutpicturapoesisishername"
    elif userinput ==9:
        songname = "drysalvages"
    elif userinput ==10:
        songname = "directive"
    elif userinput ==11:
        songname = "theideaoforderatkeywest"
    elif userinput ==12:
        songname = "greeneggsandham"
    # complete the music file name            
    songname += ".wav"
    # make the wav file
    ps.make_wav(test, fn = songname)
    text.close()   
    text2.close()   
                        
    
def checkword(word):
    word = word.lower()
    alphanumlist = ["'", "1",'2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letterlist = []
    for letter in word:
        letterlist.append(letter)
    for letter in letterlist:
        if letter not in alphanumlist:
            letterlist.remove(letter)
    newword = ""
    for letter in letterlist:
        newword += letter
    return newword
    ''''
    # make the contents of the wav files
    test = (('c', 4), ('e', 4), ('g', 4),
    		('c5', -2), ('e6', 8), ('d#6', 2))'''
    # make the variable for the name of the wav file


main()

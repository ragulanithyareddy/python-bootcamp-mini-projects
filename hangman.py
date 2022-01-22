import random  #for mutliple words options

def man(x):   #stick man for different levels
    if x==1:
        print("\n O\n\n")
        print("7 chances left")
    if x==2:
        print("\n O")
        print(" |\n")
        print("6 chances left")
    if x==3:
        print("\n O")
        print("\\|\n")
        print("5 chances left")
    if x==4:
        print("\n O")
        print("\\|/\n")
        print("4 chances left")
    if x==5:
        print("\n O")
        print("\\|/")
        print("/ ")
        print("3 chances left")
    if x==6:
        print("\n O")
        print("\\|/")
        print("/ \\")
        print("2 chances left")
    if x==7:
        print("\n O_|")
        print("\\|/")
        print("/ \\")
        print("1 chances left")
    if x==8:
        print("\n O_|")
        print("/|\\")
        print("/ \\")
        print("\nyou are deaddd,goodbye\n")
        print("Heres the word-",word)
        print("heres what you guessed...")




word= random.choice(['horse',"purple","dolphin",'cane','brother','office','tortoise',"anaconda"])   #many words can be added easily
wrong=int(0)
used=''
blanks=''
for i in range(len(word)):  #creation of blanks based on word chosen
    blanks=blanks+'*'

print("guess the word in less that 8 attempts")
print(blanks)



while (wrong!=8 and blanks!=word): 

    y= input('guess the letters in the word\n')[0].lower()  #coverts upped to lowercase any only accepts first character if there are multiple
    if not y.isalpha():  #must be an alphabet
        print('give only alphabets')
        continue

    flag=0

    for p in range(len(used)):    #repeated alphabets are not acknowledged
        if used[p]==y:
            print("already guessed,try another letter")
            print(blanks)
            flag=1
            break;   

    if (flag==0):
        flog=0
        for x in word:
            if x==y:    #if letter matchs
                position=0
                flog=1

                while position < len(word):  #for same at multiple different positions
                    position = word.find(y, position) 
                    if position == -1:
                         break
                    string_list = list(blanks)
                    string_list[position] = y
                    blanks = "".join(string_list)
                    position +=1

                '''position = word.find(y)
                if position == -1:
                    break
                string_list = list(blanks)
                string_list[position] = y
                blanks = "".join(string_list)'''

        if flog==0:   #incase letter doesnt match
            wrong=wrong+1
            man(wrong)
        print(blanks)
        used=used+y  #update history of guessed letter

if(blanks==word):
    print("\ncongrats kiddo,you won!\n")
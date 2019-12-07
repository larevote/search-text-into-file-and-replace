running = True
file_exist = False
while running:
    word_replace = ""
    word_find = ""
    file_name = ""
    while word_replace == "":
        word_replace = str(input("enter word replace:"))
    while word_find == "":
        word_find = str(input("enter word find :"))
    while file_name == "":
        file_name = str(input("enter file name:"))
    try:
        fire = open(file_name,"r+")
        file_exist = True
    except:
        print("File not exist")
    if file_exist == True:
        text = str(fire.read())
        fire.close()
        text = str(text.replace(word_find,word_replace))
        fire_new = open(file_name,"w")
        fire_new.write(text)
        fire_new.close()
    stop = str(input("for stop program write stop:"))
    if stop == "stop":
        running = False
print("Made By Mazong")


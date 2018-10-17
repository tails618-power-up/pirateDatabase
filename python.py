file=open("myfile.txt","a")
file.write("Hey guys! It's me, some random youtuber! AKA... Drewsenberg!")
file.close()
try:
    file=open("myfile2.txt","r")
    contents=file.read()
    file.close()
    print(contents)
except:
    print("THIS FILE DONT STINKIN EXIST YA BOI LIKE AND SUBSCRIBE FOR MOR DREWENBERG SLIME VIDS!")
    file=open("myfile2.txt","w")
    file.close()

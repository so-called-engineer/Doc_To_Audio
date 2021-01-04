import fitz,pyttsx3
print("enter the file path")
with fitz.open(input()) as pdf:
    mytext=""
    print("preparing....")
    for page in pdf:
        mytext+=page.getText()
engine=pyttsx3.init()
engine.setProperty("voice",engine.getProperty("voices")[1].id)
engine.say(mytext)
engine.runAndWait()

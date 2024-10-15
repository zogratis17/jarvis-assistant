import speech_recognition as sr

#i = 1
#for name in sr.Microphone.list_microphone_names():
#   print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(i, name))
#  i += 1

recognizer = sr.Recognizer() #initialize the recognizer
def mic1():
    with sr.Microphone(device_index=1) as source:
        print("Say something") 
        recognizer.adjust_for_ambient_noise(source) # try to remove background noise
        audio = recognizer.listen(source) # listen for the first phrase and extract it into audio data
        print('Recognizing...')
        text = recognizer.recognize_google(audio)
        print('You said: '+text)
    return text

#mic1()
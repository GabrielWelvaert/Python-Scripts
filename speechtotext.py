import speech_recognition as sr 

#list of .wav files in same directory as this file:
coach = ['file1.wav', 'file2.wav']

#wiping data from output.txt
open('output.txt','w').close() 

success = 0
failure = 0

#each audio file gets its own line in output.txt:
for file in coach:

    with sr.AudioFile(file) as source:
        audio = sr.Recognizer().record(source)

    with open('output.txt', 'a') as f:

        #translating audio file to text
        try:
            f.write(f"{sr.Recognizer().recognize_google(audio)} = {file}\n")
            success += 1
            print(f"file {coach.index(file)+1}/{len(coach)} read successfully by google")

        #uninterpretable audio files are matched with "ERROR"; occurs for things like screaming or grunting
        except sr.UnknownValueError:
            f.write(f"ERROR = {file}\n")
            failure += 1
            print(f"file {coach.index(file)+1}/{len(coach)} read unsuccessfully by google")

    f.close()


print(f"Task complete with {success} files translated ({((len(coach)-failure)/len(coach))*100}% success rate)")



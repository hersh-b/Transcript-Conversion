# Gets transcript file from LARCH 60 class and converts it into a readable document
# Code written by Hersh Budhwar :D


tNum = input("Enter the number following which transcript to convert. Put 0 if the filename is just Transcript.txt\n")





### I would not recommend touching the code below unless you know how python works ###
### ------------------------------------------------------------------------------ ###



if tNum == '0':
    transcriptName = "Transcript"
else:
    transcriptName = "Transcript" + " (" + tNum + ")"
    
fileName = transcriptName + ".txt"
newFileName = "Adjusted " + transcriptName + ".txt"

file = open(fileName, 'r')
contents = file.read()

tLength = len(contents) # A cute lil var

contents = contents.replace("\n", " ") # Gets rid of all newlines

# print(contents) # Debugging purposes

for c in range (tLength):
    if len(contents) > (c+20):
        if contents[c].isdigit():
            if contents[c+1].isdigit():
                if contents[c+2] == ":": #0-16
                    tStart = contents[:c]
                    tEnd = contents[c+16:]
                    contents = (tStart + tEnd)
                    tLength = len(contents)
                    
file.close

with open(newFileName, 'w') as f:
    f.write(contents)
    
print(contents)
                
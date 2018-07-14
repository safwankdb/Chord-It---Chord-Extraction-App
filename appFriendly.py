from utilities import chord_sequence
from pickle import load
from os import listdir
models = [i for i in listdir() if i[-4:] == '.sav']
models.sort()
#print('Following models were found. Select which one to use. If you are new, use version 3')
#for i in range(len(models)):
#    print(i + 1, ':', models[i])
#i = int(input('Input model number\n'))
i=1
#if i > len(models) or i < 1:
#    print('Wrong input. Terminating...')
#    exit()
model = load(open(models[i - 1], 'rb'))
#file = input("Enter name of file (alongwith path) : ")

#print('The likely chord sequence in audio file is:')
def appFriendlyOutput(filelocation):
	a=''
	for chord in chord_sequence(model, filelocation, 1):
    #print(chord, end = ' ')
		a=a+chord+' '
	return a

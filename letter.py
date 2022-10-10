alphabet= [i for i in range(1,26)]
letters=[]
ch_index=[]
#stores all the alphabets in the letters list
alpha = 'A'
for i in range(0, 26):
    letters.append(alpha)
    alpha = chr(ord(alpha) + 1)
#takes the message as input from user
message = input ("Enter the message :")
message=message.upper()
length= len(message)
#converts the message into its corresponding numbers
for i in range(length):
    index= letters.index(message[i])
    ch_index.append(index+1)
print(ch_index)

#modifies the numbers according to the condition

for i in range(length):
    for j in range(i,length):
        if ch_index[i]>ch_index[j]:
            ch_index[i]=ch_index[i]-ch_index[j]
            break
print(ch_index)


encoded=[]
en=""
for i in range(length):
    en=en+letters[ch_index[i]-1]
print("The encoded message: " + en)

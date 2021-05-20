import uuid
import random
from getmac import get_mac_address as gma
# printing the value of unique MAC
# address using uuid and getnode() function 

random.seed(2000)

# choices=[]
def initChoices(choices):
    # # global choices
    # if choices!=[]:
    #     return choices
    base=ord('a')
    for i in range(26):
        choices.append(chr(base+i))
    for i in range(10):
        choices.append(str(i))
    return choices


def generate_key1(choices):
    # global choices
    length=len(choices)
    key1=[]
    letters=[]
    for i in range(length):
        temp = random.choice(choices)
        letters.append(temp)
        key1.append(ord(temp))
    print("RANDOM KEY GENERATED (key1):","".join(letters))
    return key1


def generate_key2():
	key_ascii=[ord(i) for i in gma().replace(':',' ')]
	return key_ascii


def encryption(plain_text,key1,key2):

	text_ascii=[]
	for i in plain_text:
		text_ascii.append(ord(i))

	# print(text_ascii)

	first_phase=[]
	n=len(text_ascii) 
	# Length of plain text


	second_phase=[]
	unicodex=[]
	for i in range(0,n):
		P=text_ascii[i] * (key1[i%36] + i)
		first_phase.append(P)

		P2= P ^ key2[i%len(key2)]
		second_phase.append(P2)

		unicodex.append(chr(P2))

	# print('Second Phase: ',second_phase)
	return unicodex


def decryption(encoded_val,key1,key2):
	msg_final=[]
	for i in range(0,len(encoded_val)):

		msg_num = ord(encoded_val[i]) ^ key2[i%len(key2)]
		msg_deno =  key1[i%36] + i
		msg_final.append(chr(int(msg_num/msg_deno))) 

	print('Decoded Message: ',''.join(msg_final))


if __name__ == "__main__":
	# print(key1,key2)
	# plain_text='Everything is all right'
	plain_text=input('Enter message you want to encode: \n')

	choices = initChoices()
	key1=generate_key1(choices)

	key2=generate_key2()
	print ('MAC address (key2): '+gma())

	encoded_val = encryption(plain_text, key1, key2)

	print('Encoded Characters: ',encoded_val)
	print('Encoded Message',''.join(encoded_val))

	decryption(encoded_val,key1,key2)

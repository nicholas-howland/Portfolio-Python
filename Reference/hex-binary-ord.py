from sys import argv
import base64

string_data=argv[1]
binary_string=""
hex_string=""

print("Parsing : "+string_data)
print("Char | Binary | Hex")
for i in string_data:
	print(i+" : ",end="")
	print("00"+bin(ord(i)).split("b")[1],end="")
	binary_string=binary_string+"00"+bin(ord(i)).split("b")[1]
	print(" : "+hex(ord(i)))
	hex_string=hex_string+hex(ord(i))
count=0
print()
print("Binary Representation")
for i in binary_string:
	count=count+1;
	print(i,end="")
	if(count%4==0):
		print(" ",end="")

print("\nNumber of bits: "+str(count))

count=0;
print("\n\nHexadecimal Representation")
hex_string=hex_string.split("0x")
for i in hex_string:
	count=count+1
	print(i,end=" ")
	if(count%8==0):
		print()

print("\n\nBase64 encoded string")
base_64_data=str(base64.b64encode(string_data.encode('utf-8')))
split_data=base_64_data.split("'")
print(split_data[1])
count=0
print("Binary Representation of base64 string")
for i in binary_string:
	count=count+1;
	print(i,end="")
	if(count%6==0):
		print(" ",end="")

print()
## print(binary_string)


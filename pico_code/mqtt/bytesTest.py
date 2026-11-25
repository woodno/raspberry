msg = b'50'
print (msg)
#Uncomment the next line to show
#that msg is not a string
#print (msg + 'text')
#Uncomment the following line to
#show msg is not an int but a byte
#print (3 + msg)

num = int (msg)
#This tells the system how to
#interpret a byte into a string.
#essentially the next line says
#the byte value of 50 (00110010)
#turn it into a string using utf-8 encoding

numStr = msg.decode("utf-8")
# Now the byte 50 is turned into
# • Character '5':
# 	• Hexadecimal: 0x35
# 	• Decimal: 53
# 	• Binary: 00110101
# • Character '0':
# 	• Hexadecimal: 0x30
# 	• Decimal: 48
# 	• Binary: 00110000
#According to the rules of a lookup table
print (numStr)
num = int(numStr)
print (num + 7)

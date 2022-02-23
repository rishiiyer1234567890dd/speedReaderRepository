

##Paste text into 'text' variable
text = ''' '''

textStr = text.replace('\n',' ')

textStr = textStr.split(' ')

print(textStr)
file = open('/Users/riyer/test_proj/speedReaderUI/data/text.txt', 'w')
file.write('')
x = 0
file = open('/Users/riyer/test_proj/speedReaderUI/data/text.txt', 'a')
for i in textStr:
     file.write(textStr[x]+"\n")
     x=x+1
     


person = "Jose"

#print("my name is {}".format(person))
#print(f'my name is {person}')

d = {"a":1,"b":2}


#print(f'my number for a is : {d['a']}') 

library = [{'james cook','socialization',23},('james robert','the atomic habits',100),('darren hardy','the compound effect',120)]

#print(f' author is {library[0]}')

#for author,topic,price in library:
    #print(f'Author {author:{10}}, Topic {topic:{10}}, Price {price:.>{10}}')

from datetime import datetime
#https://strftime.org/
today = datetime(year=2019,month=2,day=2)

#print(f'today : {today}')
#print(f'today : {today:%B %d}')

my_File = open('test.txt')
#print(my_File)

content = my_File.read()
#print(content)

content = my_File.seek(0)

content = my_File.read()

#print(content)

my_file_content = my_File.readlines()

#print(my_file_content)

#for line in my_file_content:
    #print(line.split()[0])

file_content = open('test.txt','w+')
file_content.read()
print(file_content.read())

file_content.write('I am Sunny Sharma')

#If we donot have any file then opening a file in a+ mode will create a new file 


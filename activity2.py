file = open('sample_doc1.txt', 'x')
file.close()

import os 
print("To check if my_file exists or no")
if os.path.exists('my_file.txt') :
  os.remove('my_file.txt')

else :
  print("This file does not exist")

my_file = open('Codingal1.txt', 'w')
my_file.write("Hi ! I am a Penguin.I'm an year old")
my_file.close()

os.remove('Codingal2.txt')
os.rmdir('UNTITLED FOLDER 10')
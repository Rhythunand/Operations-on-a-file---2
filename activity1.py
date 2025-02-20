with open('Codingal1.txt', 'w') as file:
  file.write("Hi! I am a Penguin.I'm an year old")
file.close()

with open('Codingal1.txt', 'r') as file :
  data = file.readlines()
  print("Words in this file are.....")
  for line in data :
    word = line.split()
    print(word)
file.close()
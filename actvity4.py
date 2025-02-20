with open('Codingal2.txt') as fp:
  data1 = fp.read()

with open('sample_doc.txt') as fp:
  data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files")
with open ('Codingal1.txt', 'w') as fp:
  fp.write(data1)
file = open('Codingal1.txt', 'r')
file2 = open('sample_doc.txt', 'w')

lines_seen = set()
print("Eliminating duplicate lines....")

for line in file :
  if line not in lines_seen :
    file2.write(line)

    lines_seen.add(line)

file.close()
file2.close()
f = open("Pasta2.csv", "r", encoding = "utf8")
data = f.read()
#print(data)
rows = data.split('\n')
full_data = []
#print(rows)
print("\n")

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)

lista1 = []
for i in full_data[0]:
  if i[:2] == "a)":
    print(i)
  else: 
    print(i.strip('""'))    

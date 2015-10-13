largest = 0
for i in range(100,1000):
  for j in range(100,1000):
    prod = i*j
    word = str(prod)
    drow = ''
    for k in range(0,len(word)):
      drow+=word[len(word)-k-1]
    dorp = int(drow)
    if dorp==prod and prod>largest:
      largest=prod
print largest

sum = 0

for i in range(0,1000):
  if i%3==0 or i%5==0:
    sum+=i
print sum


//I don't know python so this is JS (answer from wikipedia)
//I'm trying to see how pushing and merging works on GitHub

function Sum(n, num){
  tot = 0;
  for(i = 1; 1<n/num; i++){
    tot += i*num;
  }
  return tot;
}

ans = Sum(ntot, n1) + Sum(ntot, n2) - Sum(ntot, n1*n2);


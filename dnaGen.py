import random
n=50
m=50
v=1
while(n<=500):
     while(m<=500):
          while(v<3):
               file = f"{n:03d}n{m:03d}m{v}.seq"
               f = open(file, 'w')
               seq=[str(n)+'\n',
                    str(m)+'\n',
                    ''.join(random.choices(['A','T','C','G','-'],k=n))+'\n',
                    ''.join(random.choices(['A','T','C','G','-'],k=m))]
               f.writelines(seq)
               f.close()
               v+=1
          v=1
          m+=50
     m=50
     n+=50


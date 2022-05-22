import random
n=1000
m=1000
v=1
while(n<=10000):
     while(m<=10000):
          while(v<3):
               file = f"{n:05d}n{m:05d}m{v}.seq"
               f = open(file, 'w')
               seq=[str(n)+'\n',
                    str(m)+'\n',
                    ''.join(random.choices(['A','T','C','G','-'],k=n))+'\n',
                    ''.join(random.choices(['A','T','C','G','-'],k=m))]
               f.writelines(seq)
               f.close()
               v+=1
          v=1
          m+=2000
     m=1000
     n+=1000


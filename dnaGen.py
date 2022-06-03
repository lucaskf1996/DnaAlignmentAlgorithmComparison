import random
n=10
m=10
v=2
while(n<=100):
     while(m<=100):
          # while(v<3):
          file = f"{n:03d}n{m:03d}m{v}.seq"
          f = open(file, 'w')
          seq=[str(n)+'\n',
               str(m)+'\n',
               ''.join(random.choices(['A','T','C','G','-'],k=n))+'\n',
               ''.join(random.choices(['A','T','C','G','-'],k=m))]
          f.writelines(seq)
          f.close()
          #      v+=1
          # v=1
          m+=10
     m=10
     n+=10


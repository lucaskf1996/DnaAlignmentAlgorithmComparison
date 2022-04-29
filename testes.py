import subprocess
import time
import os

files = os.listdir("./tests")
files.sort()
# print(files)
resultados = open("./resultados.txt", "a")
for file in files:
    # print(file)
    with open("./tests/"+file) as f:
        start = time.perf_counter()
        proc = subprocess.run(['./mainSmith'], input=f.read(), text=True, capture_output=True)
        end = time.perf_counter()
        print(end - start)
        resultados.write(f"{end - start}\n")
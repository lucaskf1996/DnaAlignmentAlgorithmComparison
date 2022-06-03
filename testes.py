import subprocess
import time
import os

files = os.listdir("./smaller_tests")
files.sort()
resultados = open("./resultados/exhaustiveParallel.txt", "a")
for file in files:
    with open("./smaller_tests/"+file) as f:
        print(file)
        start = time.perf_counter()
        proc = subprocess.run(['./exhaustiveParallel'], input=f.read(), text=True, capture_output=True)
        end = time.perf_counter()
        print(end - start)
        resultados.write(f"{end - start}\n")
resultados.close()

# resultados = open("./resultados/exhaustiveParallel.txt", "a")
# with open("./smaller_tests/010n010m2.seq") as f:
#     start = time.perf_counter()
#     proc = subprocess.run(['./exhaustiveParallel'], input=f.read(), text=True, capture_output=True)
#     end = time.perf_counter()
#     print(end - start)
#     resultados.write(f"{end - start}\n")
# resultados.close()
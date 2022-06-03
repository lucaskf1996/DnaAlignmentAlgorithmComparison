import subprocess
import time
import os

# files = os.listdir("./smaller_tests")
# files.sort()
# resultados = open("./resultados/exhaustiveParallel.txt", "a")
# for file in files:
#     with open("./smaller_tests/"+file) as f:
#         print(file)
#         start = time.perf_counter()
#         proc = subprocess.run(['./exhaustiveParallel'], input=f.read(), text=True, capture_output=True)
#         end = time.perf_counter()
#         print(end - start)
#         resultados.write(f"{end - start}\n")
# resultados.close()

resultados = open("./resultados/exhaustiveParallelBiggest.txt", "a")
with open("./biggest_test/10000n10000m1.seq") as f:
    start = time.perf_counter()
    proc = subprocess.run(['./exhaustiveParallel'], input=f.read(), text=True, capture_output=True)
    end = time.perf_counter()
    print(end - start)
    resultados.write(f"{end - start}\n")
resultados.close()

resultados = open("./resultados/exhaustiveSequentialBiggest.txt", "a")
with open("./biggest_test/10000n10000m1.seq") as f:
    start = time.perf_counter()
    proc = subprocess.run(['./mainExaustiva'], input=f.read(), text=True, capture_output=True)
    end = time.perf_counter()
    print(end - start)
    resultados.write(f"{end - start}\n")
resultados.close()
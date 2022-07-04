import time
from multiprocessing import Pool
start_time = time.time()
def f(x):
    time.sleep(2) # Wait 2 seconds
    print(x*x)
p = Pool(8)
p.map(f, [1, 2, 3, 4])
p.close()
p.join()

print("--- %s seconds ---" % (time.time() - start_time)) #Printing the time of the execution
import time
start_time = time.time()
def f(x):
    time.sleep(2) # Wait 2 seconds
    print(x*x)
for item in [1, 2, 3, 4]:
    f(item)
print("--- %s seconds ---" % (time.time() - start_time)) #Printing the time of the execution
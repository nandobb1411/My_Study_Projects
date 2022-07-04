import Implementation_1
from multiprocessing import Pool



p = Pool()
p.map(Implementation_1.main_function, [1, 2, 3, 4])
p.close()
p.join()
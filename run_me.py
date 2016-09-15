
import math
import time

def pi():
	sum = 0.0
	for k in range(0, 10000000):
		sum += (-3.0)**(-k) / (2.0*k+1.0)
	return math.sqrt(12.0) * sum

start = time.time()
print(pi())
end = time.time()
print("Elapsed time: " + str(end-start))
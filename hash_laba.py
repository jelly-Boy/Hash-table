import time
import random

class HashFunction():
	"""docstring for HashFunction"""
	def __init__(self, bucket):
		self.bucket = bucket
		self.hashTable = [[0] * 1 for i in range(bucket)]
		
	
	def Insert(self, v):
		self.hashTable[self.Hash(v)].append(v)

	def Hash(self, a):
		return (a % self.bucket)

	def MaxLenght(self):
		res = 0
		for i in range(self.bucket):
			if res < len(self.hashTable[i]):
				res = len(self.hashTable[i])
		print(f"Max lenght >> {res}")

	def MinLenght(self):
		res = 100000
		for i in range(self.bucket):
			if res > len(self.hashTable[i]):
				res = len(self.hashTable[i])
		print(f"Min lenght >> {res}")

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def func():
	n = 1000000
	h = HashFunction(round(n / 100))

	start = time.time()
	for i in range(0, n):
		v = random.randint(0, n)
		h.Insert(v)
	end = time.time()
	delta = end - start
	print(f"Time of inserting {n} integers {toFixed(delta, 6)} seconds.")
	print(f"Time of 1 simple operation {toFixed((delta / (2 * n + n / 100)),10)} seconds")
	h.MaxLenght()
	h.MinLenght()

if __name__ == "__main__":
	for i in range(0, 10):
		func()
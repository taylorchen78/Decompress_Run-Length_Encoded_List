"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [a, b] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are a elements with value b in the decompressed list.

Return the decompressed list.
"""

def decompressRLElist(List):
	outputList = []
	for i in range(0, len(List), 2):
		count = List[i]
		num = List[i + 1]
		for j in range(count):
			outputList.append(num)
	return outputList

print(decompressRLElist([1,2,3,4]))

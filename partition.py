import math

def biggest_pile(N, k):
	"""
	Find the largest pile after N items have been split "evenly"
	into k piles.
	"""
	return int( math.ceil( float(N) / k ) )

def min_partition(N, n):
	"""
	Find the minimum integer k >= 1 such that N > 0 items can be split
	into k piles without any pile obtaining more than n > 0 items.

	In other words: find minimum integer k >= 1, such that ceil(N/k) <= n.
	This function is correct in this more general sense, even if
	N, n > 0 are non integers.
	"""
	return int( math.ceil( N / math.floor(n) ) )
	
import unittest

import partition

import math
import numpy as np

class PartitionTest(unittest.TestCase):

	def test_min_partition(self):
		# number to spit
		Ns = np.arange(1,10)
		# max allowable pile size
		ns = np.arange(1,10)

		# meshgrid of all combinations
		Nmat, nmat = np.meshgrid(Ns, ns)

		# min_partition; function under test
		f = np.vectorize(partition.min_partition)

		# compute result matrix: number of piles in each scenario
		kmat = f(Nmat, nmat)

		# confirm expectations; k >= 1, and largest pile is not too large
		@np.vectorize
		def check(N,k,n):
			return k > 0 and partition.biggest_pile(N,k) <= n

		# all results check out!
		self.assertTrue( check(Nmat, kmat, nmat).all() )
		# and are minimal!
		self.assertFalse( check(Nmat, kmat - 1, nmat).any() )
		

if __name__ == '__main__':
    unittest.main()

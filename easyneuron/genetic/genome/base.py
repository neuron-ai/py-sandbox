from dataclasses import dataclass
from functools import total_ordering
from typing import List

from easyneuron.exceptions.exceptions import EmptyDataError

@dataclass(unsafe_hash=True, eq=True, repr=True)
@total_ordering
class BaseGenome:
	genes: List[float]
	fitness: float = 0.0

	def __init__(self, genes: List[float]=None):
		if genes is None:
			raise EmptyDataError("genomes cannot be empty.")

		self.genes = genes or []

	def __gt__(self, other):
		return self.fitness > other.fitness

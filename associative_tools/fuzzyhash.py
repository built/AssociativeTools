class FuzzyHash:
	
	# Challenges:
	# performance
	# Describing ranges
	# Describing asymmetric unbounded ranges (3 to infinity, etc.)
	# Non-integer keys and abstract (but still numeric) keys, ex: pi or e?
	# Could you have a revolving hash that triggers on multiples of pi? So cycling happens?
	
	def __init__(self):
		self.slots = []
	
	def __getitem__(self, key):
		for key_range, value in self.slots:
			if key in key_range:
				return value

	def __setitem__(self, key_range, value):
		self.slots += [(key_range, value)]

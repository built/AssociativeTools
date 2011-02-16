import functools

class AssociativeSet():
	def __init__(self, name):
		self.name = name
		self.contents = {}
		self.counter = 0

	def add(self, *named_sets):
		for named_set in named_sets:
			self.contents[named_set.name] = named_set

	def __len__(self):
		return len(self.contents)

	def connect(self, named_set):
		self.contents[named_set.name] = named_set
		named_set.contents[self.name] = self

	def disconnect(self, named_set):
		del self.contents[named_set.name]
		del named_set.contents[self.name]

	def __contains__(self, item):
		return (item in self.contents)

	def comprehend(self, *items):
		given_items = set(self.lookup_items_by_name(*items))
		intersection = self.related(given_items) - given_items
		return list(intersection)

	def create_relation(self, basename=None):
		relation = AssociativeSet("__%s__%s" % (basename or "relation", self.counter) )
		relation.connect(self)
		self.counter += 1
		return relation

	def related(self, criteria):
		if len(criteria) < 1: return set()
		return set(each for each in self.contents.values() if criteria.issubset( each.contents.values() )   )

	def lookup_items_by_name(self, *names):
		return [self.contents[name] if name in self else AssociativeSet(name) for name in names]

	def associate(self, *items):
		items = self.lookup_items_by_name(*items)
		self.add(*items)
		relation = self.create_relation()
		[relation.connect(item) for item in items]

	def disassociate(self, *items):
		for relation in self.comprehend(*items):
			for item in self.lookup_items_by_name(*items):
				relation.disconnect(item)
			self.disconnect(relation)

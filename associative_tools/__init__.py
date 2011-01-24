import functools

class NamedSet():
	def __init__(self, name):
		self.name = name
		self.contents = {}

	# We're expecting to add other NamedSets, so are guaranteed
	# a 'name' attribute.
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

class Workspace:
	def __init__(self):
		self.contents = {}

	def associate(self, *items):
		for item in items:
			if item not in self.contents:
				self.contents[item] = set()
			self.contents[item].add(set([thing for thing in items if thing != item]))

	def disassociate(self, *items):
		for item in items:
			for other in set(items) - set([item]):
				self.contents[other].remove(item)

	def comprehend(self, *items):
		known = set()
		for item in items:
			if item in self.contents:
				[known.add(x) for x in self.contents[item] ]
		return known - set(items)

	def dump(self):
		print
		print "--------------------------------------"
		for key in self.contents.keys():
			print "%s => %s" % (key, self.contents[key])
		print "--------------------------------------"


class RelationalWorkspace(NamedSet):
	def __init__(self, name):
		NamedSet.__init__(self, name)
		self.counter = 0

	def create_relation(self):
		relation = NamedSet("__relation__%s" % self.counter)
		relation.connect(self)
		self.counter += 1
		return relation

	def related(self, named_sets):
		related = set()
		for named_set in named_sets:
			for val in named_set.contents.values():
				related.add(val)
		return related

	def comprehend(self, *items):
		given_items = self.lookup_existing_items_by_name(*items)
		intersection = self.related(given_items) - set(given_items)
		return [x for x in intersection] # TODO: native way to Set => [] ??

	def names_to_items(self, *names):
		return [item.name if isinstance(item, NamedSet) else NamedSet(item) for item in self]

	def lookup_existing_items_by_name(self, *names):
		return [self.contents[name] for name in names if name in self]

	def associate(self, *items):
		items = [NamedSet(item) for item in items]
		self.add(*items)
		relation = self.create_relation()
		[relation.connect(item) for item in items]

	def disassociate(self, *items):
		for relation in self.comprehend(*items):
			for item in self.lookup_existing_items_by_name(*items):
				relation.disconnect(item)
			self.disconnect(relation)



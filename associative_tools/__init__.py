import functools

class NamedSet():
	def __init__(self, name):
		self.name = name
		self.contents = set()
	def add(self, *items):
		[self.contents.add(each) for each in items]
	def __len__(self):
		return len(self.contents)
	def connect(self, item):
		self.add(item)
		item.add(self)


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

	def fetch_relatives(self, *items):
		return reduce(lambda related, item: related & item.contents, items, self.contents)

	def names_to_items(self, *names):
		return [item for item in self.contents if item.name in names]

	def associate(self, *items):
		items = [NamedSet(item) for item in items]
		self.add(*items)
		relation = self.create_relation()
		[relation.connect(item) for item in items]

	def disassociate(self, *items):
		items = self.names_to_items(*items)
		[related.contents.remove(item) for item in self.fetch_relatives(*items) for related in item.contents]

	def comprehend(self, *items):
		items = self.names_to_items(*items)
		return set([match for relation in self.fetch_relatives(*items) for match in relation.contents]) - set(items)



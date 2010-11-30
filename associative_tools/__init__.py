class NamedSet:
	def __init__(self, name):
		self.name = name
		self.contents = set()

class Workspace:
	def __init__(self):
		self.contents = {}

	def associate(self, *items):
		for item in items:
			if item not in self.contents:
				self.contents[item] = set()
			self.contents[item].update(set([thing for thing in items if thing != item]))

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



import unittest
from associative_tools import AssociativeSet

class AssociativeSetTest(unittest.TestCase):

	def make_sets(self, items):
		return [AssociativeSet(item) for item in items]

	def test_named_sets_should_know_names(self):
		n = AssociativeSet("foo")
		self.assertEqual(n.name, "foo")

	def test_adding_items(self): # DO WE EVEN WANT ADD() ??
		n = AssociativeSet("root")
		n.add( *self.make_sets(["foo", "bar"]) )
		self.assertEqual(len(n.contents), 2)

	def test_disallow_duplicates(self):
		n = AssociativeSet("root")
		n.add( *self.make_sets(["foo", "bar", "foo", "foo"]) )
		self.assertEqual(len(n.contents), 2)

	def test_contains(self):
		n = AssociativeSet("root")
		n.add( *self.make_sets(["foo", "bar"]) )

		self.assertTrue("foo" in n, "Should see the named set")



if __name__ == '__main__':
    unittest.main()

import unittest
from associative_tools import AssociativeSet

class WorkspaceTest(unittest.TestCase):

	def test_association_should_create_relations(self):
		w = AssociativeSet("")
		w.associate("foo", "bar")
		self.assertEqual(len(w.contents), 3) # foo, bar, and the relation between them.

	def test_associate_many(self):
		w = AssociativeSet("")
		w.associate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents), 5) # foo, bar, baz, blarf and the relation between them.

	def test_disassociate_many(self):
		w = AssociativeSet("*")
		w.associate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents), 5) # foo, bar, baz, blarf and the relation between them.

		relations = w.comprehend("foo", "bar", "baz", "blarf")
		self.assertEqual( len(relations), 1) # Should have one match here.

		w.disassociate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents.values()), 4) # The named items still exist, but there is no relation now.

		relations = w.comprehend("foo", "bar", "baz", "blarf")
		self.assertEqual( len(relations), 0) # Should no matches here.

	"""
	Given a list of item names, return the relation which relates them.
	"""
	def test_comprehension(self):
		w = AssociativeSet("")
		w.associate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents), 5) # foo, bar, baz, blarf and the relation between them.

		matching_relation = w.comprehend("foo", "bar")[0]
		self.assert_("baz" in [result.name for result in matching_relation.contents.values()], "Not seeing baz in results")

	def test_missing_comprehension(self):
		w = AssociativeSet("*")
		w.associate("foo", "bar")
		self.assertEqual(w.comprehend("baz", "blarf"), [], "Got back a result! Should have retrieved nothing.")

	"""
	Should not return a partial match. It's all or nothing baby!
	"""
	def test_partial_comprehension(self):
		w = AssociativeSet("*")
		w.associate("foo", "bar")
		self.assertEqual(w.comprehend("bar", "blarf"), [], "Got back a result! Should have retrieved nothing.")

	"""
	Create a relation with a particular basename.
 	Useful when debugging a system.
	"""
	def test_create_special_relation(self):
		w = AssociativeSet("*")
		w.create_relation("foo")
		self.assertTrue("__foo__0" in w.contents)


if __name__ == '__main__':
    unittest.main()

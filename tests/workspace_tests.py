import unittest
from associative_tools import RelationalWorkspace, NamedSet

class WorkspaceTest(unittest.TestCase):

	def test_association_should_create_relations(self):
		w = RelationalWorkspace("")

		w.associate("foo", "bar")
		self.assertEqual(len(w.contents), 3) # foo, bar, and the relation between them.

	def test_associate_many(self):
		w = RelationalWorkspace("")

		w.associate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents), 5) # foo, bar, baz, blarf and the relation between them.
	
	def test_disassociate_many(self):
		w = RelationalWorkspace("")

		w.associate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents), 5) # foo, bar, baz, blarf and the relation between them.
		
		w.disassociate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents), 4) # The named items still exist, but there is no relation now.

	def test_comprehension(self):
		w = RelationalWorkspace("")

		w.associate("foo", "bar", "baz", "blarf")
		self.assertEqual(len(w.contents), 5) # foo, bar, baz, blarf and the relation between them.

		results = w.comprehend("foo", "bar")
		self.assert_("baz" in [result.name for result in results], "Not seeing baz in results")
		self.assert_("foo" not in [result.name for result in results], "Should not see foo in results")


if __name__ == '__main__':
    unittest.main()

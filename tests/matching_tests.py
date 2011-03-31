import unittest
from associative_tools import AssociativeSet

class MatchingTest(unittest.TestCase):

	"""
	Matching rules: (matches, describes)
	If names are the same on the top node, it's a match.
	If the names are not the same, it's assumed that one node describes the other,
	and the contents needs to match.
	"""
	def test_simplest_match(self):
		setA = AssociativeSet("foo")
		setB = AssociativeSet("foo")
		self.assertTrue(setA.matches(setB))

	def test_single_level_match(self):
		"""
		Test to see if one graph describes another (tree subset)
		Note that the root nodes will not be the same. This is a test
		to see if the subject's contents contain the given pattern.
		"""
		pattern = AssociativeSet("pattern")
		subject = AssociativeSet("subject")

		# Give the subject structure
		subject.connect(AssociativeSet("string"))
		subject.connect(AssociativeSet("blarf"))
		subject.connect(AssociativeSet("fizzbinn"))

		self.assertFalse(pattern.describes(subject), "The pattern shouldn't describe the subject yet!")

		# Now give the pattern part of that structure.
		pattern.connect(AssociativeSet("string"))

		self.assertTrue(pattern.describes(subject), "The pattern should describe the subject.")


if __name__ == '__main__':
    unittest.main()

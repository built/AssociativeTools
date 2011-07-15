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


	# def test_nested_match(self):
	# 	pattern = AssociativeSet("pattern")
	# 	subject = AssociativeSet("subject")
	#
	# 	# Give the subject structure
	# 	# Looks like this:
	# 	# subject
	# 	#  __relation__
	# 	#  		string
	# 	#  __relation__
	# 	#  		blarf
	# 	#  		fizzbinn
	#
	# 	subject_relation1 = subject.create_relation()
	# 	subject_relation1.connect(AssociativeSet("string"))
	#
	# 	subject_relation2 = subject.create_relation()
	# 	subject_relation2.connect(AssociativeSet("blarf"))
	# 	subject_relation2.connect(AssociativeSet("fizzbinn"))
	#
	# 	self.assertFalse(pattern.describes(subject), "The pattern shouldn't describe the subject yet!")
	#
	#
	# 	# Create a pattern that looks like this:
	# 	# pattern
	# 	#  __relation__
	# 	#  		blarf
	# 	#  		fizzbinn
	#
	# 	# Now give the pattern part of that structure.
	# 	pattern_relation1 = pattern.create_relation()
	# 	pattern_relation1.connect(AssociativeSet("blarf"))
	# 	pattern_relation1.connect(AssociativeSet("fizzbinn"))
	#
	# 	self.assertTrue(pattern.describes(subject), "The pattern should describe the subject.")
	#
	#
	# 	# Modify the pattern to look like this:
	# 	# pattern
	# 	#  __relation__
	# 	#  		blarf
	# 	#  		fizzbinn
	# 	#  __relation__
	# 	#  		should_bust
	#
	# 	# Now give the pattern part of that structure.
	# 	pattern_relation2 = pattern.create_relation()
	# 	pattern_relation2.connect(AssociativeSet("should_bust"))
	#
	# 	self.assertFalse(pattern.describes(subject), "The pattern should NOT describe the subject at this point.")



if __name__ == '__main__':
    unittest.main()

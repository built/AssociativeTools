from associative_tools import AssociativeSet
# This should be a proper unit test.
def expect(expected, msg=""):
	if not expected:
		print "Fail: %s" % msg
	else:
		print ".", 

s = AssociativeSet("*") # * essentially means "root" or "this namespace"

s.associate("foo", "bar")

expect("foo" in s.comprehend("bar")[0], "Can't associate properly?")

expect("bar" in s.comprehend("foo")[0], "Can't associate properly a second time?")


s = AssociativeSet("*")

s.associate("foo", "bar", "baz")


expect(set(["bar", "baz"]).issubset(s.comprehend("foo")[0].terms), "Multiple associations aren't working.")

expect(set(["baz"]).issubset(s.comprehend("foo", "bar")[0].terms), "Multiple comprehensions aren't working.")


s = AssociativeSet("*")

s.associate("foo", "bar", "baz")

expect(set(["bar", "baz"]).issubset(s.comprehend("foo")[0].terms), "Multiple associations aren't working.(REDUX)")


# The 'disassociate' method has changed in the evolution from Workspace to AssociativeSet. This feature isn't used
# in any real code as of yet and likely needs to be rethought. 
# s.disassociate("foo", "bar")

# expect(set(["baz"]).issubset(s.comprehend("foo")[0].terms), "foo should still be associated with baz")

# expect(s.comprehend("bar") == set(["baz"]), "bar should still be associated with baz")

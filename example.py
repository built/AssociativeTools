from associative_tools import Workspace
# This should be a proper unit test.
def expect(expected, msg=""):
	if not expected:
		print "Fail: %s" % msg
	else:
		print ".", 

s = Workspace()

s.associate("foo", "bar")

expect(s.comprehend("bar") == set(["foo"]), "Can't associate properly?")

expect(s.comprehend("foo") == set(["bar"]), "Can't associate properly a second time?")

s.associate("foo", "bar", "baz")

expect(s.comprehend("foo") == set(["bar", "baz"]), "Multiple associations aren't working.")

expect(s.comprehend("foo", "bar") == set(["baz"]), "Multiple comprehensions aren't working.")


s.associate("foo", "bar", "baz")

expect(s.comprehend("foo") == set(["bar", "baz"]), "Multiple associations aren't working.(REDUX)")


s.disassociate("foo", "bar")

expect(s.comprehend("foo") == set(["baz"]), "foo should still be associated with baz")

expect(s.comprehend("bar") == set(["baz"]), "bar should still be associated with baz")

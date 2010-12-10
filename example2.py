from associative_tools.fuzzyhash import FuzzyHash
# This should be a proper unit test.
def expect(expected, msg=""):
	if not expected:
		print "Fail: %s" % msg
	else:
		print ".", 

scores = FuzzyHash()

scores[range(5)] = "low"
scores[range(5, 10)] = "medium"
scores[range(10, 15)] = "high"


expect(scores[3] == "low", "Score should be low")

expect(scores[8] == "medium", "Score should be medium")

expect(scores[12] == "high", "Score should be high")


bands = FuzzyHash()

bands[["The FooBarBazzes", "Spinal Tap", "Sparks"]] = 11
bands[["The Beatles", "The Who", "The Rolling Stones"]] = 10

expect(bands["Spinal Tap"] == 11, "Should see 11")



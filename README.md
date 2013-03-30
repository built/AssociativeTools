Associative Tools
--------------------
This is a library primarily containing a class called AssociativeSet (formerly Workspace). 
I created this in support of the implementation of the Wheeler programming language, but it seems useful outside of that context as well.


The classes in this library include:

* AssociativeSet
* FuzzyHash (for both Python and Ruby)



### AssociativeSet
In a very abstract sense this class lets you connect ideas together. It creates connections between named sets which creates a graph that you can traverse.


### FuzzyHash
It's a hashtable whose keys are ranges. If you supply an index that falls within a particular key's range, you get that corresponding value back.

To get a real sense of how this works in practice and when you'd want this, see `fuzzy_example.py`.





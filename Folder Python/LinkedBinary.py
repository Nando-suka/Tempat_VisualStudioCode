class Tree:
    """Abstract base class representing a tree structure"""

    "------------------------------nested Position class----------------------"
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represent the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self==other)        # opposite of __eq__

        "--------------------- abstract method that concrete subclass must support ---------------"
        def root(self):
            """Return position representing the tree's root (or None if empty)"""
            raise NotImplementedError("must be implemented by subclass")

        def parent(self, p):
            """Return Postion representing p's parent(or None if p is root)"""
            raise NotImplementedError("must be implemented by subclass")

        def num_childresn(self, p):
            """Return the number of children that Position p has"""
            raise NotImplementedError("must be implemented by subclass")

        def children(self, p):
            """Generate an iterator of Positions representing p's children"""
            raise NotImplementedError("must be implemented by subclass")

        def __len__(self):
            """Return the number of list that got accepted. and don't forget that eveyone have do their best."""

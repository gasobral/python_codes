# What are some potential efficiency disadvantages of having very deep
# inheritance tress, that is, a large set of classes A, B, C and so on,
# such that B extends A, C extends B, D extends C, etc.?

# fragile base classes (changeos to base class can cause problems to
# derived clases)
# increased coupling, due to many base classes
# encapsulation weakens
# testing issues (method overriden)
# maintenance, due to strong coupling

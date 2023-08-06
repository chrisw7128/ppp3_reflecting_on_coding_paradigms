# Functional Prompt: Implement a function that will flatten and sort an array of integers in ascending order.


def flatten(num_list):
    num_list.sort()
    return num_list


my_list = [7, 14, 22, 1, 14, 85]

print(flatten(my_list))

# How does this solution ensure data immutability?
# Without editing the function, the output cannot be changed.

# Is this solution a pure function? Why or why not?
# No, it uses a higher order function, sort().

# Is this solution a higher order function? Why or why not?
# Yes, it uses the built-in sort() function.

# Would it have been easier to solve this problem using a different programming style?
# I don't think so, no.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# This is a simple problem, and using a single function aided by a built-in function is a reasonable solution.

# --------------------------------------------------------------------------------------------------------------

# Object Oriented Prompt. Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution.


class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired""


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def __init__(self,max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self,other):
        other.condition = "trashed"


# How does this solution demonstrate the four pillars of OOP?

# Encapsulation
# Nothing is encapsulated, because everything is linked via inheritance.

# Abstraction
# Some methods from the child classes are abstracted away due to their existence in the parent class, such as max_speed and condition.

# Inheritance
# One parent class and two child classes form a classic inheritance relationship.

# Polymorphism
# None of the parent methods are overwritten by the child classes, so no polymorphism occurs.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# No, this problem seems a natural fit for OOP because it's (parent vehicle) --> (two instances of child vehicle).

# How in particular did Object Oriented Programming assist in the solving of this problem?
# Creating two child classes of Podracer was a convenient way to connect the podracer class to the two instances of it.

# --------------------------------------------------------------------------------------------------------------

# Is one of these coding paradigms "better" than the other? Why or why not?
# No, they each have their respective use cases.

# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
# Functional programming seems more appealing becaues it is more "self-contained" which seems more accessible to a beginner.

# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
# Functional: small projects with repeatable tasks that can be completed largely by isolated functions.  OOP: enterprise-grade projects where data needs to be more inter-related.

# Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
# OOP takes more effort to understand.  Nearly everybody learns OOP after functional programming for a reason.  It's less intuitive.  Practice more to deepen understanding, as is typical.

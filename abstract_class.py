""" Here we will check that weather the List is the subclass of which class .
For this Check we Already know the Super class of List but, we are confirming that weather MutablSequence is 
the abstract class or not and if it is a abstract then, weather it is possible to instantiate it or not.
as....
"""
#For this we imported the MutableSequence from the collections Module
from collections.abc import MutableSequence

# And now we will check weather MutableSequence is abstract method or not as....
print(MutableSequence.__mro__)

#(<class 'collections.abc.MutableSequence'>, <class 'collections.abc.Sequence'>, <class 'collections.abc.Reversible'>, 
# <class 'collections.abc.Collection'>, 
#  <class 'collections.abc.Sized'>, <class 'collections.abc.Iterable'>, 
# <class 'collections.abc.Container'>, <class 'object'>)

# From the above results it is clear that MutableSquence is a abstract class as above we can see that collections.abc.Mutable
#written hence it confirms that it is a abstract class

"""
*** One most Important thing to be keep in mind is that in pyhton also "object" is superclass of all classes 
this can be confirmed as .....
"""
print(issubclass(MutableSequence, object))

# the Execution gives the following result "True".

"""
So the above method issubclass(cls, class_or_tuple) is used to check weather the 'cls' is the subclass of the 
class written or not.
if it is it return True else False

Now we will check the super class of list as...
"""
print(issubclass(list, MutableSequence))
#The Result of above code is True
#From the above check it interprets that list is the subclass of MutableSequence. But, we cannot say that MutableSequence
# the Super class of list this will result in error. Because Here MutableSequence is the Abstract class and hence the
# revese is not true.
# now we check the class of list as...
print(list.__mro__)
# the above result is as (<class 'list'>, <class 'object'>) here no where we can see that list have Super class as 
#MutableSequence
#This is the strong evidence that list is the Subclass of MutableSequence but , MutableSequence is not the Super class
# List rather object is the Super class of list.



#Let's, have a example 
from abc import ABC, abstractmethod
class Graph(ABC):
	@abstractmethod
	def move(self):
		pass

class Mutable(Graph):
    def move(self):
        print("Overidding the move method in Mutable class")
g = Mutable()
g.move()
class raw(Mutable):
    def move(self):
        print("Raw class Imlementation")
    super(Mutable,g.move())


r = raw()
r.move()




"""
optimizes the memory used with classes
without __slots__, python classes constructor will initialize a hashmap with padding
this padding is meant for dynamic variable injection later on during runtime:

ex: 
user = User("bob123", "bob")
user.password = "pwd123"

Using __slots__ tells us "only allocate space for these variables"
downside is it will raise attribute error if we try to inject variables at runtime

----
Python internal optimizations:

without slots, python will try to group shared variables within instances under a single map.
This process is called key-sharing

Variables that differ will be in their own dictionary.

However, if we even inject one variable at runtime or one instnace differs by a single variable,
python will create an entirely new dictionary for all variables of that instance
"""
class User:
    __slots__ = ('userId', 'name')
    
    def __init__(self, userId, name):
        self.userId = userId
        self.name = name
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(userId={self.userId!r}, name={self.name!r})"

class User_A:
    def __init__(self, userId, name):
        self.userId = userId
        self.name = name
    

user = User("bob123", "bob")
print(user) # use __repr__ for stringified version
# user.password = "pwd123" # raises attribute error because we used __slots__

user_A = User_A("alice123", "alice")
user_A.password = "pwd123"
# print(user_A.password) # does not error, adds the attribute to class's internal dictionary

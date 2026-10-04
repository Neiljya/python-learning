from collections import namedtuple
import array

# named tuples allow for easy access/decoupling
# tuples composed of a header + array of references to its items
vector = namedtuple('vector', ['x','y'])

new_vector = vector(10,20)

# print(new_vector)
# print(new_vector.x) # outputs 10
# print(new_vector.y) # outputs 20

# int_array is more compact, because int_list is an object, 
"""
requires header 
(ref_count, 
type (in this case its a list type), 
item_ptr (points to an array of object pointers), 
size (number of items in list),
allocated (total capacity allocated for current array)
)

array.array has mostly the same header with the exception
of an object descriptor rather than object type.

it also has an exports field, (int) tracking how many
objects are viewing this array's memory (e.g. NumPy)
----
Main optimization:

array.array stores raw types not objects, each object in python
needs its own ob_refcnt and ob_type which increases its size making
array.array signifcantly smaller

"""
int_array = array.array('i', [1,2,3,4,5])
int_list = [1,2,3,4,5]

"""
Tuple vs list

tuples have smaller memory footprint than list
because lists ob_item pointer points to a separate array in memory

because lists need to dynamically grow, python swaps this pointer out when size changes.

typically ob_item in tuple is smaller than a list.
If you had a tuple with 5 items and a list with 5 items, Python over-allocates for the list
which means the tuple item array holds only 5 pointers while the list item array can hold 8 pointers

This is mainly because Python wants to make adding onto lists faster and reduce overhead of 
allocating new memory in runtime
"""
string_int_tuple = ("bob", 2) # smaller
string_int_list = ["bob", 2] # larger


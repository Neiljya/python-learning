def square(num):
    return num ** 2

iterable = [1,2,3,4,5]

# this doesnt actually evaluate anything or call anything
# this just loads instructions to do the calling
squared_map = map(square, iterable)

# this will actually "map" the items in iterable
squares_list = list(squared_map)


##################################

# generator expression vs list comps

##################################

strs = ['a','abc','abcd','add','ade','a23','a','sdasda','sfgsdfds','asdw2q','sadacxvx']

"""
Takes more memory because listcomp will store the entire list at once
"""
str_list = [s for s in strs if len(s) > 3]

for s in str_list:
    print(s)


"""
`str_list` does not store the entire list in memory,
it lazily loads the list (by storing the instructions).

It only starts to compute once its being used
"""
str_list_b = (s for s in strs if len(s) > 3)

"""
yields values one by one, once s moves to the next string,
the previous string is discarded from memory
"""
# for s in str_list_b:
#     print(s)


##############
"""
achieves the same effect as genexp, because filter() also
lazily loads the values. Does not actually store the whole list in memory
"""
str_list_c = filter(lambda s: len(s) > 3, strs)

# this will store the list in memory because the filter() object is being used by list()
# so this is less "memory friendly"
# str_list_c = list(filter(lambda s: len(s) > 3, strs)) 

for s in str_list_c:
    print(s)

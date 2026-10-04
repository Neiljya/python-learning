def square(num):
    return num ** 2

iterable = [1,2,3,4,5]

# this doesnt actually evaluate anything or call anything
# this just loads instructions to do the calling
squared_map = map(square, iterable)

# this will actually "map" the items in iterable
squares_list = list(squared_map)

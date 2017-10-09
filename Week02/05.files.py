# Files
# f = open('filename', mode)
# text_modes = ['r', 'w', 'a', 'r+']
# binary_modes = [ 'br', 'bw', 'ba', 'br+'] r+ = read-write

# f.write(a) - returns number of
# f.close() - when

# f.read(n) - n - bytes/characters

# f.tell() - position of cursor in a file
# f.seek(n) - seeks to position n

# f.readline() - returns one string with '\n' separator
# f.readlines() - returns list of strings

# Use context manager, Luke!
#
# with open('filename') as f:
#   print(f.read())


def chain(*iterators):
    for iterator in iterators:
        yield from iterator


l = list(chain(range(5), "abc"))
print(l)
# [0, 1, 2, 3, 4, 'a', 'b', 'c']

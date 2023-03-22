import big_o

def find_max(x):
     """Find the maximum element in a list of positive integers."""
     max_ = 0
     for el in x:
         if el > max_:
             max_ = el
     return max_

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(find_max, positive_int_generator, n_repeats=100)
print("best:" + str(best))


for class_, residuals in others.items():
    print('{!s:<60s}    (res: {:.2G})'.format(class_, residuals))

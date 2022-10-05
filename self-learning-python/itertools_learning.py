import itertools

first_1 = [1, 2, 3, 4, 5]
sum_list = itertools.accumulate(first_1)
print(sum_list)

second_2 = ['A', 'B', 'C', 'D']
chain_list = itertools.chain(first_1, second_2)
print(chain_list)


for items in sum_list:
    print(items)


# Super interesting application of itertools 

names = ['Tim','Joe','Bill','Susan','Jen']
show = [1,0,1,0,1]
compressed_list = itertools.compress(names, show)
print(list(compressed_list))

# Note that for this list Joe and Susan are turned off since the list 
# had 0 instead of 1. This would come in handy when you generate a list 


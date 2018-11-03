import csv

# loadDataset()
f = open('data/sample.csv', 'r')
d = f.read()
dataset = d.split('\n')

# loadTagset()
g = open('data/tags.csv', 'r')
e = g.read()
tagset = e.split('\n')

# printDataset()
def print_list(input_list):
	print('\n'.join(map(str, input_list)))

print_list(tagset)
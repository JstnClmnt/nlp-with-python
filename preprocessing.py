import csv

# loadDataset() and loadTagset()
def load_csv(filename):
	f = open(filename, 'r')
	d = f.read()
	data = d.split('\n')
	return data

# printDataset()
def print_list(input_list):
	print('\n'.join(map(str, input_list)))

dataset = load_csv('data/sample.csv')
tagset = load_csv('data/tags.csv')

print_list(tagset)
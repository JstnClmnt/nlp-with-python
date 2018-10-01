#############################################################
# This python code just splits the stories into	            #
# sentences and displays the total number of sentences hehe	#		
#############################################################
import re
import csv

new_list, story_list = [], []

# this part retrieves the dataset
f = open('tagalog-short-stories-clean.csv', 'r')
d = f.read()
raw_data = d.split('\n')

# splits the stories separately
for row in raw_data:
	data_list = row.split(',')
	new_list.append(data_list)

# converts the list to string (bc string inaaccept nung function below)
# IMPORTANT: change index of new_list[i] depending on the story 
#     		 to be segmented into sentences
string_list = " ".join(map(str, new_list[35]))

# this function splits the story into sentences
def split_to_sentences(story):
	terminal_points = re.compile('[.!?]')
	sentence_list = terminal_points.split(story)
	return sentence_list

splitted_story = split_to_sentences(string_list)

# IMPORTANT: change file name per story
csv_file = "Ang Tulay na Kahoy.csv"

# Writes the output to a CSV file
with open(csv_file, 'w') as output:
	writer = csv.writer(output, lineterminator='\n')
	for row in splitted_story:
		writer.writerow([row])
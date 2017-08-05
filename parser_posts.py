from xml.etree.ElementTree import iterparse
from collections import Counter
from tqdm import tqdm
import re


def parse_and_remove(filename):
    doc = iterparse(filename, ('start', 'end'))

    # get the root element
    event, root = next(doc)
    
    tag = 'row'
    
    for event, elem in doc:
        if event == 'end' and elem.tag == 'row':
            yield elem.attrib
            # for garbage collection
            elem.clear()
            root.clear()
				



def get_tags_counter(max_counter= None):
	tag_generator = parse_and_remove('Posts.xml')

	tags_counter = Counter()

	for index, row_dict in tqdm(enumerate(tag_generator)):
		if 'Tags' in row_dict:
			tag_list = re.split("<(.*?)>", row_dict['Tags'])
			tag_list = [tag for tag in tag_list if tag]

			for tag in tag_list:
				tags_counter[tag] +=1

		if index == max_counter and max_counter:
			break

	return tags_counter


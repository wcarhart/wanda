"""
Generate index.html based on a content file
"""
import argparse
import os
import sys

class Card:
	def __init__(self, title, date, location, img, alt, content, is_month):
		self.title = title
		self.date = date
		self.location = location
		self.img = img
		self.alt = alt
		self.content = content
		self.is_month = is_month

def import_content_file(content_file):
	assert os.isfile(content_file)
	with open(content_file, 'r') as f:
		lines = f.readlines()
	return [line for line in lines if not line[0] == '#']

def parse_cards(lines):
	cards = []
	title = date = location = img = alt = is_month = ''
	content = []

	while True:
		# check for exit condition
		if len(lines) == 0:
			if not all([title, date, location, img, alt, content, is_month]):
				raise ValueError(f"Invalid card: incomplete card detected in content file")
			break

		# get next item
		next_item = lines.pop(0)
		if next_item == '':
			continue

		# get key value pairs
		key = next_item.split(':')[0]
		value = ':'.join(next_item.split(':')[1:]).lstrip()

		# build up card
		if key == 'title':
			if title:
				raise ValueError(f"Invalid card: title is defined more than once in card {len(cards)+1} ('{title}' and '{key}')")
			title = value
		elif key == 'date':
			if date:
				raise ValueError(f"Invalid card: date is defined more than once in card {len(cards)+1} ('{date}' and '{key}')")
			date = value
		elif key == 'location':
			if location:
				raise ValueError(f"Invalid card: location is defined more than once in card {len(cards)+1} ('{location}' and '{key}')")
			location = value
		elif key == 'img':
			if img:
				raise ValueError(f"Invalid card: img is defined more than once in card {len(cards)+1} ('{img}' and '{key}')")
			img = value
		elif key == 'alt':
			if alt:
				raise ValueError(f"Invalid card: alt is defined more than once in card {len(cards)+1} ('{alt}' and '{key}')")
			alt = value
		elif key == 'content':
			if content:
				raise ValueError(f"Invalid card: content is defined more than once in card {len(cards)+1} ('{content}' and '{key}')")
			content.append(value)
		elif key == 'is_month':
			if is_month:
				raise ValueError(f"Invalid card: is_month is defined more than once in card {len(cards)+1} ('{is_month}' and '{key}')")
			if value.lower() == 'true':
				is_month = True
			elif value.lower() == 'false':
				is_month = False
			else:
				raise ValueError(f"Invalid card: is_month must be true or false (found '{value}' in card {len(cards)+1})")
		else:
			raise ValueError(f"Invalid card: invalid key found in content file for card {len(cards)+1}: '{key}'")

		# if card is good, add it to the pile
		if all([title, date, location, img, alt, content, is_month]):
			c = Card(title, date, location, img, alt, content, is_month)
			cards.append(c)
			title = date = location = img = alt = is_month = ''
			content = []

	return cards

def build_parser():
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('content_file', type=str, required=True, help="the content file")
	return parser

def main():
	parser = build_parser
	args = parser.parse_args()

	file_contents = import_content_file(args.content_file)
	cards = parse_cards(file_contents)

if '__name__' == '__main__':
	main()
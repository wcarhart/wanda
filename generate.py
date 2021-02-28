"""
Generate index.html based on a content file
"""
import argparse
import datetime
import os

# HTML templates
top = f"""
<!DOCTYPE html>
<!-- This is an autogenerated file - DO NOT EDIT DIRECTLY -->
<!-- This file was generated on {str(datetime.datetime.now())} by <<<CONTENTSOURCE>>> via generate.py in Wanda -->
<!-- Wanda repository: https://github.com/wcarhart/wanda -->
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Alexx and Will</title>
	<meta name="description" content="Alexx and Will">
	<meta name="twitter:card" value="summary">
	<meta property="og:title" content="Alexx and Will" />
	<meta property="og:image" content="img/favicon-32x32.png" />
	<meta property="og:description" content="Alexx and Will">

	<!-- Bootstrap CDN -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

	<!-- static CSS -->
	<link rel="stylesheet" href="css/style.css">
	<link rel="stylesheet" href="css/animate.css">
	<link rel="stylesheet" href="css/waypoints.css">

	<!-- icons -->
	<link rel="apple-touch-icon" sizes="180x180" href="ico/apple-touch-icon.png">
	<link rel="icon" type="image/png" sizes="32x32" href="ico/favicon-32x32.png">
	<link rel="icon" type="image/png" sizes="16x16" href="ico/favicon-16x16.png">
	<link rel="manifest" href="ico/site.webmanifest">

	<!-- Bootstrap to make page load faster -->
	<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</head>

<!-- Love you, Alexx 👻🐛❤️ -->

<body>
	<div class="container-fluid intro">
		<div class="container">
			<div class="narrow">
				<h1>Hi there!</h1>
				<p class="lead">Welcome to <code>wanda</code>!</p>
				<p class="lead">In December 2019, I wanted to give my girlfriend more than just a standard Christmas card. Being the strapping young software engineer I was, I decided to make her a virtual Christmas card that would capture the memories from our relationship so far. The result was alexxandwill.us, dubbed the codename <code>wanda</code>, short for <i>Will and Alexx</i>, to keep the project under wraps until it was ready.</p>
				<p class="lead">What started as a Christmas card with a few dates has blossomed into a fun, interactive way for me and Alexx to look document our adventures. I can't wait to keep adding to the memories.</p>
				<p class="lead">Love you, Alexx.</p>
				<p class="lead">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Will</p>
				<div class="mobile-credits">
					<div class="row text-center justify-content-center">
						<a href="https://github.com/wcarhart" target="_blank" class="socket"><i class="fab fa-github" data-fa-transform="grow-8 down-1"></i></a>
						<a href="https://www.willcarh.art" target="_blank" class="socket"><img id="logo" src="img/willcarhartportfolio.png" alt="willcarh.art logo"></a>
						<a href="https://www.linkedin.com/in/willcarhart/" target="_blank" class="socket"><i class="fab fa-linkedin" data-fa-transform="down-3 right-1.9 grow-6"></i></a>
					</div>
					<div class="row text-center justify-content-center">
						<p class="lead">&copy;&nbsp; Will Carhart & Alexx O'Boyle 2020</p>
					</div>
				</div>
			</div>
		</div>
	</div>

	<div class="container-fluid mobile">
		<div class="container">
			<div class="narrow">
				<div class="timeline">
"""

middle = f"""
				</div>
			</div>
		</div>
	</div>
	<div class="container-fluid non-mobile">
		<div class="container">
			<div class="narrow">
				<div class="timeline">
"""

bottom = f"""
				</div>
			</div>
		</div>
		<script src="https://use.fontawesome.com/releases/v5.5.0/js/all.js"></script>
		<script src="js/jquery.waypoints.min.js"></script>
		<script src="js/waypoints.js"></script>
	</div>

	<div class="os-animation container-fluid outro non-mobile" data-animation="fadeInUp">
		<div class="container">
			<div class="narrow text-center">
				<p class="lead">&copy;&nbsp; Will Carhart & Alexx O'Boyle 2020</p>
				<a href="https://github.com/wcarhart" target="_blank" class="socket"><i class="fab fa-github" data-fa-transform="grow-8 down-1"></i></a>
				<a href="https://www.willcarh.art" target="_blank" class="socket"><img id="logo" src="img/willcarhartportfolio.png" alt="willcarh.art logo"></a>
				<a href="https://www.linkedin.com/in/willcarhart/" target="_blank" class="socket"><i class="fab fa-linkedin" data-fa-transform="down-3 right-1.9 grow-6"></i></a>
			</div>
		</div>
	</div>

</body>
</html>
"""

class Card:
	def __init__(self, title, date, location, img, alt, content, is_month):
		self.title = title
		self.date = date
		self.location = location
		self.img = img
		self.alt = alt
		self.content = content
		self.is_month = is_month

	def __repr__(self):
		return f"{{Card, title: '{self.title}', date: '{self.date}', location: '{self.location}', img: '{self.img}', alt: '{self.alt}', content: '{self.content}', is_month: '{self.is_month}'}}"

	def __str__(self):
		return f"{{Card, title: '{self.title}', date: '{self.date}', location: '{self.location}', img: '{self.img}', alt: '{self.alt}', content: '{self.content}', is_month: '{self.is_month}'}}"

def import_content_file(content_file):
	assert os.path.isfile(content_file)
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
			if not any([title, date, location, img, alt, content, not is_month]):
				raise ValueError(f"Invalid card: incomplete card detected at end of content file")
			break

		# get next item
		next_item = lines.pop(0)
		if next_item == '' or next_item == '\n':
			continue

		# get key value pairs
		key = next_item.split(':')[0]
		value = ':'.join(next_item.split(':')[1:]).lstrip().rstrip('\n')

		# build up card
		if key == 'title':
			if title:
				raise ValueError(f"Invalid card: title is defined more than once in card {len(cards)+1} ('{title}' and '{value}')")
			title = value
		elif key == 'date':
			if date:
				raise ValueError(f"Invalid card: date is defined more than once in card {len(cards)+1} ('{date}' and '{value}')")
			date = value
		elif key == 'location':
			if location:
				raise ValueError(f"Invalid card: location is defined more than once in card {len(cards)+1} ('{location}' and '{value}')")
			location = value
		elif key == 'img':
			if img:
				raise ValueError(f"Invalid card: img is defined more than once in card {len(cards)+1} ('{img}' and '{value}')")
			img = value
		elif key == 'alt':
			if alt:
				raise ValueError(f"Invalid card: alt is defined more than once in card {len(cards)+1} ('{alt}' and '{value}')")
			alt = value
		elif key == 'content':
			content.append(value)
		elif key == 'is_month':
			if is_month:
				raise ValueError(f"Invalid card: is_month is defined more than once in card {len(cards)+1} ('{is_month}' and '{value}')")
			if value.lower() == 'true':
				is_month = True
			elif value.lower() == 'false':
				is_month = False
			else:
				raise ValueError(f"Invalid card: is_month must be true or false (found '{value}' in card {len(cards)+1})")
		else:
			raise ValueError(f"Invalid card: invalid key found in content file for card {len(cards)+1}: '{key}'")

		# if card is good, add it to the pile
		if is_month or (not title == '' and not date == '' and not location == '' and not img == '' and not alt == '' and not len(content) == 0 and not is_month == ''):
			c = Card(title, date, location, img, alt, content, is_month)
			cards.append(c)
			title = date = location = img = alt = is_month = ''
			content = []

	return cards

def build_html(cards):
	mobile_html = ''
	non_mobile_html = ''
	side = 'left'

	for card in cards:
		generated_content = '<p>' + '</p>\n									<p>'.join(card.content) + '</p>'
		if card.is_month:
			inner_html = f"""
								<div class="card-body">
									<h4>{card.title}</h4>
								</div>
			"""
			mobile_template = f"""
					<div class="row timeline-row">
						<div class="col d-flex justify-content-center mobile-card">
							<div class="card text-center justify-content-center mobile-month-card">{inner_html}				</div>
						</div>
					</div>
			"""
			if side == 'left':
				non_mobile_template = f"""
					<div class="row timeline-row">
						<div class="col-5 left-timeline-item os-animation" data-animation="fadeInUp">
							<div class="card text-center">{inner_html}				</div>
						</div>
						<div class="col-2 center-timeline-item"><div class="vertical"></div>&nbsp;</div>
						<div class="col-5 right-timeline-item os-animation" data-animation="fadeInUp"></div>
					</div>
				"""
			else:
				non_mobile_template = f"""
					<div class="row timeline-row">
						<div class="col-5 left-timeline-item os-animation" data-animation="fadeInUp"></div>
						<div class="col-2 center-timeline-item"><div class="vertical"></div>&nbsp;</div>
						<div class="col-5 right-timeline-item os-animation" data-animation="fadeInUp">
							<div class="card text-center">{inner_html}				</div>
						</div>
					</div>
				"""
		else:
			inner_html = f"""
							<div class="card">
								<img src="{card.img}" class="card-img-top" alt="{card.alt}">
								<div class="card-body">
									<h4 class="card-title">{card.title}</h4>
									<h6 class="card-subtitle text-muted">{card.date}</h6>
									<hr>
									{generated_content}
									<p class="card-text text-center"><small class="text-muted">{card.location}</small></p>
								</div>
							</div>
			"""
			mobile_template = f"""
					<div class="row timeline-row">
						<div class="col d-flex justify-content-center mobile-card">{inner_html}			</div>
					</div>
			"""
			if side == 'left':
				non_mobile_template = f"""
					<div class="row timeline-row">
						<div class="col-5 left-timeline-item os-animation" data-animation="fadeInUp">{inner_html}			</div>
						<div class="col-2 center-timeline-item"><div class="vertical"></div>&nbsp;</div>
						<div class="col-5 right-timeline-item os-animation" data-animation="fadeInUp"></div>
					</div>
				"""
			else:
				non_mobile_template = f"""
					<div class="row timeline-row">
						<div class="col-5 left-timeline-item os-animation" data-animation="fadeInUp"></div>
						<div class="col-2 center-timeline-item"><div class="vertical"></div>&nbsp;</div>
						<div class="col-5 right-timeline-item os-animation" data-animation="fadeInUp">{inner_html}			</div>
					</div>
				"""

		side = 'right' if side == 'left' else 'left'
		mobile_html += mobile_template
		non_mobile_html += non_mobile_template

	final_html = top + mobile_html + middle + non_mobile_html + bottom
	return final_html

def build_parser():
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('content_file', type=str, nargs='?', default='content.md', help="the content markdown file")
	parser.add_argument('-o', '--output', type=str, required=False, default='index.html', help="the output HTML file")
	return parser

def main():
	parser = build_parser()
	args = parser.parse_args()

	file_contents = import_content_file(args.content_file)
	cards = parse_cards(file_contents)
	html = build_html(cards)

	html = html.replace('<<<CONTENTSOURCE>>>', args.content_file)

	with open(args.output, 'w+') as f:
		f.write(html)

	print(f'HTML written to {args.output}')

if __name__ == '__main__':
	main()

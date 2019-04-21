# PepnoScrape
import sys
import argparse
import requests
from bs4 import BeautifulSoup
from stanford_nlp import Stanfordnlp
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

def main(**kwargs):
	sf = Stanfordnlp()
	#sf.make_story([[("Where is the US president"),("The white house")]])
	story = []

	# main loop 
	while(True):
		user_q = str(input("What is your question? "))
		if user_q == "quit":
			break
		if user_q == "make story":
			sf.make_story(story)
			pass

		def makeUrl(keyword):
		    replaced = keyword.replace(" ", "+")
		    return("https://www.google.com/search?client=firefox-b-d&q=" + replaced)

		def strip(striptext):
			return (striptext.replace('Dochter','')
							 .replace('Moeder','')
							 .replace('Vader','')
							 .replace('Zoon',''))

		url = makeUrl(user_q)
		r = requests.get(url, headers=headers)
		soup = BeautifulSoup(r.text, 'lxml')

		# first result
		result = soup.find('div', class_='Z0LcW')

		multiple = False
		if "are" in user_q:
			multiple = True
		# if "are" in the question extract list
		try:
			if result == None:
				if multiple == True:
					for classes in soup.find_all('div', attrs={'class': 'lzmqLb'}):
						if classes.find('div', attrs={'class': 'wfg6Pb'}):
							print(strip(classes.text))
					for classes in soup.find_all('div', attrs={'class': 'IAznY'}):
						if classes.find('div', attrs={'class': 'title'}):
							print(strip(classes.text))
				elif multiple == False:
					result = soup.find('div', class_='title')
			if result == None:
				result = soup.find('div', class_='RJn8N xXEKkb ellip')
			if result == None:
				result = soup.find(class_='LGOjhe')
			if result == None:
				result = soup.find('h3', class_='bNg8Rb').parent.find("span")
			if result == None:
				result = soup.find('h3', class_='LC20lb') # wikipedia

			if multiple == False:
				print(result.text)
			story.append((user_q, result.text))
		except:
			print("Please formulate your question in a simpler way.")

	sf.make_story(story)
	# Place stanford anaphora parser here
	exit()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'QA with focus on anaphoric relations')
	args = parser.parse_args()

	main(*vars(args))

#if (ent[0] == ent[0].lower().capitalize()) or (ent[0][ent[0].find(" ")+1:] == ent[0].lower().capitalize()):
#	if ent[0] in open('all_surnames.txt', encoding="utf8").read():
#		ent = (ent[0], "PERSON")
# if nltk.word_tokenize(ent[0])[-1] == nltk.word_tokenize(ent[0].lower().capitalize())[-1]:
# 	if ent[0] in open('all_surnames.txt', encoding="utf8").read():
# 		ent = (ent[0], "PERSON")
# if entity.gender and entity.gender[0]:
# 	if (anaphor in female) and (entity.gender[0] == 'female'):
# 		prob = p.sim(an_context, entity.summary) + 0.2
# else:
# 	prob = p.sim(an_context, entity.summary)

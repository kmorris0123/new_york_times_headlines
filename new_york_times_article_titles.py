import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os


def choose_section():
	#this is where the user will choose which section's headlines they want to print.
	print("What section do you want the titles from?")
	print("Section choices: world, us, politics, ny, business day, opinion, techology, science, health, sports, books, style, food, travel, magazine, t magazine, real estate.")
	return input("--> ").replace(" ","")


def options(usr_choose):
	#this function takes the user selection from the choose_section function and will return the url of the choosen website page.
	return {
				'world': 'https://www.nytimes.com/section/world',
				'us': 'https://www.nytimes.com/section/us',
				'politics': 'https://www.nytimes.com/section/politics',
				'ny': 'https://www.nytimes.com/section/nyregion',
				'businessday': 'https://www.nytimes.com/section/business',
				'opinion': 'https://www.nytimes.com/section/opinion',
				'technology': 'https://www.nytimes.com/section/technology',
				'science': 'https://www.nytimes.com/section/science',
				'health': 'https://www.nytimes.com/section/health',
				'sports' :'https://www.nytimes.com/section/sports',
				'health': 'https://www.nytimes.com/section/arts',
				'books': 'https://www.nytimes.com/section/books',
				'style': 'https://www.nytimes.com/section/fashion',
				'food': 'https://www.nytimes.com/section/food',
				'travel': 'https://www.nytimes.com/section/travel',
				'magazine': 'https://www.nytimes.com/section/magazine',
				'tmagazine': 'https://www.nytimes.com/section/t-magazine',
				'realestate': 'https://www.nytimes.com/section/realestate'
	}.get(usr_choose)

	


def req(section):
	#this function uses beautiful soup to get the headlines
	url = section
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html,'lxml')

	count = 0
	for story_heading in soup.find_all(class_="headline"): 
		if story_heading.a: 
			count += 1
			print(str(count)+". "+story_heading.a.text.replace("\n", " ").strip())
		else:
			count += 1
			print(str(count)+". "+story_heading.contents[0].strip())


def main():


	play = True
	print("This will print all of the story headings from a section of the New York Times website.")
	while play == True:
	
		cs = choose_section()
		op = options(cs)
		req(op)

		play_again = input('Do you want to find headlines of another section? "Yes" or "No": ')

		if play_again == "yes":
			play = True
			os.system('clear')
		else:

			play = False


if __name__ == '__main__':
	main()
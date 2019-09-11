from bs4 import BeautifulSoup
import requests
import csv
#To scrape from a file

with open('games.html') as html_file:
    soupfile = BeautifulSoup(html_file,'lxml')



 #  To scrape from a website:
#source = requests.get('http://improvencyclopedia.org/games/index.html').text
#soup = BeautifulSoup(source, 'lxml')

#   To create an html file from scrape
#    f = open('games.html','w+')
#    f.write(str(soup))

all_links = []
for links in soupfile.find_all('a'):
    links = links['href']
    all_links.extend([links])

#test array
two_links_test = ['http://improvencyclopedia.org/games//10_Fingers.html','http://improvencyclopedia.org/games//3_Lines.html']

#creates a csv file to store data in
games_db = open('games_db.csv','w+')

#creates a csv_writer to pass data into file
csv_writer = csv.writer(games_db)

#writes headers of CSV file
csv_writer.writerow(['Title','Description','Categories'])
for address in all_links:
    source = requests.get(address).text
    soup = BeautifulSoup(source, 'lxml')
    title = soup.find(class_='body_title').h3.text
    categories = soup.find(class_='linklist').ul.text
    description = soup.find(class_='details').text.split('\n',8)[8].replace('\n','')
    print(description)
    #passes the data into the csv file in each itteration
    csv_writer.writerow([title,description,categories])
#closes the file
games_db.close()
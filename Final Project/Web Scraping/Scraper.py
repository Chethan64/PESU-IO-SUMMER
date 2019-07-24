#This program scrapes each link from assignment.html, then opens the link 
#to scrape data from the link and stores all the data in a single .csv file 
#Executing this program once will store data of 49 cities in a single .csv file 



import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://karki23.github.io/Weather-Data/assignment.html")
bsObj = BeautifulSoup(html,"lxml")
ul = bsObj.findAll("ul")[0]
li = ul.findAll("li")
csvfile = open('LinksMaster.csv','w+',newline='')
writer = csv.writer(csvfile)

lin = []

for link in bsObj.findAll('a'):
    lin.append(link.get('href'))



for i in lin:
	link = "https://karki23.github.io/Weather-Data/" + i
	html = urlopen(link)
	bsObj1 = BeautifulSoup(html,"lxml")
	table = bsObj1.findAll("table")[0]
	rows = table.findAll("tr")
	csvfile1 = open('7.csv','a',newline='')
	writer1 = csv.writer(csvfile1)
	try:
		for row in rows:
			csvRow = []
			for cell in row.findAll(['td','th']):
				csvRow.append(cell.getText())
			writer1.writerow(csvRow)
	finally:
		csvfile1.close()

csvfile.close()
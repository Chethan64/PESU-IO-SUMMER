#This program scrapes the data from only one link and stores it in a .csv file

#Executing this program once will store the data of a single city in a .csv file
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://karki23.github.io/Weather-Data/Moree.html")
bsObj = BeautifulSoup(html,"lxml")
table = bsObj.findAll("table")[0]
rows = table.findAll("tr")
csvfile = open('5.csv','w+',newline='')
writer = csv.writer(csvfile)
try:
	for row in rows:
		csvRow = []
		for cell in row.findAll(['td','th']):
			csvRow.append(cell.getText())
		writer.writerow(csvRow)
finally:
	csvfile.close()
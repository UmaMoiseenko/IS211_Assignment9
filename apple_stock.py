from bs4 import BeautifulSoup
from urllib2 import urlopen

soup = BeautifulSoup (urlopen("http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"))
dates = soup.findAll('table', attrs={'class': 'yfnc_datamodoutline1'})[0].findAll('table')[0].findAll('tr')
counter = 0

for date in dates:
	counter +=1

	date = dates[counter].findAll('td')

	if len(date) > 1:
		print date[0].contents[0]

		if len(date) > 2:
			print ' Close Price: ', date[4].contents[0]

	else:
		break


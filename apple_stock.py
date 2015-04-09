from bs4 import BeautifulSoup
from urllib2 import urlopen

soup = BeautifulSoup (urlopen("http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices"))
dates = soup.findAll('table', attrs={'class': 'yfnc_datamodoutline1'})[0].findAll('table')[0].findAll('tr')
counter = 0


for date in dates:
	counter +=1

	date_length = dates[counter].findAll('td')

	if len(date_length) > 1:
		print dates[counter].findAll('td', attrs={'class': 'yfnc_tabledata1', 'align': 'right'})[0].contents[0]

		if len(date_length) > 2:
			print ' Close Price: ', dates[counter].findAll('td', attrs={'class': 'yfnc_tabledata1', 'align': 'right'})[4].contents[0]

	else:
		break


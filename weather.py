from bs4 import BeautifulSoup
from urllib2 import urlopen

soup = BeautifulSoup (urlopen("http://www.wunderground.com/history/airport/KNYC/2015/4/8/MonthlyCalendar.html"))
calendar = soup.finAll('td', attrs={'class': 'day'});

for day in calendar:

	day_num = day.findAll('a', attrs={'class': 'dateText'})[0].contents[0]
	title = day.findAll('td', attrs={'class': 'value-header'})[0].contents[0]
	temp = day.findAll('td', attrs={'class': 'highLow'})[0]

	if (title == 'Actual:'):
		temp_high = temp.findAll('span')[1].contents[0]
		temp_low = temp.findAll('span')[3].contents[0]

	elif (title == 'Forecast:'):
		temp_high = temp.findAll('span')[0].contents[0]
		temp_low = temp.findAll('span')[1].contents[0]
	else:
		break

	print day_num
	print title, temp_high, ' | ', temp_low
	print ' -------------------'



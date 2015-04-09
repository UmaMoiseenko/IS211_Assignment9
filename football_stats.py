from bs4 import BeautifulSoup
from urllib2 import urlopen

soup = BeautifulSoup (urlopen("http://www.cbssports.com/nfl/stats/playersort/nfl/year-2014-season-post-category-touchdowns"))
players = soup.findAll('table', attrs={'class': 'data'})[0].findAll('tr', attrs={'valign': 'top'})

counter = 0


for player in players:
    counter +=1
    name = player.findAll('td')[0].findAll('a')[0].contents[0]
    pos = player.findAll('td')[1].contents[0]
    team = player.findAll('td')[2].findAll('a')[0].contents[0]
    td = player.findAll('td')[6].contents[0]

    print "#%s %s Position: %s, Team: %s, TD: %s" % (counter, name, pos, team, td)

    if counter == 20:
        break


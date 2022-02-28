# colemcph 2021 - scrapping and graph personal project
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
result = requests.get('https://www.imdb.com/chart/tvmeter/?sort=rk,asc&mode=simple&page=1')
# a result of 200 means the status is OK to access, no 404 errors.
print(result.status_code)
source = result.content
soup = BeautifulSoup(source, 'lxml')
titles = []
#finds all td tags, then all a tags, then gets the text representing the link AKA the title of the show. and appends them to a titles list.
for td_tag in soup.find_all('td'):
    for a in td_tag.find_all('a'):
        if not (isinstance(a.get_text(), type(None))):
            title = a.get_text()
            title = title.rstrip("\n")
            if len(title) > 1:
                titles.append(title)

#  doing the same for ratings
ratings = []
for td_tag in soup.find_all('td'):
    for strong in td_tag.find_all('strong'):
        if not (isinstance(strong.get_text(), type(None))):
            rating = strong.get_text()
            rating = rating.rstrip("\n")
            if len(rating) > 1:
                ratings.append(rating)
for i in range(len(ratings)):
    ratings[i] = float(ratings[i])

# only including titles with ratings
titles = titles[:len(ratings)]
sliced = input('how many results would you like to be displayed ? ' + " max : " + str(len(ratings)) + ' min :  1' )
xpoints = np.array(titles[:int(sliced)])
ypoints = np.array(ratings[:int(sliced)])
plt.plot(xpoints,ypoints)

plt.show()
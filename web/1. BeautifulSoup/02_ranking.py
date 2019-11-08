import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())

tags = soup.findAll('div', attrs={'class':'tit3'} )
up_town = soup.find('img', attrs={'src':'http://imgmovie.naver.net/2007/img/common/icon_na_1.gif'})

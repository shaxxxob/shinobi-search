results = []
page = requests.get('https://search17.lycos.com/web/?q='+query).text
soup = BeautifulSoup(page,'lxml')
listings = soup.find_all(class_="result-item")
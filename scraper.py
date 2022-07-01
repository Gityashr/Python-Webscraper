from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')
csv_file = open('scraper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'youtube link'])
for article in soup.find_all('article'):
    #print(article.prettify())
    headline = article.h2.a.text #h2 actually not needed here, since it's the first sub tag in article
    print(headline)
    print()
    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    print()

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # print(vid_src)

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # print(vid_id)

        yt_link = 'https://www.youtube.com/watch?v={}'.format(vid_id)
    except Exception as e:
        yt_link = 'No YouTube link here'

    print(yt_link)

    print('\n')

    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()
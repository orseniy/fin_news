# fin_news
Yahoo Finance News  Spider

Spider for getting a headline and a link to the news from the news block about the company at finance.yahoo.com
Working does not include processing javascript part

Launching a spider using the console
scrapy crawl Latest_News -o %company_name%_data.csv
Also need use correct link in spider "start_urls" field

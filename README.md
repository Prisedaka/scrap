# Scrap

## Install

Use Python 3.8 and install these dependences:

```
$ sudo apt-get install python3.8 python3.8-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

Create virtual environment:

```
$ python3.8 -m venv env
```

Activate virtual environment:

linux

```
$ source env/bin/activate
```

windows

```
$ env/Scripts/activate.bat
```

Install Scrapy:

```
$ pip install Scrapy
```

## Scrapy frameworks docs
https://docs.scrapy.org/en/latest/index.html

## Start spider to parse main page of severotek.ru and save results to json file

Save text data in tags h1, h2, h3, p.

```
$ cd ./scrap/product_scraper
$ scrapy crawl severotek -o output.json
```

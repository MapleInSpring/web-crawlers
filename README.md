Web Scrapper

### Background
The motivation for this project is
Who are our competitors
What product/services are they selling?
Who are their customers?

Steps:

1. render page in JS with splash
2. get first partner
3. click first partner
4. get website url for first partner
5. get website url for all partners
6. follow link to each partner
7. get product and services for each partner


Get all the partners
Get the website link for partners
For each partner get the product and services

Massage the result into

[
  {
	"name": "partner",
	"url": "http://...",
	"products": [""],
	"services": [""]
  }
]

scrapy shell 'http://localhost:8050/render.html?url=https://kubernetes.io/partners/#kcsp'


### Render JS page with Splash

Run splash locally
- `docker pull scrapinghub/splash`
- `docker run -p 8050:8050 scrapinghub/splash`

[Run scrapy shell with splash](https://stackoverflow.com/questions/35352423/scrapy-shell-and-scrapy-splash)

### Managing local python environment and packages with Conda
[Conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

[Recreate conda environment](https://stackoverflow.com/questions/18640305/how-do-i-keep-track-of-pip-installed-packages-in-an-anaconda-conda-environment)

- `conda env export -n webscrapper > environment.yml`
- `conda env create -f environment.yml`

### Other ways to render JS pages
[Selenium python](https://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php)

[PhantomJS](http://phantomjs.org/api/webpage/method/render.html)



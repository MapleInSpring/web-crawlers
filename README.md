

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



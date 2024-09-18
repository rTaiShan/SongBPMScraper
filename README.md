# SongBPM Scraper
Scraper for the songbpm.com using lxml and xpaths.

## Usage
After installing dependencies (see `requirements.txt`) for the (optionally virtual) environment, the program may be then executed in two ways:

```sh
# Without arguments, prompting the user for the search string
python main.py 

# With the search string present
python main.py <search string>

# For instance
python main.py Rick Astley
```

## Disclaimer
This program depends heavily on the layout of songbpm.com and **minor** changes on the site **may break this completely**.

# PbScraper
A python script to scrape Photobucket for public albums with public facing photos


Requries: BeautifulSoup4 (install via pip)

usage: PbScraper.py [-h] [--username USERNAME] [--startnum STARTNUM] [--endnum ENDNUM]

optional arguments:
  -h, --help           show this help message and exit
  --username USERNAME  Username you are scraping with.
  --startnum STARTNUM  Appended number starts at this integer.
  --endnum ENDNUM      Appended number ends at this integer.
  
  
  Simply execute like so: python .\PbScraper.py --username ellie --startnum 1 --endnum 9999
  
  This will cycle through each number and post the results of the scrape. 

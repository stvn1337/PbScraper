# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--username", help="Username you are scraping with.",type=str)
parser.add_argument("--startnum", help="Appended number starts at this integer.",type=int)
parser.add_argument("--endnum", help="Appended number ends at this integer.",type=int)
args = parser.parse_args()

username = args.username if args.username is not None else "ellie"
start_index = args.startnum if args.username is not None else 1
end_index = args.endnum if args.username is not None else 9999



def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def GetThisURL(path, currentint):
    return "http://photobucket.com/user/"+path+str(currentint)+"/library"

for test in range(start_index,end_index):
    holder = GetThisURL(username, test)
    try:
        #print(holder)
        page = urllib2.urlopen(holder)
        soup = BeautifulSoup(page, 'html.parser')
        count_box = soup.find('span', attrs={'class': 'mediaCount'})
        thecount = int(find_between(str(count_box),"(",")"))
        if thecount != "" and thecount > 0:
            print(holder,":",str(thecount))
    except:
        pass
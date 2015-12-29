#! /usr/bin/ev python

"""codeIn1.py: Scrapes bible.is to generate a list of Bible English chapters with corresponding chapters in a language of choice by the user"""

__author__ = "Diana Chang"
__email__ = "diana.chang.twn@gmail.com"
__status__ = "Development"

import argparse
from lxml import html
import codecs
import re
import requests
import ast
from xml.sax.saxutils import unescape
chapters = {"Gen":50,"Exod":40,"Lev":27,"Num":36,"Deut":34,"Josh":24,"Judg":21,"Ruth":4,"1Sam":31,"2Sam":24,"1Kgs":22,"2Kgs":25,"1Chr":29,"2Chr":36,"Ezra":10,"Neh":13,"Esth":10,"Job":42,"Ps":150,"Prov":31,"Eccl":12,"Song":8,"Isa":66,"Jer":52,"Lam":5,"Ezek":48,"Dan":12,"Hos":14,"Joel":3,"Amos":9,"Obad":1,"Jonah":4,"Mic":7,"Nah":3,"Hab":3,"Zeph":3,"Hag":2,"Zech":14,"Mal":4,"Matt":28,"Mark":16,"Luke":24,"John":21,"Acts":28,"Rom":16,"1Cor":16,"2Cor":13,"Gal":6,"Eph":6,"Eph":6,"Phil":4,"Col":4,"1Thess":5,"2Thess":3,"1Tim":6,"2Tim":4,"Titus":3,"Phlm":1,"Heb":13,"Jas":5,"1Pet":5,"2Pet":3,"1John":5,"2John":1,"3John":1,"Jude":1,"Rev":22}
file_name=''
args = 0
parser = argparse.ArgumentParser()
parser.add_argument('--outfile', action="store")
parser.add_argument('code', action="store")
args = parser.parse_args()

def main(LANG):
    ENGpage = requests.get('http://www.bible.is/ENGEVD/Matt/3/D')
    LANGpage = requests.get('http://www.bible.is/'+LANG+'/Matt/4/D')
    ENGdata = html.fromstring(ENGpage.content)
    LANGdata = html.fromstring(LANGpage.content)
    ENGtext = ENGdata.text_content()
    LANGtext = LANGdata.text_content()
    ENGlist = ENGtext[ENGtext.find('bookList')+13:ENGtext.find('var canonicalUrl')-7]
    LANGlist = LANGtext[LANGtext.find('bookList')+13:LANGtext.find('var canonicalUrl')-7]
    ENGlist = ENGlist.split("},{")
    LANGlist = LANGlist.split("},{")
    ENGkeys = []
    LANGkeys = []
    for i in range(len(ENGlist)):
        part1 = ENGlist[i][6:ENGlist[i].find(',')-1]
        part2 = ENGlist[i][ENGlist[i].find(',')+9:-1]
        ENGkeys.append([part1,part2])
    for i in range(len(LANGlist)):
        part1 = LANGlist[i][6:LANGlist[i].find(',')-1]
        part2 = str(LANGlist[i][LANGlist[i].find(',')+9:-1])
        LANGkeys.append([part1,part2])
    if (args.outfile!=None):
        outf = codecs.open(args.outfile,"w+",'utf-8')
        for i in range(len(ENGkeys)):
            for j in range(chapters[ENGkeys[i][0]]):
                neww = "".join([chr( int(re.sub('u', '0x', result), 16) ) for result in re.findall('u[0-9a-f]{4}', str(LANGkeys[i][1]))])
                outf.write(ENGkeys[i][1]+" "+str(j+1)+", "+neww+" "+str(j+1)+"\n")
        outf.close()
    else:
        for i in range(len(ENGkeys)):
            for j in range(chapters[ENGkeys[i][0]]):
                neww = "".join([chr( int(re.sub('u', '0x', result), 16) ) for result in re.findall('u[0-9a-f]{4}', str(LANGkeys[i][1]))])
                print(ENGkeys[i][1]+" "+str(j+1)+", "+neww+" "+str(j+1)+"\n")
main(args.code)

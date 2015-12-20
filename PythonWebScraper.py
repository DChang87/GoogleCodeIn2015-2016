#SELECT YOUR LANGUAGE BY EDITING THE LANG VARIABLE
import codecs
import requests
import bs4
chapters = {"Gen":50,"Exod":40,"Lev":27,"Num":36,"Deut":34,"Josh":24,"Judg":21,"Ruth":4,"1Sam":31,"2Sam":24,"1Kgs":22,"2Kgs":25,"1Chr":29,"2Chr":36,"Ezra":10,"Neh":13,"Esth":10,"Job":42,"Ps":150,"Prov":31,"Eccl":12,"Song":8,"Isa":66,"Jer":52,"Lam":5,"Ezek":48,"Dan":12,"Hos":14,"Joel":3,"Amos":9,"Obad":1,"Jonah":4,"Mic":7,"Nah":3,"Hab":3,"Zeph":3,"Hag":2,"Zech":14,"Mal":4,"Matt":28,"Mark":16,"Luke":24,"John":21,"Acts":28,"Rom":16,"1Cor":16,"2Cor":13,"Gal":6,"Eph":6,"Eph":6,"Phil":4,"Col":4,"1Thess":5,"2Thess":3,"1Tim":6,"2Tim":4,"Titus":3,"Phlm":1,"Heb":13,"Jas":5,"1Pet":5,"2Pet":3,"1John":5,"2John":1,"3John":1,"Jude":1,"Rev":22}
def main():
    ENGpage = requests.get('http://www.bible.is/ENGEVD/Matt/3/D')
    ##################
    #EDIT THIS VARIABLE TO CHANGE LANGUAGE
    LANG = 'BULB40'
    #######################
    ENGdata = bs4.BeautifulSoup(ENGpage.text,"lxml")
    ENGtext = ENGdata.get_text()
    ENGlist = ENGtext[ENGtext.find('bookList')+13:ENGtext.find('var canonicalUrl')-7]
    ENGlist = ENGlist.split("},{")
    ENGkeys = []
    LANGkeys = []
    for i in range(len(ENGlist)):
        part1 = ENGlist[i][6:ENGlist[i].find(',')-1]
        part2 = ENGlist[i][ENGlist[i].find(',')+9:-1]
        ENGkeys.append([part1,part2])
    for i in range(len(ENGlist)):
        part1 = ENGkeys[i][0];
        newpage = requests.get('http://www.bible.is/'+LANG+'/'+ENGkeys[i][0]+'/1')
        newdata = bs4.BeautifulSoup(newpage.text,'lxml')
        newtext = newdata.get_text()        
        part2 = newtext[newtext.find('var currentBookName = "')+23:newtext.find('var currentChapter')-6]
        LANGkeys.append([part1,part2])
        
    outf = codecs.open(LANG+".dat","w+","utf-8")
    for i in range(len(ENGkeys)):
        for j in range(chapters[ENGkeys[i][0]]):
            outf.write(ENGkeys[i][1]+" "+str(j+1)+", "+LANGkeys[i][1]+" "+str(j+1)+"\n")
    outf.close()
main()

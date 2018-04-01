
import mechanize
from bs4 import BeautifulSoup
import re
global count,flag
count=1
flag=0

def googlesearch():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')]
    br.open('http://www.google.com/')

    # do the query
    br.select_form(name='f')
    br.form['q'] = 'codingprivacy' # query
    data = br.submit()
    #print(data)
    soup = BeautifulSoup(data.read(),'html.parser')

    while flag!=1:
        global count,flag
        count=int(count/10)*10
        for a in soup.select('.r a'):

            #print(a)    #scraped results  contains
            url_final=re.search('q=(.+?)&amp',str(a)).group(1)
            if (url_final=="http://construct2developer.blogspot.com/p/privacy-policy.html"):
                print('Approx Rank Of Website:',count)
                print('Exact Between ',int(count/10)*10,'to',(int(count/10)*10)+10)
                print(url_final)
                flag=1
                break
            count+=1
        if(flag!=1):
            page=str((int(count/10)*10)+10)
            print('page is ',int(page)/10)

            data=br.open('https://www.google.co.in/search?q=codingprivacy&dcr=0&biw=641&bih=615&ei=dfLAWpuBFMzovgTA1oOYDQ&start='+page+'&sa=N')

            soup = BeautifulSoup(data.read(),'html.parser')






        #print "Found the URL:", a['href']
googlesearch()



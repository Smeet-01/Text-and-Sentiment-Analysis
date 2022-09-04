from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.read_excel ('Input.xlsx')
url = df.iloc[:,1:]
url_list = url.values.tolist()

def get_doc(URL):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
    response = requests.get(URL, headers = headers)
    return response.content



def data_parsing(soup):
    title = soup.find('title')
     

    title = str(title.string)
    title_list = [title]

    text_list = []
    for text in soup.find_all('p'):
        text_list.append((text.string))

    text = str(text.string)
    
    Universal_list = []
    Universal_list = title_list + text_list

    Universal_list = list(filter(None, Universal_list))
      
    return Universal_list



def output(Universal_list,i):
    textfile = open("{}.txt".format(i), "w", encoding='utf-8')
    for element in Universal_list:
        textfile.write(element + "\n")
    textfile.close()


c = 0
a = ''

for i in url_list:

    a = str(i)
    s1 = slice(2, -2)    
    A = (a[s1])
    
    html_doc = get_doc(A)
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    c += 1
    
    Universal_list = data_parsing(soup)
    
    output(Universal_list,c)
    
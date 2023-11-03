def raceInfo(Soup):
    results_header = Soup.find("div", {"class": "Results-header"})
    eventName = results_header.find("h1").text
    eventDate = results_header.find("span",{"class": "format-date"}).text
    eventNumber = results_header.find_all("span")[-1].text
    race = {'eventName':eventName,'eventDate' :eventDate ,'eventNumber':eventNumber , 'results':[]}
    return race


def lookUp(A,B):
    try:
        C = B[A]
    except:
        C = None
    return C


def raceTable(Soup):
    result_table = Soup.find("tbody", {"class":"js-ResultsTbody"}).find_all("tr")
    return result_table

def row_generate(html):
    club = lookUp('data-club',html)
    name = lookUp('data-name',html)
    position = lookUp('data-position',html)
    group = lookUp('data-agegroup',html)
    gender = lookUp('data-gender',html)
    try:
        runnerURL = html.find("td",{"class": "Results-table-td Results-table-td--name"}).find('div',{"class": "compact"}).find('a')['href']
    except:
        runnerURL = '--DID NOT WORK--'
    if runnerURL != '--DID NOT WORK--':
        runnerID = runnerURL.split("/")[-1]
    else:
        runnerID = None
    try:
        time = html.find("td",{"class": "Results-table-td Results-table-td--time"}).find('div',{"class": "compact"}).text
    except:
        time = None
    if time == None:
        try:
            time = html.find("td",{"class": "Results-table-td Results-table-td--time Results-table-td--pb"}).find('div',{"class": "compact"}).text
        except:
            time = None
    if time == None:
        try:
            time = html.find("td",{"class": "Results-table-td Results-table-td--time Results-table-td--ft"}).find('div',{"class": "compact"}).text
        except:
            time = None

    row = [club,name,position,group,gender,runnerID,time]
    return row

def Generate_Soup(URL):
    import requests
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}
    from bs4 import BeautifulSoup as bs
    try:
        make_request = requests.get(URL,headers=headers)
        if make_request.status_code == 200:
            make_soup = [bs(make_request.text, "html.parser"), True]
        else:
            make_soup = [bs(make_request.text, "html.parser"), make_request.status_code]
        return make_soup
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

import time


def run():
    TestLocations = ['agnew','wallaceneuk']
    Collection = []

    for i in range(len(TestLocations)):
        raceURL = f"https://www.parkrun.org.uk/{TestLocations[i]}/results/lastest/"
        #print (raceURL)
        mockURL = r"https://www.bbc.co.uk/sport"
        returnPage = Generate_Soup(raceURL)
        print (returnPage)
        break

        #if returnPage[1] == True:
            #data_dict = raceInfo(returnPage[0])
            #create_table = raceTable(returnPage[0])
            #for row in create_table:
                #data_dict['results'].append(row_generate(row))

            #Collection.append(data_dict)
            #time.sleep(1)
        #else:
            #print ('Was not able to make this request',returnPage[1])

    #print (Collection)



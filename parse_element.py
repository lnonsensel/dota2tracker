from bs4 import BeautifulSoup



def parse_element(responce, hero, app_name):
    responce = responce.replace('Win Rate )',f'Win Rate )')
    responce = BeautifulSoup(responce, 'lxml')

    window = str(responce.find('div',{'class': 'content-box-lvl-2 roles'}))
    head = str(responce.find('head'))
    links = responce.find_all('link')
    css = responce.find_all('style')
    js = responce.find_all('script')


    filename = f"./{app_name}/{hero}_parsed.html"
    

    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write(head)
        file.write('\n')
        for i in links:
            file.write(str(i))
            file.write('\n')
        
        for i in css:
            file.write(str(i))
            file.write('\n')
        
        for i in js:
            file.write(str(i))
            file.write('\n')

        file.write(window)

        

    return filename
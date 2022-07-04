import json
import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup


def sub_especial_characters(string: str):
    new_string = re.sub(r'[àáã]', 'a', string)
    new_string = re.sub(r'[ú]', 'u', new_string)
    new_string = re.sub(r'[óõ]', 'o', new_string)
    new_string = re.sub(r'[êé]', 'e', new_string)
    new_string = re.sub(r'[í]', 'i', new_string)
    new_string = re.sub(r'[ç]', 'c', new_string)
    
    return new_string
    

def get_objectives(URL: str):
    headers = {'user-agent': 'Mozilla/5.0'}
    link = requests.get(URL, headers=headers)
    soup = BeautifulSoup(link.content, 'html.parser')
    
    objectives = soup.find_all('div', attrs={'class': 'post-body entry-content'})
    filter_objective = re.findall(r'[(]\w+[)][\s\w,.()À-ú\-]+', str(objectives), flags=re.I | re.M)
    filter_objective = sub_especial_characters(str(filter_objective))
    
    pprint(filter_objective)
    
    with open('objectives.json', 'w') as file:
        json.dump(filter_objective, file)


get_objectives('https://www.tudosaladeaula.com/2020/08/habilidades-bncc-educacao-infantil-pre.html')

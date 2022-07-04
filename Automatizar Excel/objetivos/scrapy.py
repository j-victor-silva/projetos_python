import json
import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup


def sub_especial_characters(older_list: list) -> list:
    new_list = older_list
    for i in range(len(older_list)):
        new_list[i] = re.sub(r'[àáã]', 'a', new_list[i])
        new_list[i] = re.sub(r'[ú]', 'u', new_list[i])
        new_list[i] = re.sub(r'[óõ]', 'o', new_list[i])
        new_list[i] = re.sub(r'[êé]', 'e', new_list[i])
        new_list[i] = re.sub(r'[í]', 'i', new_list[i])
        new_list[i] = re.sub(r'[ç]', 'c', new_list[i])
    
    return new_list


def dict_converter(older_list: list) -> dict:
    regex_key = r'([(]\w+[)])([\s\w,.()\-]+)'
    new_dict = {}
    for i in range(len(older_list)):
        for k in re.finditer(regex_key, older_list[i], flags=re.I | re.M):
            new_k_key = re.sub(r'[()]+', '', k.group(1))
            new_k_value = k.group(2)
            new_dict[new_k_key] = new_k_value[1:]
    
    return new_dict
            

def get_objectives(URL: str):
    headers = {'user-agent': 'Mozilla/5.0'}
    link = requests.get(URL, headers=headers)
    soup = BeautifulSoup(link.content, 'html.parser')
    
    objectives = soup.find_all('div', attrs={'class': 'post-body entry-content'})
    filter_objective = re.findall(r'[(]\w+[)][\s\w,.()À-ú\-]+', str(objectives), flags=re.I | re.M)
    filter_objective = sub_especial_characters(filter_objective)
    filter_objective = dict_converter(filter_objective)
    
    with open('objectives.json', 'w') as file:
        json.dump(filter_objective, file)


get_objectives('https://www.tudosaladeaula.com/2020/08/habilidades-bncc-educacao-infantil-pre.html')

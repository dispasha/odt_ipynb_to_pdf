from bs4 import BeautifulSoup
import re
import json

def get_input_list(inputs):
    return BeautifulSoup(inputs, features="lxml").\
        find_all('div', {'class': 'jp-Cell-inputWrapper jp-Notebook'})

def get_output_list(outputs):
    return BeautifulSoup(outputs, features="lxml").\
        find_all('span')


def merge_htmls(inputs, outputs, word):
    print("Searching for your tags...")
    with open("config.json") as f:
        conf = json.load(f)
    output_tags = re.findall(Rf'(?:{conf["plain_word"]})|(?:{conf["formatted_word"]})|(?:{conf["original_word"]})', word)
    input_tags = re.findall(conf["input_word"].replace("%d", "[0-9]+"), word)
    print("Inserting stuff...")
    for tag, rep in zip(output_tags, get_output_list(outputs)):
        if tag == conf["plain_word"]:
            del rep['class']
            rep['data-mime-type'] = 'text/plain'
            rep = str(rep).replace("$", "")          
        elif tag == conf["formatted_word"]:
            del rep['class']      
        word = word.replace(tag, str(rep), 1)
    input_reps = get_input_list(inputs)
    for tag in input_tags:
        word = word.replace(tag, str(input_reps[int(re.search(r"\d+", tag).group()) - 1]), 1)
    print("Saving...")
    with open("temp/temp.html", 'w', errors="ignore", encoding="windows-1251") as f_output:
        with open("templates/header.html", encoding='utf-8') as head:
            word = word.replace('<head>', '<head>\n'+head.read())
            f_output.write(word)
            


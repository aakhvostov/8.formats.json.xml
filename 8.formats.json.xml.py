# coding=utf-8
from collections import Counter
from pprint import pprint
from collections import Counter
import json
import xml.etree.ElementTree as ET


def get_count(search_list, file_name):
    count = {}
    for i in search_list:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1

    return print(
        f'10 самых часто встречающихся в новостях слов длиннее 6 символов в {file_name}- '
        f'{sorted(count, key=count.get, reverse=True)[:10]}')


def get_easy_count(search_list, file_name):
    present_list = []
    for word in Counter(xml_list).most_common(10):
        present_list.append(word[0])
    Counter(search_list).most_common(10)
    return print(
        f'10 самых часто встречающихся в новостях слов длиннее 6 символов в {file_name}- '
        f'{present_list}')


with open("newsafr.json", "r", encoding="utf-8") as f:
    json_list = []
    data = json.load(f)
    items = data["rss"]["channel"]["items"]
    for news in items:
        description = news.get("description")
        description_list = description.split()
        for word in description_list:
            if len(word) > 6:
                json_list.append(word)
    json_list.sort()


parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
temp_xml_news = []
xml_list = []
xml_items = root.findall("channel/item/description")
for xmli in xml_items:
    news = xmli.text
    temp_xml_news.append(news.split())
    for words in temp_xml_news:
        for word in words:
            if len(word) > 6:
                xml_list.append(word)
xml_list.sort()


get_count(json_list, "newsafr.json")
get_easy_count(json_list, "newsafr.json")

get_count(xml_list, "newsafr.xml")
get_easy_count(xml_list, "newsafr.xml")
import re
from bs4 import BeautifulSoup as bs
import requests
import utensylia

# Maybe some more info would be fine
# Date RC: 2022-12-28
# Author: tozda


def get_tobacco_title(tagh1):

    tobacco_header_text = [i.text for i in soup.h1]

    tobacco_raw_header = tobacco_header_text[1]
    tobacco_raw_header = re.sub("'", "", tobacco_raw_header)
    tobacco_raw_header = re.sub(r"\r", "", tobacco_raw_header)
    tobacco_raw_header = re.sub(",", "", tobacco_raw_header)
    tobacco_title_array = re.split('\n', tobacco_raw_header)
    ttitle = tobacco_title_array[1] + ' ' + tobacco_title_array[2]

    return ttitle


# just definition of array
tobacco_info = []

t_params = []
t_values = []

# get the particular page
print(utensylia.generate_welcome_message())
msg = "Informacje o którym tytoniu mam ściągnąć z Tobacco Reviews? Podaj konkretny URL!"
answer = input(msg)
answer = re.sub('\n', '', answer)
url = answer
#  url = 'https://www.tobaccoreviews.com/blend/11567/hu-tobacco-moroccan-bazaar'
page = requests.get(url)
# check if response code in 200
response = page
# <Response [200]> jeśli komunikat inny to zakończ program

# get the content of web page
soup = bs(page.content, features="html.parser")

# get the tobacco title
tobacco_title = get_tobacco_title(soup.h1)

# get average rating
average_rating = soup.find(title='Average rating out of 4').text
votes = soup.find(itemprop="count").text
# just to keep it neat format to leading zeros
votes = '{:0>3}'.format(votes)

# get the table with tobacco params
tobacco_param_table = soup.find(id='stats')

# extract params and values
t_params = [i.text for i in tobacco_param_table.find_all('th')]
t_values = [i.text for i in tobacco_param_table.find_all('td')]

# and make dictionary out of it
tobacco_data = dict(zip(t_params, t_values))

# read template
array_from_file = []
current_file = open('tw_template.txt', 'r', encoding="utf-8")

for line in current_file:
    array_from_file.append(line)

current_file.close()

# get tiddlywiki timestamp
tw_timestamp = utensylia.get_timestamp()
tw_timestamp = utensylia.date2string(tw_timestamp, 23, 0)

current_date = utensylia.get_timestamp()
current_date = utensylia.date2string(current_date, 10, 1)

# check if it is flavouring
is_flavoring = ''
if tobacco_data["Flavoring"] == "None":
    is_flavoring = ''
else:
    is_flavoring = 'A,'

# get the first letters of tobacco contents
contents_array = re.split(", ", tobacco_data["Contents"])

abbreviations_array = []
for i in contents_array:
    if re.search(r'\s', i):
        letters = []
        iarr = re.split(" ", i)
        letters = []
        for ia in iarr:
            a = ia[0]
            letters.append(a)
        fcharacters = ''.join(letters)
        abbreviations_array.append(fcharacters)
        continue

    abbreviations_array.append(i[0])

# convert array with abbreviations into string
contents_abbreviations = ','.join(abbreviations_array)

# and merge all into one string
tobacco_abbreviations = is_flavoring + contents_abbreviations

tw_template_filled = []
for item in array_from_file:
    item = re.sub('<RATE>', average_rating, item)
    item = re.sub('<VOTES>', votes, item)
    item = re.sub('<TOBACCOTITLE>', tobacco_title, item)
    item = re.sub('<TIMESTAMP>', tw_timestamp, item)
    item = re.sub('<FIRSTPURCHASEDATE>', current_date, item)
    item = re.sub('<TOBACCOABBREVIATIONS>', tobacco_abbreviations, item)
    item = re.sub('<TRLINK>', url, item)
    item = re.sub('<BLENDTYPE>', tobacco_data["Blend Type"], item)
    item = re.sub('<BLENDEDBY>', tobacco_data["Blended By"], item)
    item = re.sub('<BRAND>', tobacco_data["Brand"], item)
    item = re.sub('<CONTENTS>', tobacco_data["Contents"], item)
    item = re.sub('<COUNTRY>', tobacco_data["Country"], item)
    item = re.sub('<CUT>', tobacco_data["Cut"], item)
    item = re.sub('<FLAVORING>', tobacco_data["Flavoring"], item)
    item = re.sub('<PACKAGING>', tobacco_data["Packaging"], item)

    tw_template_filled.append(item)

# write file with .tid extension
file = 'tobacco.tid'
current_file = open(file, 'w', encoding="utf-8")
for item in tw_template_filled:
    current_file.write(item)
current_file.close()

msg = "Import file " + file + " into your TiddlyWiki"
print(msg)

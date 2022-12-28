import re
import datetime


def get_timestamp():
    """
    Umożliwia pozyskanie aktualnego timestampa jako string
    :return: tmstmp - aktualny timestamp składający się z 17 znaków wymaganych przez TiddlyWiki
    """
    tmstmp = datetime.datetime.now()
    return tmstmp


def date2string(date, timestamp_length, timestamp_format):
    """ Zamienia datę na string
        timestamp_format: 0 = Formatuje bez kresek i kropek
        timestamp_format: 1 = formatuje z kreskami i kropkami

    :param date:
    :return string_date:
    """
    str_date = str(date)
    string_date = str_date[:int(timestamp_length)]
    if timestamp_format == 0:
        string_date = re.sub(r'-', '', string_date)
        string_date = re.sub(r':', '', string_date)
        string_date = re.sub(r' ', '', string_date)
        string_date = re.sub(r'\.', '', string_date)

    return string_date


def get_file_into_array(file):
    """
    Loads content of file into array
    :param file:
    :return:
    """
    array_from_file = []
    current_file = open(file, 'a', encoding="utf-8")

    for line in current_file:
        array_from_file.append(line)

    return array_from_file


def write_array_to_file(array, file):
    current_file = open(file, 'a', encoding="utf-8")
    for item in array:
        current_file.write(item)
    current_file.close()

    return 0


def map_template(template, values):
    pass


def generate_welcome_message():
    msg = "\n\t1. Open https://www.tobaccoreviews.com/ and search for the particular tobacco. Copy the URL.\n" \
          "\t2. Run the 'main.py' script\n" \
          "\t3. Paste copied URL as input to the script\n" \
          "\t4. Wait till script completes\n" \
          "\t5. Open your TiddlyWiki\n" \
          "\t6. Click 'import' icon and look for 'tobacco.tid' file located at the same directory as 'main.py' script\n" \
          "\t7. Import tiddler\n" \
          "\n\tINFO: TiddlyWiki site: 'https://tiddlywiki.com/'\n"

    return msg


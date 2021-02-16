import io
import os
from distutils import log


__author__ = "Dmitry Marenich <d.marenich@protonmail.ch>"


station_number = "03014009"
station_prefix = "EST"
data_res_daily = "MD"
data_res_hourly = "MH"
data_year = "2020"
data_path = "air_quality/data/RVVCCA/"
data_file_ext = " copy.txt"
data_format = "csv"
data_file = data_res_daily + station_prefix + station_number + data_year + data_file_ext
# TODO:
# - Refactor: And the correct, not platform-dependent usage for joining your paths is: os.path.join(root, f)
# - Refactor: Detecting correctly charset <iso-8859-1> or <UTF-8>.
#   -- fixed bug 'UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf3 in position 50: invalid continuation byte'
data_file_path = os.path.join(
    os.path.abspath(data_path), station_prefix + station_number, data_year + "/"
)
context = []

import csv

def read_csv(file=''):
    #source_codepage =
    log.info("Read file: " + file + "\n\t")
    with io.open(file, mode='r', encoding='iso-8859-1', newline='') as csv_file:
        # Add values to map
        # items = []
        # for line in csv_file:
        #     line = map(int, line.split())
        #     items.append(line)
        row_data = csv.reader(csv_file, dialect='excel-tab', delimiter=' ')
        header = []
        rows = []
        result = []
        list_column_name = []
        list_column_dimension = []
        for row in row_data:
            rows.append(row)
        # print(rows)
        list_column_name = list(rows[3])
        list_column_dimension = list(rows[4])
        table_header = map(list_column_name, list_column_dimension)
        print(table_header)
        print(list_column_name)
        print(list_column_dimension)
        # reader = csv.DictReader(res, dialect='excel-tab')
        # for line in reader:
        #     print(row)
        #     result.append(line)
        print("Test result.")
        csv_file.close
    if result == []:
        log.warn("don't have a result.")
    print(result)
    return result


def read_json():
    pass
def read_xml():
    pass
def read_sav():
    pass


def read_file(file='', path='', format=''):
    """ Read file to memory.

        filename:
            Selected file name to reading.
        file_path:
            Directory with existing data files.
        file_format:
            Data file format like CSV, JSON, XML, SAV.
        When successful, returns read file's contents.
    """
    if (file == ''):
        log.ERROR("File not found.")
    else:
        src = path + file
        # TODO: format.lower
        fmt = format

        if (fmt == " "):
            log.warn("Argument 'file format' is empty.")
        elif (fmt == "csv"):
            read_csv(src)
        elif (fmt == "json"):
            read_json(src)
        elif (fmt == "xml"):
            read_xml(src)
        elif (fmt == "sav"):
            read_sav(src)



def preprocess_data(data):
    """ Preprocess raw data for using. """
    pass


context = read_file(data_file, data_file_path, data_format)

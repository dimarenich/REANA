import io
import os
import csv


__author__ = "Dmitry Marenich <d.marenich@protonmail.ch>"


station_number = "03014009"
station_prefix = "EST"
data_res_daily = "MD"
data_res_hourly = "MH"
data_year = "2020"
data_path = "air_quality/data/RVVCCA/"
data_file_ext = ".txt"
data_format = "csv"
# Example full filename = "air_quality/data/RVVCCA/EST03014009/2020/MDEST030140092020.txt"
data_file = data_res_daily + station_prefix + station_number + data_year + data_file_ext
# TODO:
# - Refactor: And the correct, not platform-dependent usage for joining your paths is: os.path.join(root, f)
# - Refactor: Detecting correctly charset <iso-8859-1> or <UTF-8>.
#   -- fixed bug 'UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf3 in position 50: invalid continuation byte'
data_file_path = os.path.join(
    os.path.abspath(data_path), station_prefix + station_number, data_year + "/"
)
context = []


def read_csv(source=''):
    print("___________________\n")
    print("[Info] Read file: " + source + "\n\t")
    with io.open(source, mode='r', encoding='iso-8859-1') as csv_data:
        raw_data = csv.reader(csv_data, delimiter="\t")
        result = []
        for row in raw_data:
            result.append(row)
        csv_data.close
    if result == []:
        print("[Warn] Don´t have a result.")
    print(result)
    return result

def read_json():
    pass
def read_xml():
    pass
def read_sav():
    pass


def read_file(file_name='', file_path='', file_format=''):
    """ Read file to memory.

        filename:
            Selected file name to reading.
        file_path:
            Directory with existing data files.
        file_format:
            Data file format like CSV, JSON, XML, SAV.
        When successful, returns read file's contents.
    """
    f = file_path + file_name
    # TODO: fmt.lower
    fmt = file_format

    if (fmt == " "):
        print("[Warn] 'Data format' is empty. Please fill it before starting.")
    elif (fmt == "csv"):
        read_csv(f)
    elif (fmt == "json"):
        read_json(f)
    elif (fmt == "xml"):
        read_xml(f)
    elif (fmt == "sav"):
        read_sav(f)


def preprocess_data(data):
    """ Preprocess raw data for using. """
    pass


context = read_file(data_file, data_file_path, data_format)
preprocess_data(context)
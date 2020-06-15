import itertools,time
from csv import DictReader
import os
root_path = os.path.abspath(os.path.dirname(__file__))
index_column = "SCHNAM05"
city_column  = "LCITY05"
state_column = "LSTATE05"
metro_centric_locale_column = "MLOCALE"

def print_counts():
    file_location = root_path + '/school_data.csv'
    school  = Schooldata(file_location)

    schoolData = school.read_file()
    school.count_all(schoolData)


class Schooldata:
    def __init__(self, file_location):
        self.file_location = file_location

    def read_file(self):
        '''
        read the location and return the dta of the file
        convert the dictReader format file to dictionary to perform operation
        :return:
        '''
        school_dict = {}

        f = open(self.file_location, 'r', encoding='ISO-8859-1')
        dict_reader = DictReader(f)
        column_names = dict_reader.fieldnames
        for c in column_names:
            school_dict[c] = []
        for row in dict_reader:
            for c in column_names:
                school_dict[c].append(row[c])

        return school_dict

    def count_all(self, data_file):

        index_values = data_file[index_column]
        state_values = data_file[state_column]
        city_values = data_file[city_column]
        metro_centric_locale_values = data_file[metro_centric_locale_column]
        self.total_count(index_values)
        self.count_by_state(state_values)
        self.count_by_city(city_values)
        self.count_by_metro_centric_locale(metro_centric_locale_values)

    def total_count(self,data_file):
        '''

        :param file_name:
        :return: return the total count
        it will return total count to filelines-1 as first line is header
        '''
        count = sum(1 for row in data_file)
        print("Total Schools: {}".format(count))

    def count_by_state(self, data_file):
        '''

        :param file_name:
        :return: return the total count of schools according to state
        '''
        print("Schools by State:")
        for key, grp in itertools.groupby(sorted(data_file)):
            print('{}: {}'.format(key, len(list(grp))))

    def count_by_city(self, data_file):
        '''

        :param file_name:
        :return: return the total count of schools according to city,length of total city having schools
        '''
        l = []
        print("Schools by City:")
        for key, grp in itertools.groupby(sorted(data_file)):
            # print('{}: {}'.format(key, len(list(grp))))
            l.append((key, len(list(grp))))
        sorted_list = sorted(l, reverse=True, key=lambda x: x[1])
        u_sorted_list = sorted_list[0]
        print("City with most school {} ({} schools)".format(u_sorted_list[0],u_sorted_list[1]))
        print("Unique cities with atleast one school {}".format(len(l)))

    def count_by_metro_centric_locale(self, data_file):
        '''

        :param file_name:
        :return: return the total count of schools according to metro centric locale
        '''

        print("Schools by Metro-Centric locale:")
        for key, grp in itertools.groupby(sorted(data_file)):

            print ('{}: {}'.format(key, len(list(grp))))


print_counts()

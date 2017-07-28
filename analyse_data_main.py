#!/usr/bin/env python3
__author__ = 'agnetha'


from data_sourcing import *

import clean_data_files





if __name__ == "__main__":
    mp_data = MPData(mp_data_file_name)
    mp_matrix = mp_data.get_data()
    mp_header = mp_data.get_header()

    print(mp_header)
    print(mp_data.get_party_count())
    # print("Names",mp_header[0], mp_matrix[:, 0])
    # data_set = clean_data_files.extract_csv_data(file_name)
    # print(np.shape(data_set))

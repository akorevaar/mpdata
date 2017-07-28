
import numpy as np
import pandas as pd
import collections


mp_data_file_name = "data/mps-csv.csv"

class MPData:
    def __init__(self, file_name):
        self.data_set = pd.read_csv(file_name)
        self.matrix = self.data_set.as_matrix()
        self.header = self.data_set.dtypes.index
        self.n_rows = np.shape(self.matrix)[0]

        name_idx = 0
        salutation_idx = 1
        self.names = []
        for i in range(self.n_rows):
            title = ""
            if type(self.matrix[i, salutation_idx]) == str:
                title = self.matrix[i, salutation_idx] + " "
            name = self.matrix[i, name_idx]
            self.names.append("{}{} {}".format(title, name.split(",")[1].lstrip(), name.split(",")[0]))

    def get_data(self):
        return self.matrix

    def get_header(self):
        return self.header

    def get_names(self):
        return self.names

    def get_party_count(self):
        # and count
        party_idx = 3
        self.parties = collections.Counter()
        for i in range(self.n_rows):
            p = self.matrix[i, party_idx]
            if type(p) is not str:
                p = "Independent"
            self.parties[p] += 1

        return self.parties
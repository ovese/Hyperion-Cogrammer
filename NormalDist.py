import math
import numpy as np
import pandas as pd
import csv
# data source:
# https://statisticsbyjim.com/hypothesis-testing/identify-distribution-data/


class NormalDistribution:
    def __init__(self, x_list, mu,sigma):
        self.x_list = x_list
        self.mu = mu
        self.sigma = sigma


    def read_data(self,data_file):
        """
        Data file is a text input which
        represents the file to read.
        File type can be csv, xlsx, txt etc.
        Whats important to note is that the
        input file contains only numeric values
        """
        file_type = data_file.split('.')
        data = []
        if file_type[1] == "txt":
            print("Working with a text file: method 1")
            data1 = open(data_file,"r")
            print(f"type of data1 is: {data1}")
            data = data1.read()
            data1.close()
            
            print("Working with a text file: method 2")
            with open(data_file,"r") as file:
                print(f"type of file is: {file}")
                data2=file.read()
                # print(data2)
                file.close()
        elif file_type[1] == "csv":
            print("Working with a csv file")
            # rows = []
            # with open(data_file, 'r') as file:
            #     csvreader = csv.reader(file)
            #     header = next(csvreader)
            #     for row in csvreader:
            #         rows.append(row)
            # print(header)
            # print(rows)
            with open(data_file) as file:
                content = file.readlines()
            header = content[:1]
            rows = content[1:]
            for i in range(len(rows)):
                # data.append(rows[i].replace('\n',''))
                # data.append(rows[i].strip())
                data.append(float(rows[i].strip()))
        elif file_type[1] == "xlsx":
            print("Working with xlsx files")
        else:
            print("Not a known file type")
            
        return data


    def get_mean(self, data_in):
        count = 0
        list_sum = 0
        for item in data_in:
            list_sum += item
            count += 1
        return count, float(list_sum/count)
    
    
    def get_variance(self,data_in, meanval):
        data_sum_sq = 0
        data_size = len(data_in)
        for i in range(data_size):
            data_sum_sq += ( (data_in[i]-meanval)**2 )
            
        return float( data_sum_sq/(data_size-1) )         


    def exponent(self):
        exp_list = []
        for i in range(0,len(self.x_list)):
            tmp_res = -0.5*((self.x_list[i]-self.mu)/self.sigma)**2
            exp_res = math.exp(tmp_res)
            exp_list.append(float(exp_res))

        return exp_list
    
    
    def normal_dist(self):
        nd_list = []
        tmp_var = 1/(self.sigma*(2*math.pi)**0.5)
        tmp_exp = self.exponent()
        for i in range(0, len(tmp_exp)):
            f_x = tmp_var*tmp_exp[i]
            nd_list.append(f_x)
        
        return nd_list
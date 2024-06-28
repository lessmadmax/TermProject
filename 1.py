import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
class graph:
    def graphSubplot(totalRow, totalColumn, row, x, y, title, xlabel=0, ylabel=0):
        plt.sublot(totalRow, totalColumn, row)
        plt.plot(x, y)
        plt.title(title)
        if xlabel != 0:
            plt.xlabel(xlabel)
        if ylabel != 0:
            plt.ylabel(ylabel)
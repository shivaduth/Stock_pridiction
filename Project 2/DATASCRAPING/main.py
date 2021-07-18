import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import os
import csv

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

ticker = "FB"

start = dt.datetime(2021,1,1)
end = dt.datetime(2021,5,1)

data = web.DataReader(ticker,"yahoo",start,end)









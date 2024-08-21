import pandas as pd
import numpy as np

dataset = pd.read_csv('AirPassengers.csv')

passengers_series = pd.Series(np.array(dataset['#Passengers']), index=dataset['Month'])

print(passengers_series.iloc[(passengers_series.index >= "1949-01") & (passengers_series.index <= "1949-12")].sum())


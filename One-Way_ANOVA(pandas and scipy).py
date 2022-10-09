import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
URL ='https://stepik.org/media/attachments/lesson/8083/genetherapy.csv'
data = pd.read_csv(URL)
A = data[data['Therapy'] == 'A']['expr']
B = data[data['Therapy'] == 'B']['expr']
C = data[data['Therapy'] == 'C']['expr']
D = data[data['Therapy'] == 'D']['expr']
stats.f_oneway(A,B,C,D)
data.boxplot('expr', by='Therapy', figsize=(12,8), grid=True)
print(stats.f_oneway(A,B,C,D))


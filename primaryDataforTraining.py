import pandas as pd
import difflib
import openpyxl
import re


df = pd.read_csv('data_SIRIUS.csv', skipinitialspace=True, sep=';')
df.columns = df.columns.str.lower().str.replace(' ', '_')
#  удаляем строки, в которых нет жалоб на нет и приводим все к нижнему регистру
df['жалобы'] = df['жалобы'].str.lower()

df = df[~df['жалобы'].str.contains('нет')]
df = df[~df['жалобы'].str.contains('медосмотр')]
df = df[~df['жалобы'].str.contains('не предъявляет')]
df = df[~df['жалобы'].str.contains('не высказывает')]
df = df[~df['жалобы'].str.contains('не имеет')]


# Удаляем пробелы с начала строки и в её конце
df['жалобы'] = df['жалобы'].str.strip()
g = df[['специальность_врача', 'жалобы']].copy()
g['жалобы'] = g['жалобы'].str.lower().str.replace(',', '').str.strip().astype(str)
g['специальность_врача'] = g['специальность_врача'].str.lower().astype(str)
g['жалобы'] = g['жалобы'].str.replace('\n', '')
g['жалобы'] = g['жалобы'].str.replace('\t', ' ')
g['жалобы'] = g['жалобы'].str.replace('.', '')
g['жалобы'] = g['жалобы'].str.replace('(', '')
g['жалобы'] = g['жалобы'].str.replace(')', '')
g['жалобы'] = g['жалобы'].str.replace('"', '')
g['жалобы'] = g['жалобы'].str.replace('*', '')
g['жалобы'] = g['жалобы'].str.rstrip('-').str.lstrip('-')
g['жалобы'] = g['жалобы'].str.replace(' {2,}', ' ', regex=True)
g['жалобы'] = g['жалобы'].str.replace('#', '')
g['жалобы'] = g['жалобы'].str.replace('/', '')
g['жалобы'] = g['жалобы'].str.replace('·', '')
g['жалобы'] = g['жалобы'].str.replace('•', '')
g['жалобы'] = g['жалобы'].str.strip(':')
g['жалобы'] = g['жалобы'].str.replace('-', '')
g['жалобы'] = g['жалобы'].str.replace('|', '')
g['жалобы'] = g['жалобы'].str.replace("\\", '')
g['жалобы'] = g['жалобы'].str.replace(';', '')
g['жалобы'] = g['жалобы'].str.replace('&', '')
# g['жалобы'] = g['жалобы'].str.replace(re'[]')
g['жалобы'] = g['жалобы'].replace(to_replace ="['^0-9']", value='', regex = True)
g['жалобы'] = g['жалобы'].replace(to_replace ="['^a-z']", value='', regex = True)
g = g[(g['жалобы'] != '')]
g = g[(g['жалобы'] != '/')]
g = g[(g['жалобы'] != '+')]
g.to_excel('alp.xlsx')
g.to_csv('data.csv')
print(g.shape)

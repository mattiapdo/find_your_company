# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import lib
import pandas as pd

print("*************     Venture Radar Scanner        ***************\n\n")

companies = list()

with open('urls.txt') as f:
    urls = f.read().splitlines()


for url in urls:
    print("Scraping data from companies similar to", url[37:])
    companies.append(lib.parse_page(url))
       
companies = [item for sublist in companies for item in sublist]

table = pd.DataFrame(companies)
table.drop_duplicates(inplace = True)

writer = pd.ExcelWriter('table.xlsx')
table.to_excel(writer,'Sheet1')
writer.save()

print("\nDone! You collected data from ",table.shape[0],"unique companies\nNow open table.xlsx")
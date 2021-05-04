# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:23:49 2021

@author: HP
"""
import glass_scraper as gs
import pandas as pd


path = "C:/Users/HP/Documents/ds_salary_proj/Operadriver"
df = gs.get_jobs('data scientist',15,False,path,15)
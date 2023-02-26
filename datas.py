import inline as inline
import requests
import re
import pandas
import wheel
import matplotlib
import numpy
r=requests.get('http://www.cleveland.com/metro/index.ssf/2017/12/case_western_reserve_university_president_barbara_snyders_base_salary_and_bonus_pay_tops_among_private_colleges_in_ohio.html')
c=r.content

from bs4 import BeautifulSoup

soup=BeautifulSoup(c,'lxml')
main_content=soup.find('div',class_='entry-content')
content=main_content.find('ul').text
name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
names = name_pattern.findall(content)
salaries=['$876,00','$543,903','$2453,896']
[int(''.join(s[1:].split(','))) for s in salaries]
notas=pandas.Series([2,7,5,10,6],index=["Wilfred","Abbie","Lucas","Julia","Tiago"])
print("Média:",notas.mean())
print(notas.describe())
print(numpy.log(notas))
df=pandas.DataFrame({'Aluno':["Wilfred","Abbie","Harry","Julia","Carrie"],"Faltas":[3,4,2,1,4],"Provas":[2,7,5,10,6],"Seminario":[8.5,7.5,9.0,7.5,8.0]})
grafico=df.plot(kind='barh',x='Aluno',y='Faltas')
df.plot.hist()



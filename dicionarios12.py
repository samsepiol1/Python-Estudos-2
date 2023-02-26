#primeira parte
people={"name":"João","age":39,"skills":['python','ruby','php']}
filmes={"Titulo":"Star Wars","Ano":1977,"Diretor":'George Lucas'}
locadora=[{"Titulo":"Star Wars,","ano":1977,"Diretor":"George Lucas"},{"Titulo":"Avengers","ano":2012,"Diretor":"Joss Wheadon"},{"Titulo":"Matrix","ano":1999,"Diretor":"Wachowski"}]
print(locadora[2]['ano'])
pessoas={"nome":"Gustavo","sexo":"M","idade":19}
pessoas['peso']=98.5
#Segunda parte
brasil=[]
estado1={'uf':'Rio de Janeiro','Sigla':'RJ'}
estado2={'uf':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input("Unidade Federativa:"))
    estado['sigla']=str(input("Sigla:"))
    brasil.append(estado.copy)
print(brasil)




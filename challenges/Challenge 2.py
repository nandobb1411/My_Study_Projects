class Filme:
    def __init__(self, nome, ano, duração):
        self.nome=nome
        self.ano = ano
        self.duração = duração

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome=nome
        self.ano = ano
        self.temporadas = temporadas


vingadores=Filme('vingaores-guerra infinita',2018,160)
atlanta=Serie('atlanta',2018,2)
print(f'Nome:{atlanta.nome} - Ano: {atlanta.ano} '
      f'-Temporadas:{atlanta.temporadas}')
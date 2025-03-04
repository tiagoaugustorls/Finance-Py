#importando o sqlite3
import sqlite3 as lite

#criando a conexão com o banco de dados
con = lite.connect('dados.db')

#criando tabela categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE categoria (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT);")

#criando tabela receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE receitas (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL);")

#criando tabela gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE gastos (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL);")
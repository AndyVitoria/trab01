#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Corretor
import os


def abrir(dir):
    lst = []
    arq = open(dir, 'rt')
    linha = arq.readline().strip('\n')
    while (linha != ''):
        lst.append(linha)
        linha = arq.readline().strip('\n')
    return lst


def compila():
    arq = open('saida/tweets.txt')
    lstArq = abrir('dados/lote.txt')[:-1]
    for arquivos in lstArq:
        linha = abrir(arquivos)


def getTweet(string):
    # Fatia a string pegando somente o Tweet, este que está entre as tags '"text":"' e '",'
    tweet = string[1:-1].split('"text":"')[1].split('",')[0]
    return Corretor.corrige(tweet)



def getDataHora(string):
    # Fatiamento da data e hora da postagem
    tmp = string.split(',')[0][15:-1].split(' ')  # Lista temporaria
    data = tmp[2] + ' ' + tmp[1] + ' ' + tmp[-1]
    hora = tmp[3]
    return [data, hora]


def listaDir():
    # Listagem dos diretorios e arquivos dentro da pasta dados
    os.system("dir dados\\ /b /o:n >dados\\lote.txt")
    return


def getDados(elem):
    string = abrir('dados/' + elem)[0]
    tweet = getTweet(string)
    dataHora = getDataHora(string)
    id = elem[:-4]
    return [id, dataHora[0], dataHora[1], tweet]


def setDados(lst, arq):
    arq.write(lst[0] + '|' + lst[1] + '|' + lst[2] + '|' + lst[3] + '\n')
    return

def main():
    listaDir()
    saida = open('dados/' + str(input("Informe o arquivo de saida: ")),'wt')
    #saida = open('compilados/saida.txt', 'wt')
    lstArq = abrir('dados/lote.txt')[:-1]
    print("Extração dos dados em progresso.")
    tot = len(lstArq)
    cont = 0
    for elem in lstArq:
        cont += 1
        print("Progresso %d" % (cont/tot * 100))
        dados = getDados(elem)
        setDados(dados, saida)
    saida.close()
    return 0


if __name__ == '__main__':
    main()

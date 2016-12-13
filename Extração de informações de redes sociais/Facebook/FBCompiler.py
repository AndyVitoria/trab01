#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, os


def abrir(dir):
    lst = []
    arq = open(dir, 'rt', encoding='utf8')
    linha = arq.readline().strip('\n')
    while (linha != ''):
        lst.append(linha)
        linha = arq.readline().strip('\n')
    return lst


def abrirJSON(dir):
    put = open(dir, 'r', encoding='utf8')
    data = json.load(put)['data']
    put.close()
    return data


def listaDir(dir):
    # Listagem dos diretorios e arquivos dentro da pasta dados
    os.system("dir " + dir + "\\ /b /o:n >" + dir + "\\lote.txt")
    return


def getDados(dic):
    # Caso não exista mensagem o post não será armazenado
    try:
        dataHora = dic['created_time'].split('T')
        id = dic['id']
        if 'name' in dict.keys(dic):
            titulo = dic['name']
        else:
            titulo = ''
        texto = dic['message']
        check = texto.lower()
        if 'assalt' in check or 'roub' in check:
            return [id, dataHora[0], dataHora[1][:-5], titulo, texto]
        else:
            return []
    except:
        return []


def compila(lst, saida):
    for dic in lst:
        # Separa dados necessários
        dados = getDados(dic)
        # Caso ocorra algum erro o JSON nao sera usado
        if len(dados) > 0:
            # Escreve dados na tabela de compilados
            saida.write(dados[0] + '|' + dados[1] + '|' + dados[2] + '|' + dados[3] + '\n')

            # Escreve texto em arquivo separado
            arq = open('compilados/' + dados[0] + '.txt', 'w', encoding='utf8')
            arq.write(dados[4] + '\n')
            arq.close()
    return

def main():
    listaDir('JSON')
    saida = open('compilados/Tabela.txt', 'wt', encoding='utf8')
    lstArq = abrir('JSON/lote.txt')[:-1]
    print("Compilação dos dados em progresso.")
    tot = len(lstArq)
    cont = 0
    for elem in lstArq:
        cont += 1
        print("Progresso %d" % (cont / tot * 100))
        JSON = abrirJSON('JSON/' + elem)
        if len(JSON) > 0:
            compila(JSON, saida)
    saida.close()
    return 0


if __name__ == '__main__':
    main()
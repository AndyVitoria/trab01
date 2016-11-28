import os
from unicodedata import normalize


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def abrir(arquivo):
    arq = open(arquivo, 'rt')
    lst = []
    linha = arq.readline().strip('\n').strip('\"')
    while (linha) != "":
        lst.append(remover_acentos(linha))
        linha = arq.readline().strip('\n').strip('\"')
    arq.close()
    return lst


def listaDir():
    os.system("dir \"Dados Bruto\"\\ /b /o:n >\"Dados Bruto\"\\lote.txt")
    pastas = abrir('Dados Bruto/lote.txt')
    for elem in pastas:
        if not '.' in elem:
            print(elem)
            os.system("dir \"Dados Bruto\"\\" + elem + "\ /b /o:n > \"Dados Bruto\"\\" + elem + "\lote.txt")
    return


def temNumero(str):
    for elem in str:
        if elem in "0123456789":
            return True
    return False


def checaRepetido(lst):
    for i in range(0, len(lst) - 2, 1):
        for j in range(i + 1, len(lst), 1):
            if lst[i] == lst[j]:
                del (lst[j])
                if len(lst) > 3:
                    return False
                return True
    return True


def escreveItem(dic, item):
    if len(dic["Item"]) != 0:
        for lst in dic["Item"]:
            item.writelines(dic["ID"] + '|' + lst[0] + '|' + lst[1] + '\n')
    return


def escreveTabela(dic, tab):
    index = ["ID", "Crime", "Data", "Hora", "Tipo de Local", "Rua", "Bairro", "Municipio"]
    #Insere no arquivo boletins.txt
    for i in range(0, 3):
        tab[0].writelines(dic[index[i]] + '|')
    tab[0].writelines(dic[index[3]] + '\n')

    # Insere no arquivo locais.txt
    tab[1].writelines(dic[index[0]] + '|' + dic[index[4]] + '\n')

    # Insere no arquivo End.txt
    tab[2].writelines(dic[index[0]] + '|' + dic[index[5]] + '|' + dic[index[6]] + '|' + dic[index[7]] + '\n')

    return

def trataRua(STR):
    ret = ''
    temp = STR.replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('\"', ' ').split(' ')
    for elem in temp:
        if not elem in ['RUA', 'ROD', 'AV', 'N', 'S/N', '', '?', 'AVENIDA', 'TRAVESSA', ' ', 'RODOVIA' ]:
            ret += ' ' + elem
    return ret[1:]


def ExtraiDados(pasta, crimes, saidas):
    lstMunicipios = ['SERRA', 'VILA VELHA', 'CARIACICA', 'VITORIA', 'CACHOEIRO DE ITAPEMIRIM', 'LINHARES', 'SAO MATEUS', 'COLATINA', 'GUARAPARI', 'ARACRUZ', 'VIANA', 'NOVA VENECIA', 'BARRA DE SAO FRANCISCO', 'SANTA MARIA DE JETIBA', 'MARATAIZES', 'CASTELO', 'SAO GABRIEL DA PALHA', 'DOMINGOS MARTINS', 'ITAPEMIRIM', 'AFONSO CLAUDIO', 'ALEGRE', 'BAIXO GUANDU', 'CONCEICAO DA BARRA', 'GUACUI', 'IUNA', 'JAGUARE', 'SOORETAMA', 'ANCHIETA', 'MIMOSO DO SUL', 'PINHEIROS', 'PEDRO CANARIO', 'IBATIBA', 'ECOPORANGA', 'VENDA NOVA DO IMIGRANTE', 'SANTA TERESA', 'PANCAS', 'VARGEM ALTA', 'PIUMA', 'FUNDAO', 'RIO BANANAL', 'MONTANHA', 'MUNIZ FREIRE', 'JOAO NEIVA', 'MARECHAL FLORIANO', 'MUQUI', 'BOA ESPERANCA', 'MANTENOPOLIS', 'ALFREDO CHAVES', 'ITAGUACU', 'VILA VALERIO', 'ICONHA', 'IRUPI', 'SANTA LEOPOLDINA', 'CONCEICAO DO CASTELO', 'BREJETUBA', 'SAO ROQUE DO CANAA', 'MARILANDIA', 'IBIRACU', 'GOVERNADOR LINDENBERG', 'RIO NOVO DO SUL', 'AGUA DOCE DO NORTE', 'JERONIMO MONTEIRO', 'LARANJA DA TERRA', 'PRESIDENTE KENNEDY', 'ATILIO VIVACQUA', 'ITARANA', 'SAO JOSE DO CALCADO', 'BOM JESUS DO NORTE', 'AGUIA BRANCA', 'VILA PAVAO', 'IBITIRAMA', 'SAO DOMINGOS DO NORTE', 'ALTO RIO NOVO', 'APIACA', 'PONTO BELO', 'DORES DO RIO PRETO', 'MUCURICI', 'DIVINO DE SAO LOURENCO']
    excecao = abrir('Tabelas/Excecao.txt')

    arquivos = abrir("Dados Bruto/" + pasta + "/lote.txt")[:-1]

    for arq in arquivos:
        # Decidimos nao tratar anomalidades de poucas ocorrencias
        try:
            print("Filtrando arquivo: " + arq)
            dic = {"Rua": '', "Bairro": '', "Municipio": '', "Tipo de Local": '', "Crime": '', "Tipo de Crime": '',
                   "Data": '', "Hora": '',
                   "ID": '', "Item": []}
            boletim = abrir("Dados Bruto/" + pasta + "/" + arq)
            dic["ID"] = arq[:-4]
            # Ignora boletins catalogados que contem falhas
            if dic["ID"] in excecao:
                print(erro)
            # Tratamento de Anomalidade em boletim
            if "/" in boletim[5]:
                temp = boletim[5].split(',')
                if not "Tipo" in temp[0]:
                    dic["Tipo de Local"] = temp[0].strip('\"')
                temp = temp[1].split(' ')
                dic["Data"] = temp[0]
                if len(temp) > 1 and len(temp[1]) > 4:
                    dic["Hora"] = temp[1] + ':00'
                dic["Crime"] = boletim[7][:4].strip(' ')
                if dic["Crime"][:3] in ['B01', 'B02', 'B10']:
                    temp = boletim[7].strip('\"').strip(',').split(':')
                    if len(temp) > 2:
                        if not dic["Crime"] in dict.keys(dic):
                            crimes[dic["Crime"]] = temp[1:]

                    else:
                        if not dic["Crime"] in dict.keys(dic):
                            crimes[dic["Crime"]] = [temp[1]]

                if "B01G" == dic["Crime"]:
                    dic["Tipo de Local"] = "RESIDÊNCIA"
                temp = boletim[8].split(',')

            else:  # Processo de extracao de dados de boletim normal
                if "/" in boletim[6]:
                    temp = boletim[6].split(',')
                    dic["Tipo de Local"] = temp[0].strip('\"')
                    temp = temp[1].split(' ')
                    dic["Data"] = temp[0]

                    if len(temp) > 1 and len(temp[1]) > 4:
                        dic["Hora"] = temp[1] + ':00'
                    dic["Crime"] = boletim[8][:4].strip(' ')
                    temp = boletim[8].strip('\"').strip(',').split(':')
                    if dic["Crime"][:3] in ['B01','B02','B10']:

                        # Extracao de tipo de crime
                        if len(temp) > 2:
                            if not dic["Crime"] in dict.keys(dic):
                                crimes[dic["Crime"]] = temp[1:]

                        else:
                            if not dic["Crime"] in dict.keys(dic):
                                crimes[dic["Crime"]] = [temp[1]]

                    temp = boletim[9].split(',')
                else:
                    # Excecao que nao sera tratada
                    print(erro)

            # Verifica se boletim possui data
            if int(dic["Data"][-4:]) > 2016 or int(dic["Data"][-4:]) < 2002:
                print(erro)

            # Verificacao para evitar que boletim que nao sejam os desejados passem
            if not ('B01' == dic["Crime"][:3] or 'B02' in dic["Crime"][:3] or 'B10' in dic["Crime"][:3]):
                print(erro)

            # Verificacao de elementos "KM" e "BR" no boletim, seguido de tratamento dessas situacoes
            i = 0
            check = True
            while i < len(temp) and check:
                if len(temp[i]) > 1 and temp[i][0] == ' ':
                    temp[i] = temp[i][1:]
                if len(temp[i]) < 8 and temNumero(temp[i]) and not ("KM" in temp[i] and "BR" in temp[i]):
                    check = False
                else:
                    i += 1

            if not check:
                del (temp[i])
            if len(temp) == 4 and temp[3] == '':
                del (temp[3])
            if len(temp) == 3:
                dic["Rua"] = trataRua(temp[0].upper())
                dic["Bairro"] = temp[1].strip('\"').replace('-', ' ')
                dic["Municipio"] = temp[2].strip('\"')
            else:
                # Casos de anomalidades em boletins, decidimos por nao trata-los
                if checaRepetido(temp) and len(temp) > 3:
                    print(erro)  # Forcamento de erro para sair da extracao
                else:
                    dic["Rua"] = trataRua(temp[0].upper())
                    dic["Bairro"] = temp[1].strip('\"').replace('-', ' ')
                    dic["Municipio"] = temp[2].strip('\"')
            # Verificação de irregularidades nos enderecos
            if dic["Municipio"] == '' or dic['Bairro'] in ['', 'NAO INFORMADO', "ZONA RURAL", 'SN"'] or '-' in dic["Rua"] or not dic["Municipio"] in lstMunicipios or dic["Rua"] == "ZONA RURAL":
                print(erro)  # Forcamento de erro para sair da extracao
            # Procura itens roubados
            i = 15
            check = False
            while i < len(boletim):
                if "Item" in boletim[i] and i < len(boletim) - 1:
                    check = True
                    i += 1
                if check:
                    temp = boletim[i].split(',')
                    dic["Item"].append([temp[1], temp[3]])
                i += 1

            escreveTabela(dic, [saidas[0], saidas[2], saidas[3]])
            escreveItem(dic, saidas[1])
        except:
            # Arquivo de erros, para controle de estatistica de sucesso do algoritmo
            saidas[4].writelines(arq + '\n')
    return crimes


def listaCrimes(dic):
    arq = open('Tabelas/Crimes.txt', 'w')
    key = dict.keys(dic)
    sorted(key)
    for k in key:
        arq.writelines(k + "|" + dic[k][0].strip('\"'))
        if len(dic[k]) > 1:
            arq.writelines("|" + dic[k][1].strip('\"') + '\n')
        else:
            arq.writelines("|\n")

    return


def abrirSaidas():
    # Abertura de arquivos de saida #
    # lst = [BOLETINS, ITENS, LOCAIS, ENDERECOS, EXCECOES]
    lst = []
    lst.append(open("Tabelas/Boletins.txt", 'w'))  # lst[0] = Boletins
    lst.append(open("Tabelas/Itens.txt", 'w'))  # lst[1] = Itens
    lst.append(open("Tabelas/Locais.txt", 'w'))
    lst.append(open("Tabelas/End.txt", 'w'))
    lst.append(open("Tabelas/Excecao.txt", 'w'))
    # ===============================#
    return lst


def fechaSaidas(lst):
    for elem in lst:
        elem.close()
    return


def main():
    # 1 Etapa - Criação de lista de arquivos e pastas
    # Este metodo foi usado apenas na primeria excucao do algoritmo, afim de obter os locais e nomes dos arquivos
    # listaDir() # lista todos os diretorios e arquivos dento da pasta de dados brutos em um arquivo lote.txt

    pastas = abrir('Dados Bruto/lote.txt')[:-1]
    crimes = {}

    print(pastas)

    saidas = abrirSaidas()
    for elem in pastas:
        crimes = ExtraiDados(elem, crimes, saidas)

    listaCrimes(crimes)
    fechaSaidas(saidas)
    return


if __name__ == '__main__':
    main()

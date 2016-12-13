from sqlalchemy import create_engine
import FBCompiler

def abrirPost(dir):
    arq = open(dir, 'r', encoding='utf8')
    texto = arq.read()
    lst = texto.split('\n')
    return lst

def main():
    FBCompiler.listaDir('compilados')
    lstArq = FBCompiler.abrir('compilados/lote.txt')[:-2]
    # Insira aqui o usuario, senha, local e nome do seu banco de dados
    parametros = 'postgresql://postgres:1234@localhost/Savior'
    engine = create_engine(parametros)
    con = engine.connect()
    try:
        con.execute('create table FBPost (id varchar(40) not null, ordem int not null, texto text);')
    except:
        # Caso queira somente adicionar dados comente o comando abaixo.
        con.execute('truncate table FBPost;')

    for elem in lstArq:
        id = elem[:-4]
        lst = abrirPost('compilados/' + elem) # dados a serem inseridos
        ordem = 1
        for linha in lst:
            if linha != '':
                SQL = 'insert into FBPost values (\'' + id + '\', ' + str(ordem)+', \'' + linha + '\');'
                print(SQL)
                ordem += 1
                con.execute(SQL)
    try:
        con.execute('create table Facebook (id varchar(40) not null, data date, hora time, titulo text);')
    except:
        # Caso queira somente adicionar dados comente o comando abaixo.
        con.execute('truncate table Facebook;')
    FBLst = FBCompiler.abrir('compilados/Tabela.txt')
    for string in FBLst:
        string = string.replace('\"','').replace("\'",'')
        lst = string.split('|')
        SQL = 'insert into Facebook values (\'' + lst[0] + '\', \'' + lst[1] + '\', \'' + lst[2] + '\', \'' + lst[3] + '\');'
        print(SQL)
        con.execute(SQL)
    return


if __name__ == '__main__':
    main()
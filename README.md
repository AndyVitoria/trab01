# TRABALHO 01
Trabalho desenvolvido durante a disciplina de BD1

#Sumário

###1	COMPONENTES<br>
- André Barbosa da Vitória;
- Juliana Yuri Kanezaki de Souza; <br>

###2	INTRODUÇÃO E MOTIVAÇAO<br>
Este documento contém a especificação do projeto do banco de dados Your Savior, que é uma plataforma de associação, classificação e raqueamento de areas com alto risco de assaltos no estado do Espirito Santo. A motivado pela vontade de aprendizado de alunos do IFES (Instituto Federal do Espirito Santo) e pelo serviço que pode ser disponibilizado à população, objetivando assim um aumento na segurança do estado.<br>

###3	MINI-MUNDO<br>
A Secretaria de Segurança Pública do Estado do Espírito Santo (SESP-ES) deseja um sistema de informação para catalogar, classificar e apresentar as áreas de risco de assalto no estado do Espírito Santo. Esse sistema é alimentado através de um banco de dados gerado a partir dos boletins de ocorrência que a Secretaria de Segurança Pública disponibiliza em seu site. Boletins invalidados não deverão ser considerados, juntamente com quaisquer outros boletins que os incidentes iniciais não sejam roubos e furtos.<br>
Sobre os boletins, deseja-se saber: o incidente inicial, data e hora do evento, tipo de local, endereço, bairro, município, quantidade e tipos de itens roubados. Os tipos de locais são classificados em: Via pública, zona rural, comércio, residência e etc. Os boletins computados serão contabilizados aos seus respectivos endereços e tipos de locais.<br>
Os usuários poderão visualizar no mapa a taxa de assalto em uma determinada rua identificando sua cor. Quanto maior o nível de periculosidade da via mais saturada é sua coloração. Além disso, terão acesso a uma página com o ranking dos municípios, bairros e tipos de locais com maior taxa de roubos e furtos. Será possível buscar por regiões e visualizar suas estatísticas de horários mais propícios a assaltos e bens mais roubados, sendo possível comparar regiões diferentes.<br>
Os usuários poderão adicioar Boletins extraoficiais, ou seja, esses boletins não precisam ser validados pela SESP-ES.Tambem poderão pesquisar locais e rotas as quais ele preferir, assim como salvá-los em seu perfil. Ao salvar um local o usuário terá acesso as estatísticas deste local. Sobre os usuários deseja-se saber: Nome, Data de nascimento, Gênero, E-mail, Senha e o Contato. Os usuários deverão ser notificados quando houver uma atualização no banco de dados, seus locais salvos também serão atualizados.<br>
Quando atualizado, o sistema irá gerar novos relatórios contabilizando os itens mais roubados, junto com a taxa de aumento de furtos e roubos dos bairros, dos municípios e do estado. O sistema fornecerá relatórios ao administrador com o aumento da taxa de furtos e roubos, a fim de apresentar a população e a prefeitura, permitindo a população cruzar os dados com os divulgados pelas prefeituras. 
Sobre o administrador, deseja-se saber: o E-mail, Nome, Matricula Funcional, Contato e Senha. O administrador poderá adicionar e remover Boletins e gerar relatórios.<br>

###4	RASCUNHOS BÁSICOS DA INTERFACE (MOCKUPS)<br>
Protótipo do sistema<br>
Esta é uma versão idealizada do sistema montada no Balsamiq Mockups. Mostrando como funcionará sua base, podendo ser alterada no decorrer do projeto.<br>
Neste ponto a codificação não e necessária, somente as ideias de telas devem ser criadas, o princípio aqui é pensar na criação da interface para identificar possíveis informações a serem armazenadas ou descartadas <br>
Link para o [Prototipo](https://github.com/AndyVitoria/trab01/blob/master/Prototipo.pdf)<br>
![Alt text](https://github.com/AndyVitoria/BD1/blob/master/Prototipo_home.jpeg?raw=true "Prototipo Home")

###5	MODELO CONCEITUAL<br>
    5.1 NOTACAO ENTIDADE RELACIONAMENTO
![Alt text](https://github.com/AndyVitoria/trab01/blob/master/CONCEITUAL.jpg?raw=true "Modelo Conceitual")
   
    5.2 NOTACAO UML (Caso esteja fazendo a disciplina de analise)

####5.1 Validação do Modelo Conceitual
    [Grupo01]: Everson Delmaschio
    [Grupo02]: Brendon Mauro

####5.2 DECISÕES DE PROJETO
    A) Herança da tabela de pessoas: Em nosso projeto optamos por usar heranças nas tabelas de usuários e administradores a partir de uma tabela pessoa, isolando assim as caracteristicas semelhantes das duas tabelas em uma só.<br>
    B) Tabelas município e bairro: Em nosso projeto optamos por criar tabelas para municípios e bairros, evitando assim a repetição despendiosa desses campos.<br>
    C) Tabelas de contatos: Em nosso projeto optamos por criar duas tabelas de contato, provendo assim multiplas formas de contatos com multiplos valores.<br>
    D) Tabela de Tipo de local: Em nosso projeto optamos por criar uma tabela contendo os tipos de locais que os crimes ocorreram para evitar a repetição despendiosa desses campos.<br>
    E) Campo origem: Em nosso projeto optamos por usar um campo booleano na tabela boletim para identificar quem o inseriu.<br>

####5.3 DESCRIÇÃO DOS DADOS 
    PESSOA: Tabela que armazena as informações relativas à pessoa.
      nome: campo que armazena o nome para cada pessoa cadastrada no sistema.
      email: campo que armazena o email para cada pessoa cadastrada no sistema.
      senha: campo senha que armazena a senha escolhida por cada pessoa.
      ID: campo que armazena o codigo único de identificação do usuário/administrador.
    
    USUARIO: Tabela que armazena as informações relativas ao usuário.
      data_Nasc: campo que armazena a data de nascimento de cada usuário.
      genero: campo que armazena o gênero de cada usuário.
      data_de_inscricao: campo que armazena a data de inscrição de cada usuário. 
   
    ADMINISTRADOR: Tabela que armazena as informações relativas ao administrador.
      matricula_funcional: campo que armazena o numero da matricula do administrador.
      CPF: campo que armazena o número de Cadastro de Pessoa Física para cada administrador do sistema.

    CONTATO:
      contato_usuario: campo que armazena o contato do usuario. (Ex.: 27 3252-7219)
    
    TIPO_DE_CONTATO:
      codigo_contato: campo que armazena o codigo referente ao tipo de contato.
      tipo_contato: campo que armazena o nome do tipo de conato. (Ex.: Telefone)
    
    ENDERECO: Tabela que armazena as informações sobre o endereço.
      ID: campo que armazena o codigo unico do endereço.
      rua: campo que armazena o nome da rua de cada endereço cadastrado.
      CEP: campo que armazena o Codigo de Endereçamento Postal de cada endereço cadastrado.
    
    Bairro:
      Codigo_bairro: campo que armazena o codigo unico do bairro.
      Nome_bairro: campo que armazena o nome de cada bairro.
     
    Municipio:
      Codigo_municipio: campo que armazena o codigo unico do município.
      Nome_micinipio: campo que armazena o nome de cada município.
    
    LOCAL: Tabela que armazena as informações relativas ao local salvo pelo usuário.
      apelido: campo que armazena o nome fantasia do local, salvo e definido pelo usuário.
      ID_Usuario: campo que armazena o ID do usuário a que este local pertence.
      ID_Local: campo que armazena o codigo único de identificação do local.
    
    ROTA: Tabela que armazena as informações relativas à rota salva pelo usuário.
      apelido: campo que armazena o nome fantasia da rota, salva e definida pelo usuário.
      ID_Rota: campo que armazena o codigo único de identificação da rota.
      ID_Usuario: campo que armazena o ID do usuário a que esta rota pertence.
     
    CAMINHO: Tabela que armazena as informações relativas à ordem da rota salva pelo usuário.
      ordem: Campo que armazena a ordem dos caminhos da rota.
    
    BOLETIM: Tabela que armazena as informações relativas ao boletim.
      ID: campo que armazena o codigo único do boletim, gerado pela policia.
      data: campo que armazena a data de ocorrencia do crime.
      hora: campo que armazena a hora da ocorrencia do crime.
      crime: campo que armazena o tipo de crime cometido.
      origem: campo que indica quem inseriu o boletim. (Ex.: False = Usuário)
      
    ITEM_ROUBADO: Tabela que armazena as informações relativas ao item roubado.
      qtd: campo que armazena a quantidade de itens de cada item roubado.
      item: campo que armazena o nome de cada item roubado.
    
    TIPO_DE_LOCAL: Tabela que armazena as informações relativas ao tipo de local.
      codigo: campo que armazena o codigo único do tipo de local em que o crime ocorreu.
      tipo_local: campo que armazena o tipo de local em que o crime ocorreu.


###6	MODELO LÓGICO<br>
![Alt text](https://github.com/AndyVitoria/trab01/blob/master/LOGICO.jpg?raw=true "Modelo Lógico")

###7	MODELO FÍSICO<br>
    -- Geração de Modelo físico
    -- Sql ANSI 2003 - brModelo.

    CREATE TABLE PESSOA (
        Email VARCHAR(250),
        ID SERIAL PRIMARY KEY,
        Nome VARCHAR(250),
        Senha VARCHAR(50)
    );

    CREATE TABLE Contato (
        Contato_Usuario VARCHAR(250),
        ID SERIAL,
        Codigo_contato SERIAL,
        FOREIGN KEY(ID) REFERENCES PESSOA (ID)
    );

    CREATE TABLE TIPO_DE_CONTATO (
        Tipo_Contato VARCHAR(150),
        Codigo_contato SERIAL PRIMARY KEY
    );

    CREATE TABLE USUARIO (
        Data_Nasc DATE,
        Data_de_inscricao DATE,
        Genero CHAR(1),
        ID SERIAL,
        FOREIGN KEY(ID) REFERENCES PESSOA (ID)
    );

    CREATE TABLE ROTA (
        ID_Rota SERIAL PRIMARY KEY,
        Apelido VARCHAR(250),
        ID_Usuario INTEGER
    );

    CREATE TABLE LOCAL (
        ID_Local SERIAL PRIMARY KEY,
        ID_Usuario INTEGER,
        Apelido VARCHAR(250),
        ID_Endereco INTEGER
    );

    CREATE TABLE ENDERECO (
        ID_Endereco INTEGER PRIMARY KEY,
        Rua VARCHAR(250),
        CEP INTEGER,
        Codigo_bairro INTEGER
    );

    CREATE TABLE CAMINHO (
        Ordem INTEGER,
        ID_Endereco INTEGER,
        ID_Rota SERIAL,
        FOREIGN KEY(ID_Endereco) REFERENCES ENDERECO (ID_Endereco),
        FOREIGN KEY(ID_Rota) REFERENCES ROTA (ID_Rota)
    );

    CREATE TABLE ITEM_ROUBADO (
        Qtd INTEGER,
        Item VARCHAR(250),
        ID_Boletim INTEGER
    );

    CREATE TABLE TIPO_DE_LOCAL (
        Tipo_local VARCHAR(150),
        Codigo SERIAL PRIMARY KEY
    );

    CREATE TABLE ADMINISTRADOR (
        CPF INTEGER,
        Matricula_funcional VARCHAR(25),
        ID SERIAL,
        FOREIGN KEY(ID) REFERENCES PESSOA (ID)
    );

    CREATE TABLE BOLETIM (
        Data DATE,
        Hora TIME,
        Crime VARCHAR(10),
        ID_Boletim INTEGER PRIMARY KEY,
        ID_Endereco INTEGER,
        Codigo SERIAL,
        ID SERIAL,
        Origem BOOLEAN,
        FOREIGN KEY(ID_Endereco) REFERENCES ENDERECO (ID_Endereco),
        FOREIGN KEY(Codigo) REFERENCES TIPO_DE_LOCAL (Codigo),
        FOREIGN KEY(ID) REFERENCES PESSOA (ID)
    );

    CREATE TABLE BAIRRO (
        Codigo_bairro INTEGER PRIMARY KEY,
        Nome_bairro VARCHAR(250),
        Codigo_municipio INTEGER
    );

    CREATE TABLE MUNICIPIO (
        Codigo_municipio INTEGER PRIMARY KEY,
        Nome_municipio VARCHAR(250)
    );

    ALTER TABLE Contato ADD FOREIGN KEY(Codigo_contato) REFERENCES TIPO_DE_CONTATO (Codigo_contato);
    ALTER TABLE LOCAL ADD FOREIGN KEY(ID_Endereco) REFERENCES ENDERECO (ID_Endereco);
    ALTER TABLE ENDERECO ADD FOREIGN KEY(Codigo_bairro) REFERENCES BAIRRO (Codigo_bairro);
    ALTER TABLE ITEM_ROUBADO ADD FOREIGN KEY(ID_Boletim) REFERENCES BOLETIM (ID_Boletim);
    ALTER TABLE BAIRRO ADD FOREIGN KEY(Codigo_municipio) REFERENCES MUNICIPIO (Codigo_municipio);

###8	INSERT APLICADO NAS TABELAS DO BANCO DE DADOS<br>
####8.1 DETALHAMENTO DAS INFORMAÇÕES
Base de dados: A base de dados usada foi retirada do site da Secretaria de Segurança Pública do Espirito Santo. Foram usados 60 lotes de boletins de ocorencia registrados no estado do Espirito Santo.<br>
Ferramentas: Python 3.5, PyPDF, Tabula 0.9.0, Pentaho.

Justificativa: Optamos por usar a Linguagem de Programação Python pela facilidade que esta porporciona na manipulação de expressões regurlares, usamos a biblioteca PyPDF2 para obter o conteudo dos PDF's e assim verificar a validade dos boletins de ocorência, usamos a o núcleo em java da aplicação Tabula que faz manipulação de PDF .<br>

Procedimento Aplicado: Após o processo de eliminação dos boletins inválidos ou que não pertenciam a categoria de roubo, furto ou tentativa de roubo, fora feito uma integração entre um algoritmo feito em Python pelo grupo e  o núcleo da aplicação Tabula, este algoritmo fez a conversão dos  PDF's para CSV, uma vez que não foi possivel usar o PyPDF2 para extração dos conteudos, apenas para verificação. Foi aplicado também o conceito de programação paralela usando Threads em Python para acelerar o processo de conversão feito pelo Tabula. Após a conversão foi usado outro algoritmo construido em Python para extrair os dados dos CSV's usando expressões regulares e os compilamos em tabelas com os dados úteis ao propósito.<br>  

Fonte das ferramentas: [Python 3.5](https://www.python.org/), [PyPDF2](https://github.com/mstamy2/PyPDF2), [Tabula 0.9.0](https://github.com/tabulapdf/tabula-java/releases), [Pentaho 6.1](https://sourceforge.net/projects/pentaho/files/Data%20Integration/6.1/).<br>
Fonte da base de dados: [SSP-ES](http://www.sesp.es.gov.br/sitesesp/index.jsp#transparencia.jsp).<br>

####8.2 INCLUSÃO DO SCRIPT PARA CRIAÇÃO DE TABELA E INSERÇÃO DOS DADOS
Usamos a ferramenta Pentaho para converter as informações nas tabelas gerada pelo algoritmo em Python, para o formato adequado a inserção no banco de dados (PostgreSQL), e este fez esta inserção.<br>  
Procedimento para extração dos dados e inserção no Banco de dados: [Clique Aqui](https://github.com/AndyVitoria/trab01/tree/master/Procedimento%20de%20extracao%20dos%20dados).<br>
Script disponivel [aqui](https://github.com/AndyVitoria/trab01/blob/master/script.sql).

###9	TABELAS E PRINCIPAIS CONSULTAS<br>
####9.1	CONSULTAS DAS TABELAS COM TODOS OS DADOS INSERIDOS<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/tabelas)
####9.2	CONSULTAS DAS TABELAS COM FILTROS WHERE<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/consultas/where)
####9.3	CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E CAMPOS RENOMEADOS<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/consultas/logico%2C%20aritmetico%2C%20renomeado)
####9.4	CONSULTAS QUE USAM OPERADORES LIKE<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/consultas/like)
####9.5	ATUALIZAÇÃO E EXCLUSÃO DE DADOS<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/consultas/atualizacao%20e%20exclusao)
####9.6	CONSULTAS COM JUNÇÃO E ORDENAÇÃO<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/consultas/juncao%20e%20ordenacao)
####9.7	CONSULTAS COM GROUP BY<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/consultas/group%20by)
####9.8	CONSULTAS COM LEFT E RIGHT JOIN<br>
####9.9	CONSULTAS COM SELF JOIN E VIEW<br>
####9.10	SUBCONSULTAS<br>
[Tabelas](https://github.com/AndyVitoria/trab01/tree/master/consultas/subconsultas)
###10	ATUALIZAÇÃO DA DOCUMENTAÇÃO DOS SLIDES<br>
###11	DIFICULDADES ENCONTRADAS PELO GRUPO<br>
    1. Construir o Modelo Conceitual;
    2. Encontrar ferramentas para nos auxiliar na extração de dados dos boletins de forma eficaz;
    3. Aprender a usar o Pentaho;
    
###12  FORMATACAO NO GIT: https://help.github.com/articles/basic-writing-and-formatting-syntax/





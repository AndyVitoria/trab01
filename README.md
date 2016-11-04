# TRABALHO 01
Trabalho desenvolvido durante a disciplina de BD1

#Sumário

###1	COMPONENTES<br>
Integrantes do grupo: André Barbosa da Vitória, Juliana Yuri Kanezaki de Souza <br>

###2	INTRODUÇÃO E MOTIVAÇAO<br>
Este documento contém a especificação do projeto do banco de dados Your Savior, que é uma plataforma de associação, classificação e raqueamento de areas com alto risco de assaltos no estado do Espirito Santo. A motivado pela vontade de aprendizado de alunos do IFES (Instituto Federal do Espirito Santo) e pelo serviço que pode ser disponibilizado à população, objetivando assim um aumento na segurança do estado.<br>

###3	MINI-MUNDO<br>
A Secretaria de Segurança Pública do Estado do Espírito Santo deseja um sistema de informação para catalogar, classificar e apresentar as áreas de risco de assalto no estado do Espírito Santo. Esse sistema é alimentado através de um banco de dados gerado a partir dos boletins de ocorrência que a Secretaria de Segurança Pública disponibiliza em seu site. Boletins invalidados não deverão ser considerados, juntamente com quaisquer outros boletins que os incidentes iniciais não sejam roubos e furtos.<br>
Sobre os boletins, deseja-se saber: o incidente inicial, data e hora do evento, tipo de local, endereço, bairro, município, CEP, quantidade e tipos de itens roubados. Os tipos de locais são classificados em: Via pública, zona rural, comércio, residência e etc. Os boletins computados serão contabilizados aos seus respectivos endereços e tipos de locais.<br>
Os usuários poderão visualizar no mapa a taxa de assalto em uma determinada rua identificando sua cor. Quanto maior o nível de periculosidade da via mais saturada é sua coloração. Além disso, terão acesso a uma página com o ranking dos municípios, bairros e tipos de locais com maior taxa de roubos e furtos. Será possível buscar por regiões e visualizar suas estatísticas de horários mais propícios a assaltos e bens mais roubados, sendo possível comparar regiões diferentes.<br>
Os usuários poderão pesquisar locais e rotas as quais ele preferir, assim como salvá-los em seu perfil. Ao salvar um local o usuário terá acesso as estatísticas deste local. Sobre os usuários deseja-se saber: Nome, Data de nascimento, Gênero, E-mail, Senha e o Estado, Município, Bairro, Endereço e Número. Os usuários deverão ser notificados quando houver uma atualização no banco de dados, seus locais salvos também serão atualizados.<br>
Quando atualizado, o sistema irá gerar novos relatórios contabilizando os itens mais roubados, junto com a taxa de aumento de furtos e roubos dos bairros, dos municípios e do estado. O sistema fornecerá relatórios ao administrador com o aumento da taxa de furtos e roubos, a fim de apresentar a população e a prefeitura, permitindo a população cruzar os dados com os divulgados pelas prefeituras. 
Sobre o administrador, deseja-se saber: o E-mail, Nome, ID da empresa e senha. O administrador poderá adicionar e remover outros administradores, adicionar e remover tabelas do banco de dados e gerar relatórios.<br>

###4	RASCUNHOS BÁSICOS DA INTERFACE (MOCKUPS)<br>
Protótipo do sistema<br>
Esta é uma versão idealizada do sistema montada no Balsamiq Mockups. Mostrando como funcionará sua base, podendo ser alterada no decorrer do projeto.<br>
Neste ponto a codificação não e necessária, somente as ideias de telas devem ser criadas, o princípio aqui é pensar na criação da interface para identificar possíveis informações a serem armazenadas ou descartadas <br>
Link: https://drive.google.com/open?id=0B4qAOHMp3wcZUDY0alhuZEdFdWc<br>
![Alt text](https://github.com/AndyVitoria/BD1/blob/master/Prototipo_home.jpeg?raw=true "Prototipo Home")

###5	MODELO CONCEITUAL<br>
    5.1 NOTACAO ENTIDADE RELACIONAMENTO
![Alt text](https://github.com/AndyVitoria/trab01/blob/master/SAVIOR.jpg?raw=true "Modelo Conceitual")
    
    5.2 NOTACAO UML (Caso esteja fazendo a disciplina de analise)

####5.1 Validação do Modelo Conceitual
    [Grupo01]: Everson
    [Grupo02]: Brendon

####5.2 DECISÕES DE PROJETO
    [atributo]: [descrição da decisão]
    
    EXEMPLO:
    a) Campo endereço: em nosso projeto optamos por um campo multivalorado e composto, pois a empresa 
    pode possuir para cada departamento mais de uma localização... 
    b) justifique!

####5.3 DESCRIÇÃO DOS DADOS 
    [objeto]: [descrição do objeto]
    
    EXEMPLO:
    CLIENTE: Tabela que armazena as informações relativas ao cliente<br>
    CPF: campo que armazena o número de Cadastro de Pessoa Física para cada cliente da empresa.<br>


###6	MODELO LÓGICO<br>
###7	MODELO FÍSICO<br>
###8	INSERT APLICADO NAS TABELAS DO BANCO DE DADOS<br>
####8.1 DETALHAMENTO DAS INFORMAÇÕES
        Detalhamento sobre as informações e processo de obtenção ou geração dos dados.
        Referenciar todas as fontes referentes a :
        a) obtenção dos dados
        b) obtenção de códigos reutilizados
        c) fontes de estudo para desenvolvimento do projeto
        
####8.2 INCLUSÃO DO SCRIPT PARA CRIAÇÃO DE TABELA E INSERÇÃO DOS DADOS
        a) inclusão das instruções para criação das tabelas e estruturas de amazenamento do BD
        b) inclusão das instruções de inserção dos dados nas referidas tabelas
        c) inclusão das instruções para execução de outros procedimentos necessários

###9	TABELAS E PRINCIPAIS CONSULTAS<br>
####9.1	CONSULTAS DAS TABELAS COM TODOS OS DADOS INSERIDOS<br>
####9.2	CONSULTAS DAS TABELAS COM FILTROS WHERE<br>
####9.3	CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E CAMPOS RENOMEADOS<br>
####9.4	CONSULTAS QUE USAM OPERADORES LIKE<br>
####9.5	ATUALIZAÇÃO E EXCLUSÃO DE DADOS<br>
####9.6	CONSULTAS COM JUNÇÃO<br>
####9.7	CONSULTAS COM GROUP BY<br>
####9.8	CONSULTAS COM LEFT E RIGHT JOIN<br>
####9.9	CONSULTAS COM SELF JOIN E VIEW<br>
####9.10	SUBCONSULTAS<br>
###10	ATUALIZAÇÃO DA DOCUMENTAÇÃO DOS SLIDES<br>
###11	DIFICULDADES ENCONTRADAS PELO GRUPO<br>
###12  FORMATACAO NO GIT: https://help.github.com/articles/basic-writing-and-formatting-syntax/





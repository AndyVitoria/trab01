###9	TABELAS E PRINCIPAIS CONSULTAS<br>
####9.1	CONSULTAS DAS TABELAS COM TODOS OS DADOS INSERIDOS<br>
SELECT *FROM ADMINISTRADOR;<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Administrador.png "Administrador")<br><br>
SELECT *FROM BAIRRO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Bairro.png "Bairro")<br><br>
SELECT *FROM BOLETIM; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Boletim.png "Boletim")<br><br>
SELECT *FROM CAMINHO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Caminho.png "Caminho")<br><br>
SELECT *FROM CONTATO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Contato.png "Contato")<br><br>
SELECT *FROM ENDERECO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Endereco.png "Endereço")<br><br>
SELECT *FROM ITEM_ROUBADO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Item_roubado.png "Item Roubado")<br><br>
SELECT *FROM LOCAL; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Local.png "Local")<br><br>
SELECT *FROM MUNICIPIO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Municipio.png "Municipio")<br><br>
SELECT *FROM PESSOA; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Pessoa.png "Pessoa")<br><br>
SELECT *FROM ROTA; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Rota.png "Rota")<br><br>
SELECT *FROM TIPO_DE_CONTATO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Tipo_de_contato.png "Tipo de Contato")<br><br>
SELECT *FROM TIPO_DE_CRIME; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Tipo_de_crime.png "Tipo de Crime")<br><br>
SELECT *FROM TIPO_DE_LOCAL; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Tipo_de_local.png "Tipo de Local")<br><br>
SELECT *FROM USUARIO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/tabelas/Usuario.png "Usuario")<br><br>
####9.2	CONSULTAS DAS TABELAS COM FILTROS WHERE<br>
SELECT *FROM USUARIO WHERE GENERO = 'M';<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/where/where1.png)<br><br>
SELECT CRIME, CODIGO, DATA, ID_BOLETIM, FROM BOLETIM WHERE CRIME = 'B01A' AND CODIGO = 26;<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/where/where2.PNG)<br><br>
SELECT *FROM BOLETIM WHERE HORA IS NULL AND ID_ENDERECO > 10000;<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/where/where3.PNG)<br><br>
####9.3	CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E CAMPOS RENOMEADOS<br>
SELECT CURRENT_DATE - DATA_NASC AS QTD_DIAS, EMAIL, NOME, GENERO, ID FROM USUARIO WHERE ID > 1 AND GENERO = 'M';<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/logico%2C%20aritmetico%2C%20renomeado/lar1.png)<br><br>
SELECT CURRENT_DATE - DATA_NASC AS QTD_DIAS, CODIGO AS ID_TIPO_LOCAL, CRIME, HORA FROM BOLETIM WHERE HORA IS NOT NULL OR CRIME = 'B01G';<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/logico%2C%20aritmetico%2C%20renomeado/lar2.png)<br><br>
####9.4	CONSULTAS QUE USAM OPERADORES LIKE<br>
SELECT *FROM TIPO_DE_LOCAL WHERE TIPO_LOCAL LIKE '%AL%';
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/like/like1.PNG)<br><br>
SELECT *FROM TIPO_DE_LOCAL WHERE TIPO_LOCAL LIKE '________';
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/like/like2.PNG)<br><br>
SELECT *FROM TIPO_DE_CRIME WHERE ESPECIFICACAO LIKE '%O';
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/like/like3.PNG)<br><br>
####9.5	ATUALIZAÇÃO E EXCLUSÃO DE DADOS<br>
![Alt Text]()<br><br>
![Alt Text]()<br><br>
![Alt Text]()<br><br>
![Alt Text]()<br><br>
####9.6	CONSULTAS COM JUNÇÃO E ORDENAÇÃO<br>

![Alt Text]()<br><br>

![Alt Text]()<br><br>

![Alt Text]()<br><br>

![Alt Text]()<br><br>

![Alt Text]()<br><br>
![Alt Text]()<br><br>
####9.7	CONSULTAS COM GROUP BY<br>

####9.10	SUBCONSULTAS<br>

![Alt Text]()

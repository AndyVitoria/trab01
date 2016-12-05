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
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/where/where1.png "Where 1")<br><br>

SELECT CRIME, CODIGO, DATA, ID_BOLETIM FROM BOLETIM <br>
WHERE CRIME = 'B01A' AND CODIGO = 26;<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/where/where2.png "Where 2")<br><br>

SELECT *FROM BOLETIM<br> 
WHERE HORA IS NULL AND ID_ENDERECO > 10000;<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/where/where3.png "Where 3")<br><br>

####9.3	CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E CAMPOS RENOMEADOS<br>

SELECT CURRENT_DATE - DATA_NASC AS QTD_DIAS, EMAIL, NOME, GENERO, ID FROM USUARIO<br> 
WHERE ID > 1 AND GENERO = 'M';<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/logico%2C%20aritmetico%2C%20renomeado/lar1.png "LACR 1")<br><br>

SELECT CURRENT_DATE - DATA_NASC AS QTD_DIAS, CODIGO AS ID_TIPO_LOCAL, CRIME, HORA FROM BOLETIM<br> 
WHERE HORA IS NOT NULL OR CRIME = 'B01G';<br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/logico%2C%20aritmetico%2C%20renomeado/lar2.png "LACR 2")<br><br>

####9.4	CONSULTAS QUE USAM OPERADORES LIKE<br>

SELECT *FROM TIPO_DE_LOCAL<br> 
WHERE TIPO_LOCAL LIKE '%AL%';
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/like/like1.png "Like 1")<br><br>

SELECT *FROM TIPO_DE_LOCAL <br>
WHERE TIPO_LOCAL LIKE '________';
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/like/like2.png "Like 2")<br><br>

SELECT *FROM TIPO_DE_CRIME <br>
WHERE ESPECIFICACAO LIKE '%O';
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/like/like3.png "Like 3")<br><br>

####9.5	ATUALIZAÇÃO E EXCLUSÃO DE DADOS<br>

UPDATE BAIRRO2 SET NOME_BAIRRO = 'BAIRRO DAS FLORES' WHERE NOME_BAIRRO = 'FEU ROSA'; <br>
SELECT *FROM BAIRRO2 WHERE NOME_BAIRRO = 'BAIRRO DAS FLORES'; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/atualizacao%20e%20exclusao/ae1.png)<br><br>

UPDATE BAIRRO2 SET CODIGO_MUNICIPIO = 76 WHERE CODIGO_MUNICIPIO = 75; <br>
SELECT *FROM BAIRRO2 ORDER BY CODIGO_MUNICIPIO DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/atualizacao%20e%20exclusao/ae2.png)<br><br>

DELETE FROM BAIRRO2 WHERE CODIGO_MUNICIPIO = 76; <br>
SELECT *FROM BAIRRO2 ORDER BY CODIGO_MUNICIPIO DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/atualizacao%20e%20exclusao/ae3.png)<br><br>

DELETE FROM BAIRRO2 WHERE NOME_BAIRRO LIKE '%SANT_%'; <br>
SELECT *FROM BAIRRO2 ORDER BY CODIGO_MUNICIPIO DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/atualizacao%20e%20exclusao/ae4.png)<br><br>

DELETE FROM BAIRRO2 WHERE NOME_BAIRRO LIKE 'A%'; <br>
SELECT *FROM BAIRRO2 ORDER BY NOME_BAIRRO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/atualizacao%20e%20exclusao/ae5.png)<br><br>

UPDATE BAIRRO2 SET NOME_BAIRRO = 'BAGUEIRA II' WHERE NOME = 'BAGUEIRA'; <br>
SELECT *FROM BAIRRO2 ORDER BY NOME_BAIRRO; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/atualizacao%20e%20exclusao/ae6.png)<br><br>

####9.6	CONSULTAS COM JUNÇÃO E ORDENAÇÃO<br>

SELECT ID_BOLETIM, TC.CRIME, ESPECIFICACAO, TL.TIPO_LOCAL, RUA, NOME_BAIRRO AS BAIRRO, NOME_MUNICIPIO AS MUNICIPIO <br>
FROM BOLETIM <br>
INNER JOIN TIPO_DE_CRIME AS TC ON (TC.CODIGO_CRIME = BOLETIM.CRIME) <br>
INNER JOIN TIPO_DE_LOCAL AS TL ON (TL.CODIGO = BOLETIM.CODIGO) <br>
INNER JOIN ENDERECO AS E ON (E.ID_ENDERECO = BOLETIM.ID_ENDERECO) <br>
INNER JOIN BAIRRO AS B ON (E.CODIGO_BAIRRO = B.CODIGO_BAIRRO) <br>
INNER JOIN MUNICIPIO AS M ON (B.CODIGO_MUNICIPIO = M.CODIGO_MUNICIPIO) <br>
WHERE ESPECIFICACAO IS NOT NULL <br>
ORDER BY ID_BOLETIM; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/juncao%20e%20ordenacao/jo1.png)<br><br>

SELECT BOLETIM.ID_BOLETIM, TC.CRIME, ESPECIFICACAO, TL.TIPO_LOCAL, ITEM, QTD FROM BOLETIM <br>
INNER JOIN TIPO_DE_CRIME AS TC ON (TC.CODIGO_CRIME = BOLETIM.CRIME) <br>
INNER JOIN TIPO_DE_LOCAL AS TL ON (TL.CODIGO = BOLETIM.CODIGO) <br>
INNER JOIN ITEM_ROUBADO AS IR ON (IR.ID_BOLETIM = BOLETIM.ID_BOLETIM) <br>
ORDER BY ID_BOLETIM DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/juncao%20e%20ordenacao/jo2.png)<br><br>

SELECT NOME, TIPO_CONTATO, CONTATO_USUARIO FROM PESSOA <br>
INNER JOIN CONTATO ON (PESSOA.ID = CONTATO.ID) <br>
INNER JOIN TIPO_DE_CONTATO ON (CONTATO.CODIGO_CONTATO = TIPO_DE_CONTATO.CODIGO_CONTATO) <br>
ORDER BY NOME; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/juncao%20e%20ordenacao/jo3.png)<br><br>

SELECT NOME, APELIDO, RUA, NOME_BAIRRO, NOME_MUNICIPIO FROM PESSOA <br>
INNER JOIN LOCAL ON (LOCAL.ID_USUARIO = PESSOA.ID) <br>
INNER JOIN ENDERECO ON (LOCAL.ID_ENDERECO = ENDERECO.ID_ENDERECO) <br>
INNER JOIN BAIRRO ON (BAIRRO.CODIGO_BAIRRO = ENDERECO.CODIGO_BAIRRO) <br>
INNER JOIN MUNICIPIO ON (MUNICIPIO.CODIGO_MUNICIPIO = BAIRRO.CODIGO_MUNICIPIO) <br>
ORDER BY NOME; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/juncao%20e%20ordenacao/jo4.png)<br><br>

SELECT NOME, APELIDO, ORDEM, RUA, NOME_BAIRRO, NOME_MUNICIPIO FROM ROTA <br>
INNER JOIN PESSOA ON (ROTA.ID_USUARIO = PESSOA.ID) <br>
INNER JOIN CAMINHO ON (ROTA.ID_ROTA = CAMINHO.ID_ROTA) <br>
INNER JOIN ENDERECO ON (CAMINHO.ID_ENDERECO = ENDERECO.ID_ENDERECO) <br>
INNER JOIN BAIRRO ON (BAIRRO.CODIGO_BAIRRO = ENDERECO.CODIGO_BAIRRO) <br>
INNER JOIN MUNICIPIO ON (MUNICIPIO.CODIGO_MUNICIPIO = BAIRRO.CODIGO_MUNICIPIO) <br>
ORDER BY NOME, ORDEM; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/juncao%20e%20ordenacao/jo5.png)<br><br>

SELECT ID_BOLETIM, PESSOA.ID, NOME, ORIGEM FROM BOLETIM <br>
INNER JOIN PESSOA ON (BOLETIM.ID = PESSOA.ID) <br>
ORDER BY ID_BOLETIM; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/juncao%20e%20ordenacao/jo6.png)<br><br>

####9.7	CONSULTAS COM GROUP BY<br>

SELECT TL.TIPO_LOCAL, COUNT(*) FROM BOLETIM <br>
INNER JOIN TIPO_DE_LOCAL AS TL ON (TL.CODIGO = BOLETIM.CODIGO) <br>
GROUP BY TL.TIPO_LOCAL <br>
ODER BY COUNT DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/group%20by/gb1.png)<br><br>

SELECT BAIRRO.NOME_BAIRRO, NOME_MUNICIPIO, COUNT(*) FROM BOLETIM <br>
INNER JOIN ENDERECO ON (BOLETIM.ID_ENDERECO = ENDERECO.ID_ENDERECO) <br>
INNER JOIN BAIRRO ON (BAIRRO.CODIGO_BAIRRO = ENDERECO.CODIGO_BAIRRO) <br>
INNER JOIN MUNICIPIO ON (MUNICIPIO.CODIGO_MUNICIPIO = BAIRRO.CODIGO_MUNICIPIO) <br>
GROUP BY NOME_BAIRRO, NOME_MUNICIPIO  <br>
ORDER BY COUNT DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/group%20by/gb2.png)<br><br>

SELECT NOME_MUNICIPIO, COUNT(*) FROM BOLETIM <br>
INNER JOIN ENDERECO ON (BOLETIM.ID_ENDERECO = ENDERECO.ID_ENDERECO) <br>
INNER JOIN BAIRRO ON (BAIRRO.CODIGO_BAIRRO = ENDERECO.CODIGO_BAIRRO) <br>
INNER JOIN MUNICIPIO ON (MUNICIPIO.CODIGO_MUNICIPIO = BAIRRO.CODIGO_MUNICIPIO) <br>
GROUP BY NOME_MUNICIPIO  <br>
ORDER BY COUNT DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/group%20by/gb3.png)<br><br>

SELECT RUA, BAIRRO.NOME_BAIRRO, NOME_MUNICIPIO, COUNT(*) FROM BOLETIM <br>
INNER JOIN ENDERECO ON (BOLETIM.ID_ENDERECO = ENDERECO.ID_ENDERECO) <br>
INNER JOIN BAIRRO ON (BAIRRO.CODIGO_BAIRRO = ENDERECO.CODIGO_BAIRRO) <br>
INNER JOIN MUNICIPIO ON (MUNICIPIO.CODIGO_MUNICIPIO = BAIRRO.CODIGO_MUNICIPIO) <br>
WHERE RUA IS NOT NULL <br>
GROUP BY RUA, BAIRRO.NOME_BAIRRO, NOME_MUNICIPIO <br>
ORDER BY COUNT DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/group%20by/gb4.png)<br><br>

SELECT ITEM, SUM(QTD) AS QTD_ITEM FROM ITEM_ROUBADO <br>
GROUP BY ITEM  <br>
ORDER BY QTD_ITEM DESC; <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/group%20by/gb5.png)<br><br>

####9.10	SUBCONSULTAS<br>

SELECT *FROM ITEM_ROUBADO <br>
WHERE ITEM IN (SELECT DISTINCT ITEM FROM ITEM_ROUBADO WHERE ITEM <> 'CARTAO'); <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/subconsultas/sub1.png)<br><br>

SELECT *FROM MUNICIPIO <br>
WHERE NOME_MUNICIPIO NOT IN (SELECT NOME_MUNICIPIO LIKE '%A%'); <br>
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/subconsultas/sub2.png)<br><br>

SELECT *FROM BAIRRO
WHERE NOME_BAIRRO IN (SELECT NOME_BAIRRO FROM BAIRRO WHERE NOME_BAIRRO LIKE 'C%');
![Alt Text](https://github.com/AndyVitoria/trab01/blob/master/consultas/subconsultas/sub3.png)<br><br>


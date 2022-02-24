CREATE FUNCTION retornaProximaData(@data datetimeoffset, @cliente_id int)
RETURNS datetimeoffset
AS
BEGIN
	DECLARE @proxData datetimeoffset;
	SELECT @proxData =  MIN(DATA) 
	FROM [dbo].[TRANSACOES] 
	WHERE DATA > @data and CLIENTE_ID = @cliente_id and VALOR < 0
	RETURN @proxData;
END;
--drop function retornaProximaData

CREATE FUNCTION fraude(@data datetimeoffset,@data2 datetimeoffset)
RETURNS varchar(50)
AS
BEGIN
	IF @data IS NULL OR @data2 IS NULL
		RETURN 'Falha em analisar'
	ELSE
		IF DATEDIFF(second, @data, @data2) < 120
			RETURN 'Fraude'
		ELSE
			RETURN 'Transação Comum'
	RETURN 'Não analisado'
END;

CREATE VIEW TRANSACOES_STATUS AS 
SELECT  ID, 
		CLIENTE_ID, 
		DATA,
		VALOR, 
		DBO.retornaProximaData(DATA, CLIENTE_ID) as DATA_COMPARADA, 
		dbo.fraude(DATA, DBO.retornaProximaData(DATA, CLIENTE_ID) ) AS STATUS
FROM TRANSACOES
WHERE VALOR < 0;

SELECT DISTINCT CLIENTE_ID, 
				C.NOME 
FROM TRANSACOES_STATUS TS
INNER JOIN CLIENTES c on C.ID = TS.CLIENTE_ID
WHERE STATUS = 'Fraude';  --Retorna o id e nome dos cliente que sofreram fraude

SELECT DISTINCT T.CLIENTE_ID, 
				C.NOME, 	
				COUNT(T.ID) AS TRANSACOES , 
				COUNT(CASE WHEN STATUS = 'Fraude' THEN 1 END ) as TRANSACOES_FRAUDE
FROM TRANSACOES T
LEFT JOIN TRANSACOES_STATUS TS ON TS.ID = T.ID
INNER JOIN CLIENTES C on C.ID = TS.CLIENTE_ID
WHERE T.VALOR < 0 
GROUP BY T.cliente_id, C.NOME
ORDER BY T.CLIENTE_ID;  --Retorna o id e nome de todos os clientes e informa a qtd de transacoes deles e quantas são fraude

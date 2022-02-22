CREATE FUNCTION retornaProximaData(@data datetimeoffset, @cliente_id int)
RETURNS datetimeoffset
AS
BEGIN
	DECLARE @proxData datetimeoffset;
	select @proxData =  MIN(DATA) 
	from [dbo].[TRANSACOES] 
	where data > @data and cliente_id = @cliente_id
	RETURN @proxData;
END;
--drop function retornaProximaData
--oi
CREATE FUNCTION fraude(@data datetimeoffset,@data2 datetimeoffset)
RETURNS varchar(50)
AS
BEGIN
	IF @data is null or @data2 is null
		RETURN 'Falha em analisar'
	ELSE
		IF DATEDIFF(second, @data, @data2) <= 120
			RETURN 'Fraude'
		ELSE
			RETURN 'Transação Comum'
	RETURN 'Não analisado'
END;

create view transacoes_status as 
SELECT id, cliente_id, data,valor, DBO.retornaProximaData(data, cliente_id) as prox, dbo.fraude(data, DBO.retornaProximaData(data, cliente_id) ) as Status
from transacoes;

select distinct cliente_id, c.nome from transacoes_status ts
left join CLIENTES c on c.id = ts.cliente_id
where status = 'Fraude'



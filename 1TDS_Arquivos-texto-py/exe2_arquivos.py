import oracledb as db

user = "rm98837"
pwd = "280101"
url = "oracle.fiap.com.br/orcl"

try:
    lista = []
    with open ('faturamento.txt', 'r') as file:
        for lin in file:
            dado = lin.replace("\n", "").split(';')
            dic = {
                "prod": dado[0],
                "marca": dado[1],
                "loja": dado[2],
                "data": dado[3],
                "qtd": int(dado[4]),
                "valor": float(dado[5])
            }
            
            lista.append(dic)

    print(lista)
    with db.connect (user=user, password=pwd, dsn=url) as con:
        sql = """INSERT INTO faturamento_tdpj (id, produto, marca, loja, data, qtd, valor)
         VALUES (gerador_id.nextval, :prod, :marca, :loja, TO_DATE(:data, 'YYYY-MM-DD'), :qtd, :valor)"""
        with con.cursor() as cur:
            for reg in lista:
                cur.execute(sql, reg)
        con.commit()

    print("Registros inseridos")

except Exception as erro:
    print(erro) 

from sqlalchemy import create_engine
from urllib.parse import quote_plus
import os

def conexion (user:str,password:str,server:str,bdd:str):
    parametro = quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={bdd};"
        f"UID={user};"
        f"PWD={password};"
    )
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={parametro}",
                            fast_executemany=True)
    return engine


def get_engine () ->object:
    user1 = os.getenv("DB_USER_BDD1")
    pass1 = os.getenv("DB_PASS_BDD1")


    server1 = os.getenv("BDD1")
    server2 = os.getenv("BDD2")
    
    
    Bases = [
        "bait",
        "Renovaciones",
        "pospago",
        "prepago",
        "upsell",
        "Comisiones",
        "backoffice"
    ]

    opciones = list(Bases)

    bdd = opciones[7-1]


    engine = conexion(user=user1, password=pass1, server=server1, bdd=bdd)
    print(f"\n✅ Conectado a '{bdd}'")
    return engine

#if __name__ == "__main__":
#    engine = get_engine()
    
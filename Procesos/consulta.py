
from sqlalchemy import Engine,text
import pandas as pd


def usuarios_tlmk (engine:Engine)-> pd.DataFrame:
    consulta = """
    select  id_usuario,isnull(apellidos+' ' +name,'Prueba') as nombre, usuarioTlmk,a.password,Estatus_Tlmk from usuariosTlmk a
    left join  gc_wfm.dbo.users b on id_hr = usuarioNomina
    where Estatus_Tlmk = 0
    order by id desc
    """
    df = pd.read_sql(text(consulta),engine)
    return df

def actualiza_tlmk(engine: Engine, id: int):
    update = """
    UPDATE backoffice.dbo.usuariosTlmk
    SET Estatus_Tlmk = 1, updated_at = getdate()
    WHERE id_usuario = :id
    """
    with engine.connect() as conn:
        conn.execute(text(update), {"id": id})
        conn.commit()












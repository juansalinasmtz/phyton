from fastapi import FastAPI
from Procesos.conexion import get_engine
from Procesos.consulta import usuarios_tlmk
from Procesos.pagina import Acceso_tlmk,cierre_pagina,crear_usuarios
from dotenv import load_dotenv
import os


load_dotenv()

app = FastAPI()

@app.post("/ejecutar-usuarios")
def main ():
    engine = get_engine()
    user_tlmk= usuarios_tlmk(engine)
    usuario = os.getenv("APP_USER1")
    password = os.getenv("APP_PASS1")

    procesados = []
    errores = []

    print(user_tlmk)

    playwright,browser,page = Acceso_tlmk(usuario,password)

    try:
        for row in user_tlmk.itertuples():
            crear_usuarios(
                page=page,
                usuariotlmk=row.usuarioTlmk,
                nombre=row.nombre,
                password=row.password,
                id_usuario=row.id_usuario,
                engine=engine
            )
            procesados.append(row.usuarioTlmk)
    except Exception as e:
        errores.append(str(e))
    finally:
        cierre_pagina(browser=browser, playwright=playwright)

    return{
        "procesados":len(procesados),
        "usuarios":procesados,
        "errores": errores
    }

if __name__ == '__main__':
    main()
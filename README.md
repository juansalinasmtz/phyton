# Usuarios TLMK

Automatización para la creación de usuarios en el sistema Telemarketing.
Consulta usuarios pendientes en SQL Server y los crea automáticamente 
mediante Playwright.

## Tecnologías
- Python
- SQLAlchemy
- Playwright
- Pandas
- FastAPI

## Instalación
1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Instalar playwright: `playwright install chromium`
4. Copiar `.env.example` a `.env` y rellenar con tus credenciales

## Uso
```bash
python main.py
```

## Estructura
- `main.py` — Orquestador principal
- `Procesos/conexion.py` — Conexión a base de datos
- `Procesos/consulta.py` — Queries SQL
- `Procesos/pagina.py` — Automatización web con Playwright
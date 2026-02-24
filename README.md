# Reporte de antenas de telecomunicaciones automatizado

Script automatizado en Python diseñado para la monitorización de infraestructura de telecomunicaciones. El script realiza consultas iterativas a una base de datos para identificar antenas activas y generar reportes de estado.

## Funcionalidades Técnicas

* **Automatización de consultas**: Extracción de antenas de telecomunicacines activas.

* **Generación de Logs**: Sistema de registro de historicos con reporte de antenas activas.

## Estrucutra del Script

* **main.py**: Lógica central y flujo de ejecución del script.
* **model/**: Conexión y consultas a la base de datos.
* **requirements.txt**: Dependencias mínimas necesarias.

## Uso

1. **Configuración**: Editar model/conexion_db.py con las credenciales de acceso a la base de datos.

2. **Entorno virtual**:

    linux:

    ```
    python3 -m venv /path/to/new/virtual/environment 
    ```

    Windows:
    
    ```
    python -m venv /path/to/new/virtual/environment
    ```

3. **Instalar dependencias:**

    ```
    pip install -r requirements.txt

    ```

4. Ejecutar main.py

    linux:

    ```
    python3 main.py
    ```

    Windows:
    
    ```
    python main.py
    ```

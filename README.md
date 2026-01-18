# Empleotronix

Aplicación web para visualizar datos de empleados construida con Streamlit.

## Ejecutar localmente

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```

## Despliegue en Streamlit Cloud

Para desplegar esta aplicación y hacerla pública:

1. **Subir a GitHub**:
   - Crea un nuevo repositorio en GitHub.
   - Sigue las instrucciones para subir tu código existente:
     ```bash
     git remote add origin <URL_DE_TU_REPOSITORIO>
     git branch -M main
     git push -u origin main
     ```

2. **Conectar con Streamlit Cloud**:
   - Ve a [share.streamlit.io](https://share.streamlit.io/).
   - Inicia sesión con tu cuenta de GitHub.
   - Haz clic en "New app".
   - Selecciona tu repositorio, la rama (main) y el archivo principal (`app.py`).
   - Haz clic en "Deploy".

¡Tu aplicación estará lista en unos minutos!

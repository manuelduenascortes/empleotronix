import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración básica de la página
st.set_page_config(page_title="Empleotronix", layout="centered")

# Título y descripción
st.title("EMPLEOTRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Carga de datos con cache para optimizar rendimiento
@st.cache_data
def load_data():
    df = pd.read_csv("employees.csv")
    return df

try:
    # Cargar datos del archivo
    df = load_data()
    
    # Mostrar dataframe
    st.dataframe(df)

    st.write("---")

    # Controles en columnas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Selector de color
        color = st.color_picker("Elige un color para las barras", "#0099C6")
    
    with col2:
        # Switch para mostrar nombres
        show_name = st.toggle("Mostrar el nombre", value=True)
    
    with col3:
        # Switch para mostrar sueldo
        show_salary = st.toggle("Mostrar sueldo en la barra", value=False)

    # Configuración del gráfico
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Eje Y con rango de empleados
    y_pos = range(len(df))
    bars = ax.barh(y_pos, df['salary'], color=color)
    
    # Configuración de ejes
    if show_name:
        ax.set_yticks(y_pos)
        ax.set_yticklabels(df['full name'])
    else:
        ax.set_yticks([])
        
    ax.set_xlabel('Salary')
    
    # Etiquetas de datos en las barras
    if show_salary:
        ax.bar_label(bars, fmt='%d', padding=3)

    # Ajuste de diseño
    plt.tight_layout()
    
    # Renderizado del gráfico
    st.pyplot(fig)

except FileNotFoundError:
    st.error("El archivo employees.csv no se encuentra.")
except Exception as e:
    st.error(f"Error: {e}")

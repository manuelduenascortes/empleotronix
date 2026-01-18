import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Empleotronix", layout="centered")

# Title and description
st.title("EMPLEOTRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("employees.csv")
    return df

try:
    df = load_data()
    
    # Display dataframe
    st.dataframe(df)

    st.write("---")

    # Controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        color = st.color_picker("Elige un color para las barras", "#0099C6")
    
    with col2:
        show_name = st.toggle("Mostrar el nombre", value=True)
    
    with col3:
        show_salary = st.toggle("Mostrar sueldo en la barra", value=False)

    # Chart
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create horizontal bars
    y_pos = range(len(df))
    bars = ax.barh(y_pos, df['salary'], color=color)
    
    # Customize axes
    if show_name:
        ax.set_yticks(y_pos)
        ax.set_yticklabels(df['full name'])
    else:
        ax.set_yticks([])
        
    ax.set_xlabel('Salary')
    
    # Add values to bars if toggled
    if show_salary:
        ax.bar_label(bars, fmt='%d', padding=3)

    # Adjust layout
    plt.tight_layout()
    
    # Display chart
    st.pyplot(fig)

except FileNotFoundError:
    st.error("El archivo employees.csv no se encuentra. Por favor, asegúrate de que existe en el directorio.")
except Exception as e:
    st.error(f"Ocurrió un error: {e}")

import streamlit as st

from src.carga_datos import cargar_csv
from src.dashboard import mostrar_dashboard
from src.tabla_datos import mostrar_tabla_datos


RUTA_CSV = "data/penguins.csv"


st.set_page_config(
    page_title="Dashboard Penguins - GitFlow",
    page_icon="🐧",
    layout="wide"
)


st.title("🐧 Análisis de Datos Penguins")
st.markdown(
    """
    Aplicación desarrollada en **Streamlit** para analizar datos de pingüinos,
    aplicando una estrategia de control de versiones basada en **GitFlow**.
    """
)


try:
    df = cargar_csv(RUTA_CSV)

    st.success("Archivo penguins.csv cargado y validado correctamente.")

    menu = st.sidebar.radio(
        "Menú de navegación",
        [
            "Dashboard principal",
            "Visualización tabular"
        ]
    )

    if menu == "Dashboard principal":
        mostrar_dashboard(df)

    elif menu == "Visualización tabular":
        mostrar_tabla_datos(df)

except Exception as error:
    st.error(f"Error al cargar la aplicación: {error}")

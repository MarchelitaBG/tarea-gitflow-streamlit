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

    st.sidebar.header("Filtros de análisis")

    especies = ["Todas"] + sorted(df["species"].dropna().unique().tolist())
    islas = ["Todas"] + sorted(df["island"].dropna().unique().tolist())

    especie_seleccionada = st.sidebar.selectbox("Filtrar por especie", especies)
    isla_seleccionada = st.sidebar.selectbox("Filtrar por isla", islas)

    df_filtrado = df.copy()

    if especie_seleccionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado["species"] == especie_seleccionada]

    if isla_seleccionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado["island"] == isla_seleccionada]

    st.sidebar.info(f"Registros filtrados: {len(df_filtrado)}")

    menu = st.sidebar.radio(
        "Menú de navegación",
        [
            "Dashboard principal",
            "Visualización tabular",
            "Estadísticas descriptivas"
        ]
    )

    if df_filtrado.empty:
        st.warning("No existen registros para los filtros seleccionados.")
    else:
        if menu == "Dashboard principal":
            mostrar_dashboard(df_filtrado)

        elif menu == "Visualización tabular":
            mostrar_tabla_datos(df_filtrado)

        elif menu == "Estadísticas descriptivas":
            st.subheader("Estadísticas descriptivas")
            st.write("Resumen estadístico de las variables numéricas del conjunto de datos filtrado.")
            st.dataframe(
                df_filtrado.describe(),
                use_container_width=True
            )

except Exception as error:
    st.error(f"Error al cargar la aplicación: {error}")

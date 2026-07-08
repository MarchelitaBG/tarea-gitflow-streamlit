import streamlit as st
import pandas as pd


def mostrar_tabla_datos(df: pd.DataFrame) -> None:
    st.subheader("Visualización tabular de datos")

    st.write("Registros cargados desde el archivo penguins.csv.")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.info(f"Total de registros visualizados: {len(df)}")

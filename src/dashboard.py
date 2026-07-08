import streamlit as st
import pandas as pd
import plotly.express as px


def mostrar_metricas_generales(df: pd.DataFrame) -> None:
    total_registros = len(df)
    total_especies = df["species"].nunique()
    total_islas = df["island"].nunique()
    promedio_masa = round(df["body_mass_g"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total registros", total_registros)
    col2.metric("Especies", total_especies)
    col3.metric("Islas", total_islas)
    col4.metric("Masa promedio", f"{promedio_masa} g")


def mostrar_graficos(df: pd.DataFrame) -> None:
    st.subheader("Dashboard de análisis de pingüinos")

    conteo_especies = df.groupby("species").size().reset_index(name="cantidad")
    fig_especies = px.bar(
        conteo_especies,
        x="species",
        y="cantidad",
        title="Cantidad de pingüinos por especie",
        labels={
            "species": "Especie",
            "cantidad": "Cantidad"
        }
    )
    st.plotly_chart(fig_especies, use_container_width=True)

    fig_masa = px.box(
        df,
        x="species",
        y="body_mass_g",
        title="Distribución de masa corporal por especie",
        labels={
            "species": "Especie",
            "body_mass_g": "Masa corporal (g)"
        }
    )
    st.plotly_chart(fig_masa, use_container_width=True)

    fig_dispersion = px.scatter(
        df,
        x="bill_length_mm",
        y="bill_depth_mm",
        color="species",
        size="body_mass_g",
        title="Relación entre longitud y profundidad del pico",
        labels={
            "bill_length_mm": "Longitud del pico (mm)",
            "bill_depth_mm": "Profundidad del pico (mm)",
            "species": "Especie",
            "body_mass_g": "Masa corporal (g)"
        }
    )
    st.plotly_chart(fig_dispersion, use_container_width=True)


def mostrar_dashboard(df: pd.DataFrame) -> None:
    mostrar_metricas_generales(df)
    mostrar_graficos(df)

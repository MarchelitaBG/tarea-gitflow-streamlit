import os
import pandas as pd


COLUMNAS_REQUERIDAS = [
    "species",
    "island",
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex"
]


def validar_extension_csv(ruta_archivo: str) -> bool:
    return ruta_archivo.lower().endswith(".csv")


def validar_existencia_archivo(ruta_archivo: str) -> bool:
    return os.path.exists(ruta_archivo)


def validar_archivo_no_vacio(ruta_archivo: str) -> bool:
    return os.path.getsize(ruta_archivo) > 0


def validar_columnas_requeridas(df: pd.DataFrame) -> bool:
    return all(columna in df.columns for columna in COLUMNAS_REQUERIDAS)


def validar_dataframe_no_vacio(df: pd.DataFrame) -> bool:
    return not df.empty

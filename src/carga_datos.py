import pandas as pd

from src.validaciones import (
    validar_extension_csv,
    validar_existencia_archivo,
    validar_archivo_no_vacio,
    validar_columnas_requeridas,
    validar_dataframe_no_vacio,
)


def cargar_csv(ruta_archivo: str) -> pd.DataFrame:
    if not validar_extension_csv(ruta_archivo):
        raise ValueError("El archivo debe tener extensión CSV.")

    if not validar_existencia_archivo(ruta_archivo):
        raise FileNotFoundError("El archivo no existe.")

    if not validar_archivo_no_vacio(ruta_archivo):
        raise ValueError("El archivo CSV está vacío.")

    df = pd.read_csv(ruta_archivo)

    if not validar_dataframe_no_vacio(df):
        raise ValueError("El archivo no contiene registros.")

    if not validar_columnas_requeridas(df):
        raise ValueError("El archivo no contiene las columnas requeridas.")

    return df

import pandas as pd
import pytest

from src.validaciones import (
    validar_extension_csv,
    validar_existencia_archivo,
    validar_archivo_no_vacio,
    validar_columnas_requeridas,
    validar_dataframe_no_vacio,
)

from src.carga_datos import cargar_csv


def test_validar_extension_csv_correcta():
    assert validar_extension_csv("penguins.csv") is True


def test_validar_extension_csv_incorrecta():
    assert validar_extension_csv("penguins.xlsx") is False


def test_validar_existencia_archivo():
    assert validar_existencia_archivo("data/penguins.csv") is True


def test_validar_archivo_no_vacio():
    assert validar_archivo_no_vacio("data/penguins.csv") is True


def test_validar_columnas_requeridas():
    df = pd.DataFrame({
        "species": ["Adelie"],
        "island": ["Torgersen"],
        "bill_length_mm": [39.1],
        "bill_depth_mm": [18.7],
        "flipper_length_mm": [181],
        "body_mass_g": [3750],
        "sex": ["male"]
    })

    assert validar_columnas_requeridas(df) is True


def test_validar_columnas_requeridas_faltantes():
    df = pd.DataFrame({
        "species": ["Adelie"],
        "island": ["Torgersen"]
    })

    assert validar_columnas_requeridas(df) is False


def test_validar_dataframe_no_vacio():
    df = pd.DataFrame({"species": ["Adelie"]})
    assert validar_dataframe_no_vacio(df) is True


def test_validar_dataframe_vacio():
    df = pd.DataFrame()
    assert validar_dataframe_no_vacio(df) is False


def test_cargar_csv_correctamente():
    df = cargar_csv("data/penguins.csv")
    assert len(df) == 40
    assert "species" in df.columns
    assert "body_mass_g" in df.columns


def test_cargar_csv_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        cargar_csv("data/no_existe.csv")


def test_cargar_csv_extension_incorrecta():
    with pytest.raises(ValueError):
        cargar_csv("data/penguins.xlsx")

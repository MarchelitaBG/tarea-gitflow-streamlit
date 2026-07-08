# 🐧 Dashboard Penguins con Streamlit y GitFlow

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-red)
![Pytest](https://img.shields.io/badge/Pytest-8.4-green)
![GitFlow](https://img.shields.io/badge/GitFlow-Implementado-orange)
![Release](https://img.shields.io/badge/Release-v1.0.0-purple)

---

## 📌 Descripción

**Dashboard Penguins con Streamlit y GitFlow** es una aplicación web desarrollada en Python para el análisis visual del dataset `penguins.csv`.

El proyecto permite validar, cargar, visualizar y analizar información del conjunto de datos **Palmer Penguins**, aplicando una estrategia formal de control de versiones basada en **GitFlow**.

La solución incorpora:

- Validaciones de archivo CSV.
- Carga controlada de datos.
- Dashboard interactivo.
- Visualización tabular.
- Filtros por especie e isla.
- Estadísticas descriptivas.
- Pruebas automatizadas con Pytest.
- Versionamiento con ramas `main`, `develop`, `feature/*`, `release/*` y tag `v1.0.0`.

---

## 🎯 Objetivo General

Desarrollar una aplicación web con **Streamlit** para el análisis visual del dataset `penguins.csv`, aplicando la metodología **GitFlow** durante el ciclo de desarrollo, integración, pruebas y liberación de la versión estable.

---

## ✅ Objetivos Específicos

- Implementar funciones de validación para archivos CSV.
- Construir una aplicación principal en Streamlit.
- Visualizar datos mediante gráficos interactivos.
- Incorporar visualización tabular del dataset.
- Agregar filtros dinámicos por especie e isla.
- Crear pruebas unitarias con Pytest.
- Gestionar el desarrollo mediante GitFlow.
- Publicar el repositorio en GitHub con ramas y tags.

---

## 🧰 Tecnologías Utilizadas

| Tecnología | Versión / Referencia | Uso dentro del proyecto |
|---|---:|---|
| Python | 3.9 | Lenguaje principal |
| Streamlit | 1.50 | Framework web para el dashboard |
| Pandas | 2.x | Lectura y procesamiento de datos |
| Plotly | 5.x | Gráficos interactivos |
| Pytest | 8.4 | Pruebas unitarias |
| Git | 2.52 | Control de versiones |
| GitHub | Cloud | Repositorio remoto |
| AlmaLinux | 9.7 | Máquina virtual de desarrollo |

---

## 🏗️ Arquitectura del Sistema

```text
Usuario
   │
   ▼
Navegador Web
   │
   ▼
app.py
   │
   ├── dashboard.py
   ├── tabla_datos.py
   ├── carga_datos.py
   └── validaciones.py
           │
           ▼
      data/penguins.csv
```

La arquitectura es modular. Cada archivo tiene una responsabilidad específica, facilitando el mantenimiento, las pruebas y la documentación.

---

## 📂 Estructura del Proyecto

```text
tarea-gitflow-streamlit/
├── app.py
├── README.md
├── informe.md
├── requirements.txt
├── data/
│   └── penguins.csv
├── src/
│   ├── validaciones.py
│   ├── carga_datos.py
│   ├── dashboard.py
│   └── tabla_datos.py
├── tests/
│   └── test_validaciones.py
└── docs/
    └── capturas/
```

| Carpeta / Archivo | Descripción |
|---|---|
| `app.py` | Aplicación principal de Streamlit |
| `data/penguins.csv` | Dataset utilizado para el análisis |
| `src/validaciones.py` | Funciones de validación |
| `src/carga_datos.py` | Carga validada del CSV |
| `src/dashboard.py` | Métricas y gráficos |
| `src/tabla_datos.py` | Visualización tabular |
| `tests/test_validaciones.py` | Pruebas unitarias |
| `requirements.txt` | Dependencias del proyecto |
| `docs/capturas/` | Evidencias visuales |

---

## 🌳 GitFlow Aplicado

El proyecto fue desarrollado utilizando una estrategia GitFlow con ramas especializadas para cada etapa.

```text
main
 │
 └── develop
       ├── feature/validaciones
       ├── feature/carga-datos
       ├── feature/tabla-datos
       ├── feature/dashboard
       ├── feature/app-streamlit
       ├── feature/pruebas-pytest
       ├── feature/filtros-dashboard
       └── release/v1.0.0
              └── merge a main + tag v1.0.0
```

### Ramas utilizadas

| Rama | Propósito |
|---|---|
| `main` | Versión estable |
| `develop` | Integración de funcionalidades |
| `feature/validaciones` | Funciones de validación |
| `feature/carga-datos` | Carga del dataset |
| `feature/tabla-datos` | Visualización tabular |
| `feature/dashboard` | Gráficos y métricas |
| `feature/app-streamlit` | Aplicación principal |
| `feature/pruebas-pytest` | Pruebas automatizadas |
| `feature/filtros-dashboard` | Filtros y estadísticas |
| `release/v1.0.0` | Preparación de versión estable |

---

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/cefer181/tarea-gitflow-streamlit.git
cd tarea-gitflow-streamlit
```

Crear y activar entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8503
```

Abrir en el navegador:

```text
http://IP_SERVIDOR:8503
```

---

## 📊 Funcionalidades

### Dashboard principal

Incluye indicadores generales:

- Total de registros.
- Total de especies.
- Total de islas.
- Masa corporal promedio.

### Gráficos interactivos

- Cantidad de pingüinos por especie.
- Distribución de masa corporal por especie.
- Relación entre longitud y profundidad del pico.

### Visualización tabular

Permite revisar directamente los registros cargados desde `penguins.csv`.

### Filtros

Permite filtrar por:

- Especie.
- Isla.

### Estadísticas descriptivas

Presenta valores como:

- Conteo.
- Promedio.
- Desviación estándar.
- Mínimo.
- Máximo.
- Percentiles.

---

## 🧪 Pruebas Automatizadas

Ejecutar:

```bash
pytest -v
```

Resultado esperado:

```text
11 passed
```

Las pruebas validan:

- Extensión `.csv`.
- Existencia del archivo.
- Archivo no vacío.
- Columnas requeridas.
- DataFrame no vacío.
- Carga correcta del CSV.
- Excepciones controladas.

---

## 🏷️ Versión Liberada

```text
v1.0.0
```

---

## 📸 Evidencias

Las capturas del proyecto se encuentran en:

```text
docs/capturas/
```

Se incluyen evidencias de:

- Dashboard principal.
- Visualización tabular.
- Estadísticas descriptivas.
- Ejecución de Pytest.
- Ramas GitFlow en GitHub.
- Tag `v1.0.0`.

---

## 📚 Documentación adicional

Se recomienda revisar también:

```text
docs/README_Premium.docx
docs/README_Premium.pdf
informe.md
```

---

## 👥 Autores

| Integrante | Rol |
|---|---|
| Marcela Baldeón | Revisión funcional, validación y apoyo documental |
| César Jácome | Desarrollo, GitFlow, pruebas y documentación técnica |

---

## ✅ Conclusión

El proyecto permitió aplicar GitFlow en un desarrollo funcional con Streamlit, incorporando buenas prácticas de modularidad, pruebas automatizadas, versionamiento y documentación técnica.

# 📄 Informe Técnico del Proyecto

## Dashboard Penguins con Streamlit y GitFlow

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.50-red)
![Pytest](https://img.shields.io/badge/Pytest-8.4-green)
![GitFlow](https://img.shields.io/badge/GitFlow-Implementado-orange)
![Release](https://img.shields.io/badge/Release-v1.0.0-purple)

---

## 1. Datos Generales

| Campo | Información |
|---|---|
| Proyecto | Dashboard Penguins con Streamlit y GitFlow |
| Versión | 1.0.0 |
| Repositorio | <https://github.com/cefer181/tarea-gitflow-streamlit> |
| Integrantes | Marcela Baldeón / César Jácome |
| Fecha | Julio 2026 |

---

## 2. Introducción

El presente informe describe el procedimiento realizado para desarrollar una aplicación web con **Streamlit** orientada al análisis visual del archivo `penguins.csv`.

El proyecto fue gestionado aplicando **GitFlow**, con el propósito de organizar el desarrollo mediante ramas especializadas para funcionalidades, integración, pruebas, release y publicación de una versión estable.

Además, se implementaron pruebas automatizadas con **Pytest**, visualizaciones interactivas con **Plotly**, procesamiento de datos con **Pandas** y publicación del repositorio en **GitHub**.

---

## 3. Objetivos

### 3.1 Objetivo General

Desarrollar una aplicación web con Streamlit para el análisis visual del dataset Palmer Penguins, aplicando la metodología GitFlow durante todo el proceso de desarrollo, pruebas, integración y publicación.

### 3.2 Objetivos Específicos

- Crear funciones de validación para archivos CSV.
- Implementar la aplicación principal con Streamlit.
- Desarrollar visualización tabular de datos.
- Construir un dashboard interactivo.
- Implementar filtros dinámicos por especie e isla.
- Crear pruebas automatizadas con Pytest.
- Realizar un release con versión estable.
- Publicar el código en GitHub con ramas y tags.

---

## 4. Alcance del Proyecto

El proyecto incluye:

- Aplicación principal en Streamlit.
- Archivo `penguins.csv` dentro del repositorio.
- Validaciones para archivos CSV.
- Carga controlada del dataset.
- Dashboard con métricas y gráficos.
- Tabla de datos.
- Estadísticas descriptivas.
- Pruebas unitarias.
- Flujo GitFlow.
- Publicación en GitHub.
- Tag `v1.0.0`.

No se incluyó resolución de conflictos ni rama `hotfix`, ya que no fueron requeridas para esta actividad.

---

## 5. Tecnologías Utilizadas

| Tecnología | Uso |
|---|---|
| Python 3.9 | Lenguaje principal |
| Streamlit | Aplicación web |
| Pandas | Procesamiento de datos |
| Plotly | Gráficos interactivos |
| Pytest | Pruebas automatizadas |
| Git | Control de versiones |
| GitHub | Repositorio remoto |
| AlmaLinux 9.7 | Entorno de desarrollo |

---

## 6. Procedimiento Realizado

### 6.1 Preparación del entorno

Se utilizó una máquina virtual con **AlmaLinux 9.7**. Se verificó la instalación de Git y Python, y posteriormente se instaló `pip`.

Comandos principales:

```bash
cat /etc/os-release
git --version
python3 --version
pip3 --version
```

Luego se creó el proyecto en:

```bash
/opt/tarea-gitflow-streamlit
```

Se configuró el entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Y se instalaron las dependencias:

```bash
pip install streamlit pandas plotly pytest
pip freeze > requirements.txt
```

---

### 6.2 Creación de la estructura del proyecto

Se creó la estructura modular:

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

---

### 6.3 Inicialización de Git

Se inicializó el repositorio local:

```bash
git init
git branch -M main
git add .
git commit -m "chore: estructura inicial del proyecto Streamlit"
```

Luego se creó la rama de integración:

```bash
git checkout -b develop
```

---

## 7. Implementación de GitFlow

El desarrollo se realizó mediante ramas `feature`, integradas posteriormente a `develop`.

### Ramas utilizadas

| Rama | Funcionalidad |
|---|---|
| `feature/validaciones` | Funciones de validación |
| `feature/carga-datos` | Carga validada del CSV |
| `feature/tabla-datos` | Visualización tabular |
| `feature/dashboard` | Dashboard interactivo |
| `feature/app-streamlit` | Aplicación principal |
| `feature/pruebas-pytest` | Pruebas automatizadas |
| `feature/filtros-dashboard` | Filtros y estadísticas |

### Flujo aplicado

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
              └── main + tag v1.0.0
```

---

## 8. Desarrollo de Funcionalidades

### 8.1 Validaciones

Se implementaron funciones para validar:

- Extensión `.csv`.
- Existencia del archivo.
- Archivo no vacío.
- Columnas requeridas.
- DataFrame con registros.

Archivo:

```text
src/validaciones.py
```

---

### 8.2 Carga de datos

Se creó el archivo:

```text
src/carga_datos.py
```

Este módulo valida el archivo antes de leerlo con Pandas.

---

### 8.3 Visualización tabular

Se creó:

```text
src/tabla_datos.py
```

La funcionalidad presenta los registros con `st.dataframe`.

---

### 8.4 Dashboard

Se creó:

```text
src/dashboard.py
```

Incluye:

- Métricas generales.
- Gráfico por especie.
- Gráfico de masa corporal.
- Gráfico de dispersión.

---

### 8.5 Aplicación principal

Se creó:

```text
app.py
```

La aplicación contiene:

- Configuración de Streamlit.
- Carga del dataset.
- Menú lateral.
- Filtros por especie e isla.
- Navegación por secciones.

---

## 9. Dataset Utilizado

El archivo utilizado fue:

```text
data/penguins.csv
```

El dataset contiene registros de pingüinos con variables como:

| Variable | Descripción |
|---|---|
| `species` | Especie |
| `island` | Isla |
| `bill_length_mm` | Longitud del pico |
| `bill_depth_mm` | Profundidad del pico |
| `flipper_length_mm` | Longitud de la aleta |
| `body_mass_g` | Masa corporal |
| `sex` | Sexo |

---

## 10. Ejecución de la Aplicación

La aplicación se ejecutó con:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8503
```

Acceso desde navegador:

```text
http://IP_SERVIDOR:8503
```

---

## 11. Evidencias de Dashboard

### 11.1 Dashboard principal

El dashboard principal muestra métricas generales y gráficos interactivos.

> Insertar captura: `docs/capturas/dashboard-principal.png`

### 11.2 Visualización tabular

Permite visualizar los registros del dataset.

> Insertar captura: `docs/capturas/tabla-datos.png`

### 11.3 Estadísticas descriptivas

Presenta resumen estadístico de las variables numéricas.

> Insertar captura: `docs/capturas/estadisticas.png`

---

## 12. Pruebas con Pytest

Se implementaron pruebas en:

```text
tests/test_validaciones.py
```

Se ejecutó:

```bash
pytest -v
```

Resultado obtenido:

```text
11 passed
```

Las pruebas verifican:

- Archivo correcto.
- Archivo inexistente.
- Extensión incorrecta.
- Columnas requeridas.
- DataFrame vacío y no vacío.
- Carga correcta del CSV.

> Insertar captura: `docs/capturas/pytest.png`

---

## 13. Release y Tag

Se creó la rama:

```bash
git checkout -b release/v1.0.0
```

Luego se integró a `main` y `develop`.

Se generó el tag:

```bash
git tag -a v1.0.0 -m "Primera version estable de la aplicacion Streamlit"
```

Se publicó en GitHub:

```bash
git push origin main
git push origin develop
git push origin --tags
```

---

## 14. Publicación en GitHub

Repositorio:

```text
https://github.com/cefer181/tarea-gitflow-streamlit
```

Se publicaron:

- Rama `main`.
- Rama `develop`.
- Ramas `feature`.
- Tag `v1.0.0`.

> Insertar captura: `docs/capturas/github-branches.png`

---

## 15. Buenas Prácticas Implementadas

| Buena práctica | Aplicación |
|---|---|
| Modularidad | Separación en archivos dentro de `src/` |
| GitFlow | Uso de ramas main, develop, feature y release |
| Pruebas | Validación con Pytest |
| Versionado | Tag `v1.0.0` |
| Documentación | README, informe y evidencias |
| Dataset incluido | Archivo `penguins.csv` en el repositorio |
| Commits descriptivos | Mensajes claros por funcionalidad |

---

## 16. Conclusiones Técnicas

1. La aplicación de GitFlow permitió separar de forma ordenada el desarrollo de funcionalidades, la integración y la liberación estable, reduciendo el riesgo de afectar la rama principal.

2. La implementación de pruebas con Pytest permitió validar funciones críticas de carga y validación de datos antes de liberar la versión `v1.0.0`.

3. La modularización del proyecto facilitó la mantenibilidad, separando responsabilidades entre validación, carga de datos, dashboard y visualización tabular.

4. El uso de Streamlit permitió construir rápidamente una interfaz web funcional para análisis de datos, reduciendo el esfuerzo de desarrollo frontend.

5. La publicación en GitHub con ramas y tags permite evidenciar trazabilidad completa del trabajo realizado.

---

## 17. Recomendaciones

- Mantener ramas `feature` visibles durante la revisión académica para evidenciar GitFlow.
- Subir capturas en la carpeta `docs/capturas/`.
- Mantener actualizado el archivo `requirements.txt`.
- No eliminar el tag `v1.0.0`.
- Conservar el archivo `penguins.csv` en el repositorio.

---

## 18. Lecciones Aprendidas

- GitFlow mejora la organización de proyectos con varias funcionalidades.
- Streamlit es una herramienta eficiente para crear dashboards en Python.
- Pytest permite controlar la calidad de funciones críticas.
- El uso de ramas y commits descriptivos facilita la trazabilidad.
- La documentación técnica es clave para transferir conocimiento entre integrantes.

---

## 19. Mejoras Futuras

- Permitir carga dinámica de archivos CSV.
- Agregar exportación a PDF o Excel.
- Implementar despliegue en la nube.
- Agregar autenticación.
- Incorporar reportes de cobertura de pruebas.
- Mejorar el diseño visual de la interfaz.

---

## 20. Autores

| Integrante | Participación |
|---|---|
| Marcela Baldeón | Revisión funcional, validación y apoyo documental |
| César Jácome | Construcción del proyecto, GitFlow, pruebas y documentación |

---

## 21. Anexos

### Anexo 1. Comandos principales de GitFlow

```bash
git checkout -b feature/validaciones
git checkout develop
git merge feature/validaciones
git checkout -b release/v1.0.0
git checkout main
git merge release/v1.0.0
git tag -a v1.0.0 -m "Primera version estable"
```

### Anexo 2. Comando de ejecución

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8503
```

### Anexo 3. Comando de pruebas

```bash
pytest -v
```

# Pipeline de Datos – API a Base de Datos SQL

## 📌 Descripción del proyecto
Este proyecto implementa un **pipeline de datos sencillo pero realista**, orientado a demostrar
conocimientos de **ingeniería de datos a nivel junior**.

El sistema:
- Extrae datos desde una API pública
- Limpia y transforma los datos con Python
- Almacena la información procesada en un formato estructurado
- Sigue un flujo ETL (Extract, Transform, Load)

Este proyecto forma parte de mi portfolio técnico y está pensado para prácticas
y primeras oportunidades profesionales en el sector tecnológico.

---

## 🛠️ Tecnologías utilizadas
- Python 3
- Requests
- Pandas
- SQLite (fase inicial)
- Git y GitHub

---

## 📂 Estructura del proyecto



data-pipeline-project/
├── README.md
├── requirements.txt
├── src/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
└── data/
└── database.db



---

## 🔄 Flujo del pipeline (ETL)

1. **Extracción (Extract)**  
   Se consumen datos desde una API REST pública.

2. **Transformación (Transform)**  
   Se limpian los datos, se normalizan columnas y se preparan para su almacenamiento.

3. **Carga (Load)**  
   Los datos se almacenan en una base de datos relacional.

---

## 🎯 Objetivos del proyecto
- Practicar flujos reales de trabajo con datos
- Aplicar Python y SQL de forma conjunta
- Construir un proyecto sólido para el portfolio profesional

---

## 🚀 Posibles mejoras futuras
- Sustituir SQLite por PostgreSQL
- Añadir contenedores Docker
- Incluir control de errores y logs
- Automatizar la ejecución del pipeline
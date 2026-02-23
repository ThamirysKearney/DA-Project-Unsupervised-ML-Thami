# 🍄 Taller de Aprendizaje Automático No Supervisado
## UCI Mushroom Dataset — Clustering, PCA y Random Forest

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange)
![Status](https://img.shields.io/badge/Status-En%20desarrollo-yellow)

---

## 📋 Descripción del Proyecto

Proyecto de Data Science aplicada que explora el **UCI Mushroom Dataset** (8.124 muestras, 22 variables categóricas) usando técnicas de aprendizaje no supervisado y supervisado para descubrir si los datos contienen estructura natural que separe setas comestibles de venenosas — sin usar las etiquetas durante el entrenamiento.

Este proyecto fue construido como taller de aprendizaje para nivel junior profesional, con énfasis en comprensión real de cada decisión técnica.

---

## 🎯 Objetivos

- Explorar y preprocesar un dataset 100% categórico
- Aplicar **PCA** para reducción de dimensionalidad y visualización
- Detectar estructuras ocultas con **KMeans**
- Comparar con modelo supervisado **Random Forest**
- Evaluar hasta qué punto el aprendizaje no supervisado "descubre" la clase real

---

## 🗂️ Estructura del Repositorio

```
thamirys-mushroom-ml/
├── data/               ← Raw y Processed datasets
├── notebooks/          ← Notebook principal re-estructurado
├── reports/            ← Gráficos de PCA y matrices
├── scripts/            ← Utilidades de automatización
├── webapp/             ← Estructura para dashboard futuro
├── README.md
└── requirements.txt
```

---

## 🔧 Tecnologías

| Librería | Uso |
|---|---|
| `pandas` | Manipulación de datos categóricos |
| `scikit-learn` | PCA, KMeans, Random Forest, KNN Imputer |
| `plotly` | Visualizaciones 3D interactivas |
| `seaborn` | EDA y Mapas de calor (Cramer's V) |

---

## 🚀 Cómo ejecutar el proyecto

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd mushroom-unsupervised-ml

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Abrir el notebook
jupyter notebook notebooks/workshop_clustering_pca.ipynb
```

---

## 📊 Flujo del Análisis (Sincronizado con Notebook)

1.  **Setup y Carga**: Configuración de entorno y constantes.
2.  **EDA (Análisis Exploratorio)**: Detección de nulos reales con `?` y análisis de correlación categórica (**V de Cramer**).
3.  **Preprocesamiento**: Imputación por **KNN**, One-Hot Encoding y escalado de datos.
4.  **PCA**: Reducción de dimensiones y visualización dinámica en **3D**.
5.  **Benchmark (Random Forest)**: Evaluación de precisión mediante Train/Test Split y **Matriz de Confusión**.
6.  **Clustering (KMeans)**: Búsqueda del **K óptimo (Codo)** y validación contra etiquetas reales (98.8% acierto).
7.  **Conclusiones**: Lecciones aprendidas sobre la separabilidad natural de los datos.

---

## 📉 Conclusiones y Limitaciones

- **Separabilidad**: El dataset presenta una estructura geométrica tan clara que un modelo no supervisado distingue la toxicidad casi a la perfección.
- **PCA**: Vital para entender que el dataset no es ruido, sino grupos densos en el espacio multidimensional.
- **Limitaciones**: Sensibilidad de KMeans a la inicialización y pérdida de información inherente a la reducción de dimensiones.

---

## 🔮 Roadmap — Próximos Pasos

- [ ] Despliegue de un **Dashboard Interactivo** con Plotly Dash o Streamlit.
- [ ] Implementación de modelos adicionales como **UMAP** o **DBSCAN**.
- [ ] Exportación del modelo final como API (FastAPI).

---

## 📚 Dataset

**UCI Mushroom Dataset** (1981)
- 8.124 instancias | 22 features categóricas | Clase binaria (edible/poisonous)
- [UCI ML Repository](https://archive.ics.uci.edu/dataset/73/mushroom)
- DOI: 10.24432/C5959T

---

## 👤 Autor

Proyecto desarrollado como taller de aprendizaje de ML No Supervisado.

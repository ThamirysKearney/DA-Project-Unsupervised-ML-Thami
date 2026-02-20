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
mushroom-unsupervised-ml/
├── data/
│   ├── raw/            ← Dataset original descargado, nunca modificado
│   └── processed/      ← Dataset tras limpieza y encoding
├── notebooks/          ← Jupyter Notebook principal del análisis
├── src/                ← Funciones auxiliares reutilizables
├── reports/            ← Gráficas exportadas y métricas
├── webapp/             ← Roadmap del dashboard web (fase futura)
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔧 Tecnologías

| Librería | Uso |
|---|---|
| `pandas` | Carga y manipulación de datos |
| `numpy` | Operaciones numéricas |
| `matplotlib` / `seaborn` | Visualización |
| `scikit-learn` | PCA, KMeans, Random Forest, métricas |
| `ucimlrepo` | Descarga directa del dataset UCI |

---

## 🚀 Cómo ejecutar el proyecto

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd mushroom-unsupervised-ml

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Abrir el notebook
jupyter notebook notebooks/mushroom_analysis.ipynb
```

---

## 📊 Flujo del Análisis

```
Carga de datos → EDA → Preprocesamiento → PCA → Random Forest → KMeans → Comparación
```

1. **EDA**: Exploración univariada y bivariada de 22 variables categóricas
2. **Preprocesamiento**: Tratamiento de nulos + One-Hot Encoding
3. **PCA**: Reducción de dimensionalidad y visualización 2D
4. **Random Forest**: Modelo supervisado base + evaluación con PCA
5. **KMeans**: Clustering no supervisado + método del codo
6. **Comparación**: Clusters vs clases reales (Adjusted Rand Index)

---

## 📉 Limitaciones del Proyecto

Ver sección dedicada al final del notebook con análisis de:
- Limitaciones de One-Hot Encoding en datasets categóricos
- Limitaciones de PCA sobre variables binarias
- Limitaciones de KMeans (sensibilidad a inicialización, asume clusters esféricos)
- Riesgo de sobreajuste en Random Forest
- Mejoras futuras: UMAP, DBSCAN

---

## 🔮 Roadmap — Fase Futura

- [ ] Dashboard web interactivo (HTML + CSS + JS)
- [ ] Visualización de clusters en tiempo real
- [ ] Filtros por variable para exploración interactiva

---

## 📚 Dataset

**UCI Mushroom Dataset** (1981)
- 8.124 instancias | 22 features categóricas | Clase binaria (edible/poisonous)
- [UCI ML Repository](https://archive.ics.uci.edu/dataset/73/mushroom)
- DOI: 10.24432/C5959T

---

## 👤 Autor

Proyecto desarrollado como taller de aprendizaje de ML No Supervisado.

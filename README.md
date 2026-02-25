<h1 align="center">Taller de Aprendizaje Automático No Supervisado</h1>
<h2 align="center">UCI Mushroom Dataset - Clustering, PCA y Random Forest</h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--learn-1.3+-orange" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Status-Finalizado-brightgreen" alt="Status">
</p>

---

<h2 align="center">Descripción del Proyecto</h2>

<p align="center">
Proyecto de Ciencia de Datos aplicada que explora el <b>UCI Mushroom Dataset</b> (8,124 muestras, 22 variables categóricas) utilizando técnicas de aprendizaje no supervisado y supervisado. El objetivo es descubrir si los datos contienen una estructura natural que separe las setas comestibles de las venenosas sin utilizar las etiquetas durante el entrenamiento de los clusters.
</p>

<p align="center">
Este proyecto fue construido como un taller de aprendizaje para nivel junior profesional, con un fuerte énfasis en la comprensión técnica de cada decisión tomada.
</p>

---

<h2 align="center">Objetivos</h2>

- Explorar y preprocesar un conjunto de datos 100% categórico.
- Aplicar **PCA** para la reducción de dimensionalidad y visualización dinámica.
- Detectar estructuras ocultas mediante el algoritmo **KMeans**.
- Comparar los resultados con un modelo supervisado de **Random Forest**.
- Evaluar la capacidad del aprendizaje no supervisado para "descubrir" la clase real a través del **Adjusted Rand Index**.

---

<h2 align="center">Estructura del Repositorio</h2>

```text
thamirys-mushroom-ml/
├── data/               <-- Datasets originales y procesados
├── notebooks/          <-- Cuaderno principal con el analisis paso a paso
├── reports/            <-- Graficos exportados e insights tecnicos
├── scripts/            <-- Utilidades de automatizacion (limpieza tras desarrollo)
├── webapp/             <-- Estructura para futuro dashboard interactivo
├── README.md           <-- Documentacion general del proyecto
└── requirements.txt    <-- Librerias necesarias para el entorno
```

---

<h2 align="center">Tecnologías Utilizadas</h2>

| Librería | Propósito y Uso en el Proyecto |
|:---:|---|
| **Pandas** | Carga, manipulación y limpieza de datos categóricos. |
| **Scikit-learn** | Implementación de PCA, KMeans, Random Forest y KNN Imputer. |
| **Plotly** | Generación de visualizaciones 3D dinámicas e interactivas. |
| **Seaborn** | Análisis exploratorio (EDA) y cálculo de correlaciones (Cramer's V). |
| **Scipy** | Pruebas estadísticas y métricas de asociación. |

---

<h2 align="center">Cómo Ejecutar el Proyecto</h2>

```bash
# 1. Clonar el repositorio
git clone https://github.com/ThamirysKearney/DA-Project-Unsupervised-ML-Thami.git
cd DA-Project-Unsupervised-ML-Thami

# 2. Instalar las dependencias listadas
pip install -r requirements.txt

# 3. Lanzar el cuaderno de notas
jupyter notebook notebooks/workshop_clustering_pca.ipynb
```

---

<h2 align="center">Flujo del Análisis</h2>

1.  **Configuración**: Preparación del entorno y constantes de diseño.
2.  **EDA**: Detección de nulos reales y análisis de correlación categórica mediante la **V de Cramer**.
3.  **Preprocesamiento**: Imputación avanzada con **KNN**, codificación One-Hot y escalado de características.
4.  **PCA**: Reducción de dimensiones y visualización espacial en 3D.
5.  **Benchmark**: Evaluación de un modelo de **Random Forest** para establecer una base de precisión.
6.  **Clustering**: Búsqueda del **K óptimo** (Método del Codo) y validación de clusters contra la realidad.
7.  **Conclusiones**: Análisis crítico de la separabilidad natural de las muestras.

---

<h2 align="center">Conclusiones y Limitaciones</h2>

- **Separabilidad**: Los datos presentan una estructura tan definida que el modelo no supervisado distingue la toxicidad con un éxito superior al 98%.
- **PCA**: Resultó vital para comprender que el dataset no es ruido, sino grupos densos en un espacio multidimensional.
- **Limitaciones**: Sensibilidad de KMeans a la inicialización y pérdida inevitable de información al reducir dimensiones.

---

<h2 align="center">Roadmap — Próximos Pasos</h2>

- [ ] Desarrollo de un Dashboard interactivo utilizando Streamlit.
- [ ] Implementación de algoritmos de densidad como DBSCAN.
- [ ] Despliegue del modelo final como una API consumible.

---

<h2 align="center">Contacto y Autor</h2>

<div align="center">
  <p>Proyecto desarrollado por <b>Thamirys Kearney</b></p>
  
  <a href="https://linkedin.com/in/thamirys-kearney-0a7a7331/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://github.com/ThamirysKearney">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="mailto:thamirys.kearney@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>
  <a href="https://discord.com/users/thamikearney_98219">
    <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  </a>
</div>

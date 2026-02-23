import json

def apply_new_headers(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Mapeo de índices de celda a sus nuevos encabezados
    # Basado en el implementation_plan.md y la extracción previa
    header_updates = {
        0: ["# Taller ML no Spervisado: Mushroom Dataset (Clustering and PCA)"],
        1: ["### Estructura de este cuaderno:"],
        3: ["# 1. Setup y Carga de Datos"],
        4: ["## 1.1 Librerías"],
        7: ["## 1.2 Configuración Global (Constantes)"],
        9: ["## 1.3 Carga del Dataset y Primer Vistazo"],
        11: ["# 2. EDA: Análisis Exploratorio"],
        18: ["## 2.1 Detección de Nulos Reales"],
        45: ["## 2.2 Limpieza de Datos (Imputación KNN)"],
        52: ["## 2.3 Análisis de Correlación: V de Cramer"],
        57: ["## 2.4 Conclusiones del EDA"],
        59: ["# 3. Preprocesamiento de Datos"],
        60: ["## 3.1 Limpieza Final y Separación de Variables"],
        64: ["## 3.2 Verificación de Balanceo del Target"],
        67: ["## 3.3 Codificación y Escalado de Datos"],
        69: ["## 3.4 Verificación de Dimensionalidad"],
        72: ["# 4. Análisis de Componentes Principales (PCA)"],
        74: ["## 4.1 Reducción a 2 Componentes"],
        76: ["## 4.2 Visualización del Espacio PCA"],
        78: ["## 4.3 Interpretación de los Componentes"],
        103: ["## 4.4 Visualización Avanzada: Espacio PCA 3D"],
        80: ["# 5. Modelo Supervisado: Benchmark (Random Forest)"],
        81: ["## 5.1 Entrenamiento y Feature Importance"],
        89: ["## 5.2 Evaluación Real (Train/Test Split)"],
        98: ["## 5.3 Optimización y Matriz de Confusión"],
        107: ["# 6. Aprendizaje No Supervisado: Clustering (KMeans)"],
        108: ["## 6.1 Búsqueda del K Óptimo (Codo y Silueta)"],
        113: ["## 6.2 Generación de Clusters y Evaluación"],
        119: ["## 6.3 Visualización: Clusters vs Clase Real"],
        124: ["# 7. Conclusiones Finales y Lecciones Aprendidas"],
        125: ["## 7.1 Limitaciones y Futuras Mejoras"]
    }

    # Celdas que deben ser limpiadas de encabezados antiguos o simplificadas
    # (Especialmente las que tenían números manuales redundantes)
    for idx, content in header_updates.items():
        if idx < len(nb['cells']):
            nb['cells'][idx]['source'] = [line + "\n" for line in content]
            # Asegurarse de que el último elemento no tenga salto de línea si antes no lo tenía, 
            # pero en notebooks es común que cada línea lo tenga.
            if nb['cells'][idx]['source']:
                nb['cells'][idx]['source'][-1] = nb['cells'][idx]['source'][-1].strip()

    # Guardar cambios
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Notebook updated successfully.")

if __name__ == "__main__":
    apply_new_headers('notebooks/workshop_clustering_pca.ipynb')

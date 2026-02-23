import json

def restore_limitations_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Nuevo contenido para la celda 125 (conservando el encabezado jerárquico)
    new_source = [
        "## 7.1 Limitaciones y Futuras Mejoras\n",
        "\n",
        "Tras completar este taller, es importante reconocer que el modelo tiene margen de mejora:\n",
        "- **Sensibilidad**: KMeans es sensible a valores extremos, aunque el escalado ayuda.\n",
        "- **Ampliación**: En el futuro, se podrían explorar más de 2 clusters para identificar sub-familias específicas de setas como sugería el profesor.\n",
        "- **Interpretación**: Aunque PC1 y PC2 explican mucha varianza, todavía perdemos algo de información al reducir dimensiones."
    ]
    
    # Actualizar la celda
    target_idx = 125
    if target_idx < len(nb['cells']):
        nb['cells'][target_idx]['source'] = new_source
        print(f"Cell {target_idx} restored successfully.")
    else:
        print(f"Error: Cell {target_idx} not found.")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    restore_limitations_content('notebooks/workshop_clustering_pca.ipynb')

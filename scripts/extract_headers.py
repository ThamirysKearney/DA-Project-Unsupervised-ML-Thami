import json
import os

def get_notebook_structure(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    structure = []
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            content = "".join(cell['source'])
            lines = content.split('\n')
            for line in lines:
                if line.strip().startswith('#'):
                    structure.append({
                        "cell_index": i,
                        "header": line.strip()
                    })
    
    with open('notebook_headers.json', 'w', encoding='utf-8') as f:
        json.dump(structure, f, indent=2, ensure_ascii=False)
    print(f"Structure saved to notebook_headers.json")

if __name__ == "__main__":
    get_notebook_structure('notebooks/workshop_clustering_pca.ipynb')

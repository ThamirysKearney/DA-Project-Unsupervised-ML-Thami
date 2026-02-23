import subprocess
import json
import sys

def get_old_content():
    try:
        # Get the previous version of the notebook from git
        result = subprocess.run(['git', 'show', 'HEAD:notebooks/workshop_clustering_pca.ipynb'], 
                               capture_output=True, text=False)
        content = result.stdout.decode('utf-8', errors='ignore')
        nb = json.loads(content)
        
        # Look for the cell containing the limitations header in the old version
        for cell in nb['cells']:
            if cell['cell_type'] == 'markdown':
                source_text = "".join(cell['source'])
                if "Limitaciones y Futuras Mejoras" in source_text:
                    print("---FOUND OLD CONTENT---")
                    print(json.dumps(cell['source'], indent=2, ensure_ascii=False))
                    return
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_old_content()

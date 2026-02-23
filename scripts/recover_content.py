import json

def recover_cell_content(backup_path, target_idx):
    with open(backup_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    if target_idx < len(nb['cells']):
        content = nb['cells'][target_idx]['source']
        print("RECOVERED CONTENT:")
        print("".join(content))
    else:
        print(f"Index {target_idx} out of range.")

if __name__ == "__main__":
    recover_cell_content('notebooks/backup_nb.ipynb', 125)

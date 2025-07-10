import os
import glob

# Get all Python files in pages directory
pages_files = glob.glob("pages/*.py")

for file_path in pages_files:
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if the import already exists
    if "from client import TokenClient" not in content:
        # Add the import after existing imports
        lines = content.split('\n')
        
        # Find the last import line
        last_import_index = -1
        for i, line in enumerate(lines):
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                last_import_index = i
        
        # Insert the new import after the last import
        if last_import_index != -1:
            lines.insert(last_import_index + 1, "from client import TokenClient")
        else:
            # If no imports found, add at the beginning
            lines.insert(0, "from client import TokenClient")
        
        # Write back to file
        with open(file_path, 'w') as f:
            f.write('\n'.join(lines))
        
        print(f"Added import to: {file_path}")
    else:
        print(f"Import already exists in: {file_path}")

print("Finished adding imports to all pages files!")
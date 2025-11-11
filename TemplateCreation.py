import os

# Define folder structure
folders = [
    "data/raw",
    "data/interim",
    "data/processed",
    "notebooks",
    "src/data",
    "src/features",
    "src/models",
    "src/utils",
    "src/evaluation",
    "configs",
    "models",
    "reports/figures"
]

# Define files with default content
files = {
    "README.md": "# Machine Learning Project\n\nProject description goes here.",
    ".gitignore": "__pycache__/\n.ipynb_checkpoints/\nmodels/\ndata/\n.env\n",
    "requirements.txt": "# Add dependencies here\ntensorflow\nscikit-learn\npandas\nnumpy\nmatplotlib\nseaborn\n",
    "configs/config.yaml": "# Configuration file for ML project\n",
    "configs/logging.conf": "# Logging configuration\n",
    "reports/results.txt": "",
    "setup.py": """from setuptools import setup, find_packages

setup(
    name='ml_project',
    version='0.1',
    packages=find_packages(),
)
"""
}

# Directories where __init__.py should be created
package_dirs = [
    "src",
    "src/data",
    "src/features",
    "src/models",
    "src/utils",
    "src/evaluation"
]

def create_folders():
    """Create all directories in the project."""
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"📁 Created folder: {folder}")

def create_files():
    """Create base files with default content."""
    for file_path, content in files.items():
        dir_name = os.path.dirname(file_path)
        if dir_name:  # Only create directory if path is not empty
            os.makedirs(dir_name, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"📄 Created file: {file_path}")

def create_init_files():
    """Create __init__.py files for Python packages."""
    for package_dir in package_dirs:
        init_path = os.path.join(package_dir, "__init__.py")
        with open(init_path, "w", encoding="utf-8") as f:
            f.write("# Makes this directory a Python package\n")
        print(f"🐍 Created: {init_path}")

if __name__ == "__main__":
    print("🚀 Setting up ML project structure...\n")
    create_folders()
    create_files()
    create_init_files()
    print("\n✅ Project structure setup complete with __init__.py files!")

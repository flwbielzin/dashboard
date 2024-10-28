from cx_Freeze import setup, Executable
import sys
import os

# Se você está usando Windows, defina base como "Win32GUI"
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Função para coletar arquivos em uma pasta
def include_files_in_directory(directory):
    return [(os.path.join(directory, file), directory) for file in os.listdir(directory)]

# Defina as opções para o build
build_exe_options = {
    "packages": ["dash", "dash_bootstrap_components", "pandas", "plotly"],
    "include_files": [
        "df_cat_despesa.csv",
        "df_cat_receita.csv",
        "df_despesas.csv",
        "df_receitas.csv",
    ] + include_files_in_directory("components") + include_files_in_directory("assets"),
}

setup(
    name="MeuDashboard",
    version="0.1",
    description="Um dashboard em Dash",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base)]
)

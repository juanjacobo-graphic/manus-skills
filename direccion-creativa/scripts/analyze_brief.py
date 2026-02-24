'''
Este script analiza un archivo de brief y extrae la información clave.
'''
import sys

def analyze_brief(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        # Aquí iría la lógica para extraer y analizar la información del brief.
        # Por ahora, solo imprimimos un mensaje de éxito.
        print(f"Brief analizado con éxito: {file_path}")
        print("--- Resumen del Brief ---")
        print(content)
        print("------------------------")

    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_brief(sys.argv[1])
    else:
        print("Uso: python analyze_brief.py <ruta_al_brief>")

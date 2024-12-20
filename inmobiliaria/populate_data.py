import os
import subprocess

# Define el orden de carga de los fixtures
FIXTURES = [
    "fixtures/regiones.json",
    "fixtures/comunas.json"
    ]

def load_fixtures():
    print("Iniciando la carga de fixtures...\n")
    for fixture in FIXTURES:
        print(f"Cargando {fixture}...")
        try:
            # Ejecuta el comando 'loaddata' para cada fixture
            subprocess.run(["python", "manage.py", "loaddata", fixture], check=True)
            print(f"✔ {fixture} cargado correctamente.\n")
        except subprocess.CalledProcessError as e:
            print(f"✘ Error al cargar {fixture}: {e}\n")
            break  # Detiene el proceso si hay un error en algún fixture

    print("Población de datos completada.")

if __name__ == "__main__":
    load_fixtures()

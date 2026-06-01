import subprocess
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
py = ROOT / ".venv" / "Scripts" / "python.exe"
BUILD_SCRIPT = ROOT / "scripts" / "build_book.py"

with open("test_output.txt", "w", encoding="utf-8") as f:
    f.write("Iniciando prueba de Popen...\n")
    
    try:
        env = os.environ.copy()
        env["PYTHONUTF8"] = "1"
        
        f.write("Lanzando build_book.py...\n")
        process = subprocess.Popen(
            [str(py), str(BUILD_SCRIPT)],
            cwd=ROOT,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
        )
        
        f.write("Leyendo stdout...\n")
        assert process.stdout is not None
        for line in process.stdout:
            f.write(f"LINE: {line}")
            f.flush()
            
        return_code = process.wait()
        f.write(f"Build finalizado con return code: {return_code}\n")
    except Exception as e:
        f.write(f"Excepcion en Popen: {e}\n")

    f.write("Prueba finalizada.\n")
print("Prueba completada.")

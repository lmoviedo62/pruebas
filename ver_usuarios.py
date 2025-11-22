import sqlite3
import os

# Verificar que existe la base de datos
if not os.path.exists('serena.db'):
    print(" ERROR: No existe el archivo serena.db")
    print(" Ubicación actual:", os.getcwd())
    exit()

print(" Conectando a serena.db...")

# Conectar a la base de datos
conn = sqlite3.connect('serena.db')
cursor = conn.cursor()

# Ver qué tablas existen
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
print(f"\n Tablas en la base de datos: {tablas}\n")

try:
    # Intentar leer usuarios
    cursor.execute("SELECT id, email, nombre, apellido, programa, semestre, telefono FROM users")
    usuarios = cursor.fetchall()
    
    print(f" Total usuarios registrados: {len(usuarios)}\n")
    
    if len(usuarios) == 0:
        print("  La tabla 'users' existe pero NO hay usuarios registrados")
        print("\n Posibles razones:")
        print("   1. Aún no has completado ningún registro desde el formulario")
        print("   2. El registro no se está guardando correctamente")
        print("\n Solución: Intenta registrarte desde http://127.0.0.1:8000/register")
    else:
        for user in usuarios:
            print(f"{'='*60}")
            print(f"ID: {user[0]}")
            print(f"Email: {user[1]}")
            print(f"Nombre: {user[2]} {user[3]}")
            print(f"Programa: {user[4]}")
            print(f"Semestre: {user[5]}")
            print(f"Teléfono: {user[6]}")
        print(f"{'='*60}\n")
    
except sqlite3.OperationalError as e:
    print(f" ERROR al leer la tabla 'users': {e}")
    print("\n Esto significa que la tabla no existe o tiene una estructura diferente")

except Exception as e:
    print(f" Error inesperado: {e}")

conn.close()
print("\n Conexión cerrada")

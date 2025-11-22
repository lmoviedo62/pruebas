"""
Script de migración para agregar campos de reset_token a la tabla users
Ejecuta este script UNA SOLA VEZ después de actualizar el modelo User
"""

import sqlite3

def migrate():
    # Conectar a la base de datos
    conn = sqlite3.connect('serena.db')
    cursor = conn.cursor()
    
    try:
        # Agregar columna reset_token
        cursor.execute('''
            ALTER TABLE users ADD COLUMN reset_token VARCHAR(255) NULL
        ''')
        print("✅ Columna reset_token agregada")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("⚠️  Columna reset_token ya existe")
        else:
            raise e
    
    try:
        # Agregar columna reset_token_expires
        cursor.execute('''
            ALTER TABLE users ADD COLUMN reset_token_expires DATETIME NULL
        ''')
        print("✅ Columna reset_token_expires agregada")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("⚠️  Columna reset_token_expires ya existe")
        else:
            raise e
    
    # Confirmar cambios
    conn.commit()
    conn.close()
    
    print("\n✅ Migración completada exitosamente!")

if __name__ == "__main__":
    migrate()

    
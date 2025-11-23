"""
Script de migración para agregar created_at y updated_at a emotion_entries
"""

import sqlite3
from datetime import datetime

def migrate():
    conn = sqlite3.connect('serena.db')
    cursor = conn.cursor()
    
    try:
        # Agregar columna created_at
        cursor.execute('''
            ALTER TABLE emotion_entries ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ''')
        print("✅ Columna created_at agregada")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("⚠️  Columna created_at ya existe")
        else:
            raise e
    
    try:
        # Agregar columna updated_at
        cursor.execute('''
            ALTER TABLE emotion_entries ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ''')
        print("✅ Columna updated_at agregada")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("⚠️  Columna updated_at ya existe")
        else:
            raise e
    
    conn.commit()
    conn.close()
    
    print("\n✅ Migración completada!")

if __name__ == "__main__":
    migrate()
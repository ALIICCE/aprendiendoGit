import sqlite3

conn = sqlite3.connect("bot_telegram.db")
cursor = conn.cursor()

# Tabla 1: Comandos de ayuda
cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_help (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comando TEXT UNIQUE NOT NULL,
    descripcion TEXT NOT NULL
)
""")

# Tabla 2: Verbos en inglés (forma base)
cursor.execute("""
CREATE TABLE IF NOT EXISTS verbos_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    verbo TEXT UNIQUE NOT NULL
)
""")

# Tabla 3: Verbos en presente continuo
cursor.execute("""
CREATE TABLE IF NOT EXISTS verbos_continuo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    verbo_continuo TEXT UNIQUE NOT NULL,
    verbo_base_id INTEGER,
    FOREIGN KEY (verbo_base_id) REFERENCES verbos_base(id)
)
""")

# Tabla 4: Verbos en español
cursor.execute("""
CREATE TABLE IF NOT EXISTS verbos_espanol (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    traduccion TEXT NOT NULL,
    verbo_base_id INTEGER,
    FOREIGN KEY (verbo_base_id) REFERENCES verbos_base(id)
)
""")

# Insertar algunos datos de ejemplo en menu_help
cursor.execute("""
INSERT OR IGNORE INTO menu_help (comando, descripcion)
VALUES
    ('/start', 'Inicia el bot'),
    ('/help', 'Muestra los comandos disponibles'),
    ('/verbos', 'Muestra verbos comunes en inglés')
""")

# Verbos: run, eat, sleep
verbos = [
    ("run", "running", "correr"),
    ("eat", "eating", "comer"),
    ("sleep", "sleeping", "dormir"),
]

for verbo, continuo, espanol in verbos:
    cursor.execute("INSERT OR IGNORE INTO verbos_base (verbo) VALUES (?)", (verbo,))
    cursor.execute("SELECT id FROM verbos_base WHERE verbo = ?", (verbo,))
    verbo_id = cursor.fetchone()[0]
    cursor.execute("INSERT OR IGNORE INTO verbos_continuo (verbo_continuo, verbo_base_id) VALUES (?, ?)", (continuo, verbo_id))
    cursor.execute("INSERT OR IGNORE INTO verbos_espanol (traduccion, verbo_base_id) VALUES (?, ?)", (espanol, verbo_id))

conn.commit()
conn.close()
print("✅ Base de datos creada correctamente.")

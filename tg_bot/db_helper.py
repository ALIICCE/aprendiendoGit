import sqlite3

DB_PATH = "bot_telegram.db"

def buscar_menu_help():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT comando, descripcion FROM menu_help")
    resultados = cursor.fetchall()
    conn.close()
    return "\n".join([f"{comando} - {descripcion}" for comando, descripcion in resultados])

def buscar_verbos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT vb.verbo, vc.verbo_continuo, ve.traduccion
        FROM verbos_base vb
        LEFT JOIN verbos_continuo vc ON vb.id = vc.verbo_base_id
        LEFT JOIN verbos_espanol ve ON vb.id = ve.verbo_base_id
    """)
    resultados = cursor.fetchall()
    conn.close()

    respuesta = "📘 Verbos:\n"
    for verbo, continuo, espanol in resultados:
        respuesta += f"- {verbo} | {continuo} | {espanol}\n"
    return respuesta.strip()

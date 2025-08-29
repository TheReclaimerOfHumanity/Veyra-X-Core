import sqlite3, json, os, time

DB_PATH = os.environ.get("VEYRA_DB", "veyra.db")

def _init():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts REAL, source TEXT, type TEXT, payload TEXT, tags TEXT
    )""")
    conn.commit()
    return conn

def remember_event(source: str, type_: str, payload: dict, tags=None):
    conn = _init()
    cur = conn.cursor()
    cur.execute("INSERT INTO events(ts,source,type,payload,tags) VALUES(?,?,?,?,?)",
                (time.time(), source, type_, json.dumps(payload), ",".join(tags or [])))
    conn.commit(); conn.close()

def recall_last(n=5):
    conn = _init()
    cur = conn.cursor()
    cur.execute("SELECT ts,source,type,payload,tags FROM events ORDER BY id DESC LIMIT ?", (n,))
    rows = cur.fetchall()
    conn.close()
    return rows


python
import sqlite3
import pandas as pd

def migrate_items(db_path='storage/short_term.db', csv_path='storage/long_term_storage.csv'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                      id INTEGER PRIMARY KEY,
                      feature1 REAL,
                      feature2 REAL,
                      access_count INTEGER)''')
    
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    
    if not items:
        print("No items to migrate.")
        return

    df = pd.read_csv(csv_path) if os.path.exists(csv_path) else pd.DataFrame(columns=["id", "feature1", "feature2", "access_count"])
    
    for item in items:
        if item[3] < 2:  # access_count < 2
            df = df.append({"id": item[0], "feature1": item[1], "feature2": item[2], "access_count": item[3]}, ignore_index=True)
            cursor.execute(f"DELETE FROM items WHERE id={item[0]}")
    
    df.to_csv(csv_path, index=False)
    conn.commit()
    conn.close()

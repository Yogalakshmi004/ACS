

import os
import sqlite3
import pandas as pd

def migrate_items(db_path='storage/short_term.db', csv_path='storage/long_term_storage.csv', access_threshold=2):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Make sure the items table exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY,
                        feature1 REAL,
                        feature2 REAL,
                        access_count INTEGER
                    )''')
    conn.commit()

    # Read all items
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    if not items:
        print("[INFO] No items found to migrate.")
        conn.close()
        return

    # Load existing long-term storage
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        df = pd.DataFrame(columns=["id", "feature1", "feature2", "access_count"])

    # Migrate items with access_count below threshold
    migrated = 0
    for item in items:
        item_id, feature1, feature2, access_count = item
        if access_count < access_threshold:
            df = pd.concat([df, pd.DataFrame([{
                "id": item_id,
                "feature1": feature1,
                "feature2": feature2,
                "access_count": access_count
            }])], ignore_index=True)
            cursor.execute(f"DELETE FROM items WHERE id = ?", (item_id,))
            migrated += 1

    # Save updated long-term storage
    df.to_csv(csv_path, index=False)

    conn.commit()
    conn.close()

    print(f"[SUCCESS] Migrated {migrated} items to long-term storage.")

if _name_ == "_main_":
    migrate_items()
import sqlite3

DATABASE = 'tasks.db'
TABLE_NAME = 'users'

def delete_all_items():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        cursor.execute(f'DELETE FROM {TABLE_NAME};')
        conn.commit()
        print(f'All items deleted from {TABLE_NAME}.')
    except Exception as e:
        print(f'Error deleting items: {e}')
    finally:
        conn.close()

if __name__ == '__main__':
    delete_all_items()

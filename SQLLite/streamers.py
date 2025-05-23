import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME_STREAMERS = 'streamers'
TABLE_NAME_PARTIDAS = 'matches'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


def create_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME_STREAMERS} (
            id_streamer INTEGER PRIMARY KEY AUTOINCREMENT,
            nick_name TEXT,
            puuid TEXT
        )
        '''
    )

    cursor.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME_PARTIDAS} (
            id_partida INTEGER PRIMARY KEY AUTOINCREMENT,
            id_streamer INTEGER,
            id_partidas_lol TEXT,
            FOREIGN KEY(id_streamer) REFERENCES {TABLE_NAME_STREAMERS}(id_streamer)
        )
        '''
    )

    connection.commit()
    cursor.close()
    connection.close()


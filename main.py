from SQLLite.streamers import create_table
from extract.extract_ID import id_match


def main():
    create_table()
    partidas = id_match()
    print(partidas)

if __name__ == '__main__':
    main()
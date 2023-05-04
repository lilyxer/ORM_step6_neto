import psycopg2

def create_bd(psd):
    """
    Заходит под админом и пробует создать базу данных shop_db под нужды ORM
    psd - пароль базы
    """
    conn =  psycopg2.connect(database='postgres', user='postgres', 
                             password=psd)
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    try:
        cur.execute("""CREATE DATABASE shop_db;""")
    except Exception as e:
        print(f'{e}отработал rollback')
        conn.rollback()
    conn.close()

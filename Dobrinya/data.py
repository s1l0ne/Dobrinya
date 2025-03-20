import connect


def get_train_data() -> list:
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM datamarts.dobrinya\n"
                "WHERE report_year BETWEEN 2018 AND 2019\n"
                "ORDER BY departure_road, report_year, report_month")

    return cur.fetchall()


def get_test_data() -> list:
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM datamarts.dobrinya_test\n'
                'ORDER BY departure_road, report_year, report_month')

    return cur.fetchall()

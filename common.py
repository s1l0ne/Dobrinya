import connect

conn = connect.connect()
cur = conn.cursor()

base_request = ('INSERT INTO datamarts.dobrinya('
                '   report_month, '
                '   report_year, '
                '   departure_road, '
                '   total_cargo_weight, '
                '   transport_fee)\n'
                '{values}')

values = ('SELECT '
          '     report_month, '
          '     report_year, '
          '     departure_road, '
          '     SUM(cargo_weight) AS total_cargo_weight, '
          '     SUM(carriage_fee) as transport_fee '
          'FROM ('
          'SELECT '
          '     report_month::BIGINT, '
          '     report_year::BIGINT, '
          '     departure_road::BIGINT, '
          '     cargo_weight::BIGINT, '
          '     carriage_fee::BIGINT\n'
          'FROM rgd."{year}_{month}_1"\n'
          'UNION ALL\n'
          'SELECT\n'
          '     report_month::BIGINT, '
          '     report_year::BIGINT, '
          '     departure_road::BIGINT, '
          '     cargo_weight::BIGINT, '
          '     carriage_fee::BIGINT\n'
          'FROM rgd."{year}_{month}_2")\n'
          'GROUP BY report_month, report_year, departure_road')

for year in range(2020, 2021):
    for month in range(1, 5):
        cur.execute(base_request.format(values=values.format(year=year, month=str(month).zfill(2))))
        conn.commit()
        print(year, str(month).zfill(2), sep='_')

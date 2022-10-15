from flask import Flask, render_template, request
from db import get_conn

from flask_paginate import Pagination, get_page_args

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aircrafts/')
def aircrafts():
    conn = get_conn()

    with conn.cursor() as cur:
        cur.execute(
            '''
            SELECT * FROM bookings.aircrafts_data
            '''
        )
        result = cur.fetchall()

    if conn:
        conn.close()

    return render_template('aircrafts.html', aircrafts=result)


@app.route('/airports/')
def airports():
    conn = get_conn()

    with conn.cursor() as cur:
        cur.execute(
            '''
            SELECT * FROM bookings.airports_data
            ORDER BY 1
            '''
        )
        result = cur.fetchall()
    
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(result)
    pagination_ports = result[offset:offset+per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap5')
    if conn:
        conn.close()

    return render_template(
        'airports.html',
        airports=pagination_ports,
        page=page,
        per_page=per_page,
        pagination=pagination,
    )


@app.route('/flights/')
def flights():
    conn = get_conn()

    with conn.cursor() as cur:
        cur.execute(
            '''
            SELECT * FROM bookings.flights
            ORDER BY 1
            LIMIT 10
            '''
        )
        flights_first_rows = cur.fetchall()

        cur.execute(
            '''
            SELECT COUNT(*) FROM bookings.flights
            '''
        )
        flights_count = cur.fetchall()[0][0]


    if conn:
        conn.close()

    return render_template(
        'flights.html',
        flights_first_rows=flights_first_rows,
        flights_count=flights_count)


@app.route('/select_flights/', methods=['GET', 'POST'])
def select_flights():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(
            '''
            SELECT COUNT(*) FROM bookings.flights
            '''
        )
        flights_count = cur.fetchall()[0][0]

    if request.method == 'GET':

        if conn:
            conn.close()

        return render_template('select_flights.html', flights_count=flights_count)

    elif request.method == 'POST':
        flight_id_01 = request.form['flight_id_01']
        flight_id_02 = request.form['flight_id_02']
        flight_id_03 = request.form['flight_id_03']


        if flight_id_01 and int(flight_id_01) <= flights_count:
            flight_id_01 = int(flight_id_01)
        else:
            flight_id_01 = 0
        
        if flight_id_02 and int(flight_id_01) <= flights_count:
            flight_id_02 = int(flight_id_02)
        else:
            flight_id_02 = 0
        
        if flight_id_03 and int(flight_id_01) <= flights_count:
            flight_id_03 = int(flight_id_03)
        else:
            flight_id_03 = 0
        
        flight_id_list = [flight_id_01, flight_id_02, flight_id_03]

        with conn.cursor() as cur:
            cur.execute(
                '''
                SELECT
                    f.flight_id,
                    f.flight_no,
                    airport1.city::json ->> 'ru' as departure_city,
                    f.departure_airport,
                    f.scheduled_departure,
                    f.actual_departure,
                    airport2.city::json ->> 'ru' as arrival_city,
                    f.arrival_airport,
                    f.scheduled_arrival,
                    f.actual_arrival,
                    t.passenger_name,
                    t.contact_data::json ->> 'email' as email,
                    t.contact_data::json ->> 'phone' as phone
                FROM bookings.tickets AS t
                JOIN bookings.ticket_flights AS tf ON t.ticket_no = tf.ticket_no
                JOIN bookings.flights AS f ON tf.flight_id = f.flight_id
                JOIN bookings.airports_data AS airport1 ON f.departure_airport = airport1.airport_code
                JOIN bookings.airports_data as airport2 on f.arrival_airport = airport2.airport_code
                WHERE f.flight_id = ANY(%s)
                ORDER BY f.flight_no, f.scheduled_departure, t.passenger_name
                ''',
                (flight_id_list, )
            )

            flights_selected = cur.fetchall()

            if conn:
                conn.close()      

        return render_template(
            'select_flights.html',
            flights_count=flights_count,
            flights_selected=flights_selected,
        )


if __name__ == '__main__':
    app.run(debug=False)
import os
from flask import Flask, jsonify, request, redirect, url_for
import pymysql

application = Flask(__name__)

@application.route('/api/tours')
def getTours():
    db = pymysql.connect("31.31.196.94", "u0480826_toursad",
                         "Admin1234", "u0480826_tours")
    cursor = db.cursor()
    cursor.execute('''select * from tours
inner join hotels h on tours.idHotel = h.idHotel
inner join countries c on h.idCountry = c.idCountry''')
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'tours': r})


@application.route('/api/hotels')
def getHotels():
    db = pymysql.connect("31.31.196.94", "u0480826_toursad",
                         "Admin1234", "u0480826_tours")
    cursor = db.cursor()
    cursor.execute('''select * from hotels
    inner join countries c on hotels.idCountry = c.idCountry''')
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'hotels': r})


@application.route('/api/countries')
def getCountries():
    db = pymysql.connect("31.31.196.94", "u0480826_toursad",
                         "Admin1234", "u0480826_tours")
    cursor = db.cursor()
    cursor.execute('''select * from countries''')
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'countries': r})


@application.route('/api/getImagesHotel')
def getImagesHotel():
    hotel_id = request.args.get('hotel_id', type=int)
    db = pymysql.connect("31.31.196.94", "u0480826_toursad",
                         "Admin1234", "u0480826_tours")
    cursor = db.cursor()
    cursor.execute('''select * from imagesHotel
inner join hotels h on imagesHotel.idHotel = h.idHotel
where h.idHotel = {0}'''.format(hotel_id))
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'images': r})


@application.route('/api/findTours')
def findTours():
    country = request.args.get('country', type=str)
    dateStart = request.args.get('dateStart', type=str)
    dateEnd = request.args.get('dateEnd', type=str)

    if country == "" and dateStart == "" and dateEnd == "":
        return redirect("/tours")

    db = pymysql.connect("31.31.196.94", "u0480826_toursad",
                         "Admin1234", "u0480826_tours")
    cursor = db.cursor()

    if country is not None and dateEnd == "" and dateStart == "":
        cursor.execute('''select * from tours
inner join hotels h on tours.idHotel = h.idHotel
inner join countries c on h.idCountry = c.idCountry
where c.nameCountry = "{0}"'''.format(country))
        r = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]
        return jsonify({'tours': r})

    cursor.execute('''select * from tours
inner join hotels h on tours.idHotel = h.idHotel
inner join countries c on h.idCountry = c.idCountry
where c.nameCountry = "{0}" and dateStart = "{1}" and dateEnd = "{2}" '''.format(country, dateStart, dateEnd))

    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'tours': r})
   
@application.route('/api/addTour')
def addTour():
    idHotel = request.args.get('idHotel', type=str)
    dateStart = request.args.get('dateStart', type=str)
    dateEnd = request.args.get('dateEnd', type=str)
    price = request.args.get('price', type=str)

    db = pymysql.connect("31.31.196.94", "u0480826_toursad",
                         "Admin1234", "u0480826_tours")
    cursor = db.cursor()

    sql = """insert into tours(idHotel, dateStart, dateEnd, price) values(%s, %s, %s, %s)"""
    cursor.execute(sql, (idHotel, dateStart, dateEnd, price))
    db.commit()

    return jsonify({'message': 'success'})

if __name__ == "__main__":
   application.run(host='0.0.0.0')
import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

def db_cursor():
    return mysql.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWD,
                         db=DB_NAME).cursor()

def get_weather_report():
    with db_cursor() as cs:
        cs.execute("""
            SELECT country, main, humidity, description
            FROM owr
        """)
        result = [models.WeatherReport(*row) for row in cs.fetchall()]
        return result

def get_weather_report_details(country):
    pro = '%' + country + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT main, humidity, description
            FROM owr
            WHERE country like %s
        """, [pro])
        result = [models.WeatherReport(*row) for row in cs.fetchall()]
        return result

def get_dam_level():
    with db_cursor() as cs:
        cs.execute("""
            SELECT date, sector, water_retention, can_receive_more
            FROM damlevel
        """)
        result = [models.DamLevel(*row) for row in cs.fetchall()]
        return result

def get_dam_level_details(sector):
    pro = '%' + sector + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT date, water_retention, can_receive_more
            FROM damlevel
            WHERE sector like %s
        """, [pro])
        result = [models.DamLevel(*row) for row in cs.fetchall()]
        return result

def get_forecast():
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, TAMBON_T, AMPHOE_T, PROV_T, Type, sector
            FROM forecast
        """)
        result = [models.Forecast(*row) for row in cs.fetchall()]
        return result

def get_forecast_details(Type):
    pro = '%' + Type + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT month, TAMBON_T, AMPHOE_T, PROV_T, sector
            FROM forecast
            WHERE Type like %s
        """, [pro])
        result = [models.Forecast(*row) for row in cs.fetchall()]
        return result

def get_questionnaire():
    with db_cursor() as cs:
        cs.execute("""
            SELECT sector, province, amphoe, warning_freq, warning_way, want_warning_way, type, flood_freq, rain_freq
            FROM survey
        """)
        result = [models.questionnaire(*row) for row in cs.fetchall()]
        return result

def get_questionnaire_details(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT sector, amphoe, warning_freq, warning_way, want_warning_way, type, flood_freq, rain_freq
            FROM survey
            WHERE province like %s
        """, [pro])
        result = [models.questionnaire(*row) for row in cs.fetchall()]
        return result

def get_rain_freq_and_damlevel(sector):
    # sec = '%' + sector + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT q.sector, q.province, q.rain_freq, d.can_receive_more, d.water_retention 
            FROM survey q 
            INNER JOIN damlevel d 
            WHERE d.sector = q.sector and q.sector like %s
        """, [sector])
        result = cs.fetchall()
        return models.RainFreqLevel(*result)


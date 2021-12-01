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
            SELECT sector, main, humidity, description, ts, province
            FROM owr
        """)
        result = [models.WeatherReport(*row) for row in cs.fetchall()]
        return result

def get_weather_report_details(sector):
    pro = '%' + sector + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT province, main, humidity, description, ts
            FROM owr
            WHERE sector like %s
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
        result = [models.Questionnaire(*row) for row in cs.fetchall()]
        return result

def get_questionnaire_details(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT sector, amphoe, warning_freq, warning_way, want_warning_way, type, flood_freq, rain_freq
            FROM survey
            WHERE province like %s
        """, [pro])
        result = [models.Questionnaire(*row) for row in cs.fetchall()]
        return result

def get_rain_freq_and_damlevel(province):
    prov = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT q.sector, q.province, q.rain_freq, d.can_receive_more, d.water_retention 
            FROM survey q 
            INNER JOIN damlevel d 
            WHERE  q.province like %s and d.sector = q.sector
        """, [prov])
        result = [models.RainFreqLevel(*row) for row in cs.fetchall()]
        return result

def get_forecast_damlevel(province):
    prov = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
           SELECT f.sector, f.`PROV_T`, f.`Type`, d.can_receive_more, d.water_retention, d.date
           FROM forecast f 
           INNER JOIN damlevel d 
           WHERE d.sector = f.sector and f.PROV_T like %s
        """, [prov])
        result = [models.ForecastDamLevel(*row) for row in cs.fetchall()]
        return result

def get_qestion_avg_rain_freq(sector):
    sec = '%' + sector + '%'
    with db_cursor() as cs:
        cs.execute("""
                SELECT sector, ROUND(AVG(rain_freq),2) avg_rain_freq
                FROM survey
                WHERE sector like %s
                GROUP BY sector
            """, [sec])
        result = [models.QuestionRainFreq(*row) for row in cs.fetchall()]
        return result

def get_owr_avg_humidity(sector):
    sec = '%' + sector + '%'
    with db_cursor() as cs:
        cs.execute("""
                SELECT sector, ROUND(AVG(humidity),2) avg_rain_freq
                FROM owr
                WHERE sector like %s
                GROUP BY sector
            """, [sec])
        result = [models.OwrHumidity(*row) for row in cs.fetchall()]
        return result
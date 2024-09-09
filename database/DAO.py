from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct(year(s.`datetime`)) as y
from new_ufo_sightings.sighting s 
order by y desc

                                             """
        cursor.execute(query, ())
        for row in cursor:
            result.append(row["y"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getForme():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct(shape) as s
from new_ufo_sightings.sighting s 
where shape!=''
order by s



                                                 """
        cursor.execute(query, ())
        for row in cursor:
            result.append(row["s"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getNodi(forma, anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select s.id as id
from new_ufo_sightings.sighting s 
where shape=%s and year(s.`datetime`)=%s """
        cursor.execute(query, (forma, anno))
        for row in cursor:
            result.append(row["id"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getDizArcoLongitudini(forma, anno):
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """select s1.id as a1, s2.id as a2, s1.longitude as l1, s2.longitude as l2
from new_ufo_sightings.sighting s1, new_ufo_sightings.sighting s2
where s1.id in (select s.id as id from new_ufo_sightings.sighting s where shape=%s and year(s.`datetime`)=%s and s.shape!='' )
	  and s2.id in (select s.id as id from new_ufo_sightings.sighting s where shape=%s and year(s.`datetime`)=%s and s.shape!=''  )
	  and s1.state=s2.state 
	  and s1.id<s2.id 
	  and s1.longitude!=s2.longitude
"""
        cursor.execute(query, (forma, anno, forma, anno))
        for row in cursor:
            result[(row['a1'], row['a2'])]=(row['l1'], row['l2'])

        cursor.close()
        conn.close()
        return result





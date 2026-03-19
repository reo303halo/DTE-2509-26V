# pip install mysql-connector-python
# pip install dotenv
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

class DataBase():
    def __init__(self):
        self.mysqlConnector = mysql.connector.connect(
            host="localhost", #:3306
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="dte_2509"
        )

    def __enter__(self):
        try:
            self.cursor = self.mysqlConnector.cursor()
            return self
        except mysql.connector.Error as error:
            print("Error while connecting to MySQL", error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mysqlConnector.commit()
        self.cursor.close()
        self.mysqlConnector.close()


    def getAllData(self):
        self.cursor.execute("SELECT * FROM film;")
        return self.cursor.fetchall()
    
    def getMovieById(self, movie_id):
        self.cursor.execute("SELECT * FROM film WHERE fnr = %s", (movie_id, )) # Note that the single parameter is made as a tuple.
        return self.cursor.fetchone()

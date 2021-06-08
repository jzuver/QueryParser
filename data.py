#import sqlite
import os
import subprocess
import sqlite3
from sqlite3 import Error


"""
sqliteConnect
param: none
return: sqlite cursor object for data.db or print error
"""

def sqliteConnect():
    try:
        cur = sqlite3.connect('data.db')
        return cur
    except Error:
        print(Error)


"""
initDb
param: none
funtion: to open os connection to db, process create.sql file to flush database, change database mode to read csv, read in losers.csv and insults.  csv to database
return: none
"""

def initDb():
    os.system("sqlite3 data.db \".read create.sql\" \".mode csv\" \".import Losers.csv Losers\" \".import Insults.csv Insults\"")

   
"""
fetch
param inputs: cur: a sqlite cursor object, userInput: a string looked for in the database, table: a string to specify which table to query,
column: a string to specify which column to query, id: a string used to query the join statement id
return: A string retrieved from the sqlite database
"""

def fetch(cur, userInput, table="null", column="null", id="null"):
    cursor = cur.cursor()
    if table == "null":
        script = "SELECT tweet FROM Insults i, Losers l Where l.loser_id = i.loser_id  AND l.name = " +"\""+userInput+"\""
        cursor.execute(script)
        row = cursor.fetchone()
        if not (row is None):
            return row[0]
        else:
            return "Result not found!"

    script = "SELECT "+column+" FROM "+table+" WHERE "+id+" = "+"\""+userInput+"\""
    cursor.execute(script)
    row = cursor.fetchone()
    if not (row is None):
        return row[0]
    else:
        return "Result not found!"




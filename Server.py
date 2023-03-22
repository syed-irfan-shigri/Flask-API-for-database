from flask import Flask, request, jsonify
import mysql.connector as mysql
from fastapi import FastAPI
from flask_cors import CORS


app = FastAPI()
conn = mysql.connect(host="localhost", user="root", password="", database="test_fast_api")

@app.get("/get-all-data")
def allData():
    curs=conn.cursor(dictionary=True)
    curs.execute("SELECT * from items")
    temp=curs.fetchall()
    for a in temp:
        print(a)
    return temp

@app.get("/get-data-by-id/{id}")
def getDataById(id: int):
    curs=conn.cursor(dictionary=True)
    query="SELECT * from items where id="+ str(id)
    curs.execute(query)
    temp=curs.fetchall()
    return temp


@app.get("/delete-data-by-id/{id}")
def deleteDataById(id: int):
    curs=conn.cursor(dictionary=True)
    query="DELETE FROM items where id="+ str(id)
    curs.execute(query)
    conn.commit()
    return "Deleted successfully"



@app.post("/post-data")
def postdata(item_name:str , item_price:int, item_status:int ):
        curs=conn.cursor(dictionary=True)
        query = "Insert into items (`item_name`, `item_price`, `item_status`) values ('"+item_name+"',"+str(item_price)+","+str(item_status)+")"
        curs.execute(query)
        conn.commit()
        return "Data successfully inserted into database"

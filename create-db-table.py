import sqlite3
conn=sqlite3.connect("project.db")
cur=conn.cursor()
#create table
cur.execute("DROP TABLE IF EXISTS users")
query="""CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    username TEXT NOT NULL UNIQUE,
    password TEXT

)"""
cur.execute(query)

cur.execute("DROP TABLE IF EXISTS decks")
query3="""CREATE TABLE decks(
    deckid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    deckname TEXT NOT NULL

)"""
cur.execute(query3)

cur.execute("DROP TABLE IF EXISTS cards")
query1=""" CREATE TABLE cards (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    deckname TEXT NOT NULL,
    front TEXT,
    back TEXT

)"""
cur.execute(query1)

conn.commit()
conn.close()

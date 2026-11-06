#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""14. Kengaytirilgan Todo"""
import sqlite3
from datetime import datetime, timedelta
class Todo:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, priority INTEGER, due_date TEXT, done INTEGER DEFAULT 0)")
        self.conn.commit()
    def add(self, title, priority=2, days=0):
        due = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        self.conn.execute("INSERT INTO tasks (title, priority, due_date) VALUES (?,?,?)", (title, priority, due))
        self.conn.commit(); print("✅")
    def today(self):
        t = datetime.now().strftime("%Y-%m-%d")
        return self.conn.execute("SELECT id, title, priority, due_date FROM tasks WHERE due_date<=? AND done=0 ORDER BY priority", (t,)).fetchall()
    def done(self, tid):
        self.conn.execute("UPDATE tasks SET done=1 WHERE id=?", (tid,)); self.conn.commit(); print("✅")
def main():
    t = Todo()
    while True:
        print("\n1.Qoshish 2.Bugungi 3.Bajarildi 4.Chiqish")
        c = input("> ")
        if c=="1": t.add(input("Vazifa: "), int(input("Prioritet: ") or 2), int(input("Kun: ") or 0))
        elif c=="2":
            for r in t.today(): print(r)
        elif c=="3": t.done(int(input("ID: ")))
        elif c=="4": break
if __name__ == "__main__": main()

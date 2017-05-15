import sqlite3

db = sqlite3.connect("informal.db")

def CreateTable():
    db.row_factory = sqlite3.Row
    db.execute("create table  Admin(Name text, Age int)")
    db.commit()
def Add(Name,Age):
    db.row_factory = sqlite3.Row
    db.execute("create table  Admin(Name text, Age int)")
    # Add records
    db.execute("insert into Admin(Name,Age) values(?,?)", ("Mody", 25))
    db.execute("insert into Admin(Name,Age) values(?,?)", ("Loshi", 21))
    db.execute("insert into Admin(Name,Age) values(?,?)", ("Foshi", 23))
    db.commit()
    print("Record is added")

def main():
    CreateTable()
    IndexOp = int(input("Select Operation, 1- Add:"))
    if(IndexOp==1):
        Name=input("Enter name:")
        Age=int(input("Enter Age:"))
        Add(Name,Age)
if __name__ == '__main__':main()

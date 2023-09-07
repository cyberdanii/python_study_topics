from time import sleep, perf_counter
from threading import Thread
import random

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="da98ni11el30",
  database="pn_blog"
)
def insertar():
    with mydb.cursor() as mycursor:

        sql = [f"INSERT INTO prueba (codigo) VALUES ({str(random.random()+x)});" for x in range(0, 100)]
        for query in sql:
            mycursor.execute(query)
            mydb.commit()

        mycursor.execute("SELECT * FROM prueba")

        myresult = mycursor.fetchall()

        # for x in myresult:
        #     print(x)

def seleccionar():
    with mydb.cursor() as mycursor:
        mycursor.execute("SELECT * FROM prueba")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print('done')


start_time = perf_counter()

# create and start 10 threads
threads = []
for n in range(1, 11):
    t = Thread(target=seleccionar)
    threads.append(t)
    t.start()

# wait for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
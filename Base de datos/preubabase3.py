from peewee import PostgresqlDatabase, AutoField, CharField, DateField, ForeignKeyField, Model, DateTimeField
from datetime import datetime

ahora = datetime.now()

pg_db = PostgresqlDatabase("my_db", user="uji_motorsport", password="ujimotorsport", host="localhost", port=5432)


class Prueba(Model):
   Id = AutoField()
   revoluciones = CharField()
   timestop = DateTimeField()
   
   class Meta:
       database = pg_db

pg_db.connect()

pg_db.create_tables([Prueba])


chamo = Prueba( Id='1',
                   revoluciones='50',
                   timestop= ahora)

chamo.save(force_insert=True)

for i in Prueba.select():
     print('Id: {} - revoluciones: {} - timestop: {}'
     .format(Prueba.Id, Prueba.revoluciones, Prueba.timestop))
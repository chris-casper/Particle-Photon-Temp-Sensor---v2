from pyparticleio.ParticleCloud import ParticleCloud  
import MySQLdb
import time
import datetime
import arrow

access_token = "###PARTICLE_ACCESS_TOKEN_HERE##"
particle_cloud = ParticleCloud(username_or_access_token=access_token)
tempF = particle_cloud.sensor04.tempF
connected = particle_cloud.sensor04.connected
timestamp = arrow.now().to('US/Eastern')

db = MySQLdb.connect (host = "localhost",
                              user = "###SQL_WRITE_ACCOUNT_HERE##",
                              passwd = "###SQL_WRITE_ACCOUNT_PW_HERE##",
                              db = "###SQL_DB_HERE##")
cursor = db.cursor()
cursor.execute('''INSERT INTO ###SQL_DB_HERE## VALUES (%s,%s,%s)''',(tempF, timestamp, connected))
db.commit()
db.close()
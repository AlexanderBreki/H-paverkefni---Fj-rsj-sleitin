# Creates a single table and writes data to it
import sqlite3
conn = sqlite3.connect('verslanir.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS verslun (titill CHAR(50))""")
c.execute("""INSERT INTO verslun VALUES ('Bragi')""")
c.execute("""INSERT INTO verslun VALUES ('Oliver')""")
conn.commit() # Save changes
c.execute("""SELECT * FROM verslun""")
# Iterate over the results
for row in c:
    print (row)
c.close() # Close the connection

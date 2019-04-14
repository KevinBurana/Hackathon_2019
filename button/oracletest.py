#!/usr/bin/python3

import cx_Oracle

connectionString = "(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = cedar.humboldt.edu)(PORT = 1521)(CONNECTION_DATA = (SID = STUDENT)))"

con = cx_Oracle.connect(connectionString)
cur = con.cursor()

param = 'SH130c';

cur.callproc('kiosk_update',[param])

cur.close()
con.close()

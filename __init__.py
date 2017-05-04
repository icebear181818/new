
import MySQLdb


connection=MySQLdb.connect(host="localhost",user="root",passwd="maxdos1234",db="test")
cursor=connection.cursor()
a=[1,2]
sql="SELECT * FROM test.test WHERE number in ("
# for i in a:
#
#     sql="SELECT * FROM test.test WHERE number="+str(i)
#     cursor.execute(sql)
#     print cursor.fetchall()
# for i in a:
#     sql = sql+ str(i)+','
#
# sql=sql[:-1]
# sql=sql+')'
# print sql




# args=['A', 'C']
# sql='SELECT fooid FROM foo WHERE bar IN (%s)'
# in_p=', '.join(map(lambda x: '%s', args))
# sql = sql % in_p
# cursor.execute(sql, args)

tem=','.join(['1','2'])
print tem
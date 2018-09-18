#!/usr/bin/python2
import cgi
import cgitb;cgitb.enable()
import commands
import mysql.connector as mariadb
#print "Content-type:text/html"
#print ""
#webdata=cgi.FieldStorage()
#username=webdata.getvalue('username')
f=open("/var/www/html/store/dn.txt",'rb')
username=f.read()
f.close()
conn=mariadb.connect(host='localhost',user='root',password='q',database='ebook')

cursor=conn.cursor()
cursor.execute('Select * from user where Username="{}";'.format(username))
chk=cursor.fetchall()
i=chk[0][3]
commands.getoutput('sudo lvcreate --name '+i+'  -V10G  --thin ebook/pool1')
commands.getoutput('sudo mkfs.xfs /dev/ebook/'+i)
commands.getoutput('sudo mkdir /var/www/html/store/'+i)
commands.getoutput('sudo mount /dev/ebook/'+i+'  /var/www/html/store/'+i)




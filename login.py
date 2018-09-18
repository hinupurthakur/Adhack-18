#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb

print "Content-type:text/html"
print ""

conn=mariadb.connect(host='localhost',user='root',password='q',database='ebook')
cursor=conn.cursor()

web_data=cgi.FieldStorage()
username=web_data.getvalue('username')
password= web_data.getvalue('password')
cursor.execute('Select * from user where Password="{}" and Username="{}";'.format(password,username))
chk=cursor.fetchall()
if len(chk)==0:
	print "<h1>"
        print "Incorrect Data"
        print "</h1>"
        print "<a href='http://52.207.241.131/edrive/login.html'>"
        print "Click here for redirection"
        print "</a>"


else:
	name=chk[0][1]
	email=chk[0][2]
	username=chk[0][3]
	contact=chk[0][5]
	city=chk[0][6]
	url='http://52.207.241.131/store/'+username
	f=open("/var/www/html/store/dn.txt","w")
        f.write(username)
        f.close()

	html='''<html lang="en">

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My Account| BookSpot</title>
        <link href="http://52.207.241.131/edrive/css/bootstrap.css" rel="stylesheet">
        <link href="http://52.207.241.131/edrive/css/style.css" rel="stylesheet">
        <script src="http://52.207.241.131/edrive/js/jquery.js"></script>
        <script src="http://52.207.241.131/edrive/js/bootstrap.min.js"></script>
    </head>

    <body style="padding-top: 50px;">
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>                        
                    </button>
                    <a class="navbar-brand" href="http://52.207.241.131/edrive/index.html"><span class="glyphicon glyphicon-globe"></span>BookSpot</a>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
		 <li><a href="http://52.207.241.131/edrive/upload.html"><span class="glyphicon glyphicon-upload"></span> Upload</a></li>'''
	print html
	print'<li><a href='+url+'><span class="glyphicon glyphicon-book"></span> Library</a></li>'

	html1='''<li><a href="http://52.207.241.131/edrive/explore.html"><span class="glyphicon glyphicon-tasks"></span> Explore</a></li>
                       
                        <li><a href="http://52.207.241.131/edrive/index.html"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>
                    </ul>
                </div>
            </div>
        </div>
 		  <div class="container-fluid decor_bg" id="content">
            <div class="row">
                <div class="container">
                    <div>
                        <h2>HELLO BOOKWORM</h2>
			 <h3>WELCOME TO YOUR BookSpot.</h3>'''
	print html1
  	print '<h3> Name:<font color=blue>'	
	print name
	print '</font></h3>'
	print '<h3> Email:<font color=blue>'	
	print email
	print '</font></h3>'
        print '<h3> Username:<font color=blue>'
        print username
	print '</font></h3>'
	print '<h3> Contact No:<font color=blue>'	
	print contact
	print '</font></h3>'
	print '<h3> City:<font color=blue>'	
	print city
	print '</font></h3>'	
	f=open("/var/www/html/store/dn.txt","w")
	f.write(username)
	f.close()
	ht='''
   	    </div>         
                 </div>
               </div>
            </div>
                </div>
            </div>
        </div>
			
			
        <footer>
            <div class="container">
                <center>
                    <p>Copyright &copy; BookSpot. All Rights Reserved  |  Contact Us: +91 9772139728  +91 8755366285</p>	
                </center>
            </div>
        </footer>
    </body>
</html>'''
	print ht


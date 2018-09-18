#!/usr/bin/python2

import cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb

print "Content-type:text/html"
print ""

web_data=cgi.FieldStorage()

name= web_data.getvalue('name')
email= web_data.getvalue('e-mail')
username=web_data.getvalue('username')
password= web_data.getvalue('password')
contact= web_data.getvalue('contact')
address= web_data.getvalue('address')
city= web_data.getvalue('city')

conn=mariadb.connect(user='root',password='q',database='ebook',host='localhost')

cursor=conn.cursor()

cursor.execute('select Username from user where Username="{}";'.format(username))
out=cursor.fetchall()
if len(out)>0:
	print "<h1>"
	print "Username Already Exists."
	print "</h1>"
	print  "<meta http-equiv='refresh' content='3;http://52.207.241.131/signup.html'>"

else :

	cursor.execute('insert into user (Name,Email,Username,Password,Contact,Address,City)values("{}","{}","{}","{}","{}","{}","{}");'.format(name,email,username,password,contact,address,city))

	
	conn.commit() 
	f=open("/var/www/html/store/dn.txt","w")
        f.write(username)
        f.close()

	execfile('/var/www/cgi-bin/drive.py')
        url='http://52.207.241.131/store/' + username

	html='''<html lang="en">

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My Account| BookSpot</title>
        <link href="http://52.207.241.131/edrive/css/bootstrap.min.css" rel="stylesheet">
        <link href="http://52.207.241.131/edrive/css/style.css" rel="stylesheet">
        <script src="http://52.207.241.131/edrive/js/jquery.js"></script>
        <script src="http://52.207.241.131/edrive/js/bootstrap.min.js"></script>
    </head>

    <body>
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>                        
                    </button>
                    <a class="navbar-brand" href="index.html"><span class="glyphicon glyphicon-globe"></span>BookSpot</a>
                </div>
                <div class="collapse navbar-collapse" id="myNavbar">
                    <ul class="nav navbar-nav navbar-right">
		 <li><a href="http://52.207.241.131/edrive/upload.html"><span class="glyphicon glyphicon-upload"></span> Upload</a></li>'''
	print html
	print '<li><a href='
	print url
	print '><span class="glyphicon glyphicon-book"></span> Library</a></li>'
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
                       
			<h2>Hello Bookworm</h2>
			<h3>Welcome to your BookSpot</h3>
		'''
	print html1	
	print '<h3>'
	print '</h3>'
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
	

	ht='''	</div>         
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


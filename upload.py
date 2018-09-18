#!/usr/bin/python2
import cgi, os,commands
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass
print "Content-type:text/html"
print ""
form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename.replace("\\","/"))
    f=open("/var/www/html/store/dn.txt",'rb')
    drive=f.read()
    f.close()
    #drive=commands.getoutput('sudo cat /var/www/html/store/dn.txt')
    commands.getoutput('sudo chmod 777 /var/www/html/store/'+drive)
    
    open('/var/www/html/store/'+drive+'/' + fn, 'wb').write(fileitem.file.read())
    print '<h2>'
    print "Book successfully uploaded"
    print '</h2>'
    print '<a href="http://52.207.241.131/edrive/explore.html">'
    print 'Click Here to Continue'
    print '</a>'

else:
    print  '<h2>'
    print  'No file was uploaded'
    print  '</h2>'

import sys
import MySQLdb
import memcache

memc = memcache.Client(['192.168.1.2'], debug=1);

try:
    conn = MySQLdb.connect (host = "192.168.1.2",
                            user = "david",
                            passwd = "da3020291",
                            db = "world")
except MySQLdb.Error, e:    
     print "Error %d: %s" % (e.args[0], e.args[1])
     sys.exit (1)

popularfilms = memc.get('Country')

if not popularfilms:
    cursor = conn.cursor()
    cursor.execute('select name, population from Country where population >= 10000 order by population desc limit 10;')
    rows = cursor.fetchall()
    memc.set('Country',rows,60)
    print "Updated memcached with MySQL data"
else:
    print "Loaded data from memcached"
    for row in popularfilms:
        print "%s, %s" % (row[0], row[1])
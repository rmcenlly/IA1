from bottle import redirect, install, view, route, request, run, static_file
from bottle_sqlite import SQLitePlugin
import sqlite3
from sqlite3 import Error

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./static_files')

@route('/img/<filename>')
def img(filename):
    return static_file(filename, root='./img')

@route('/houses/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/burchill/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/burling/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/day/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/fradgley/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/hobart/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/mcintosh/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/rapp/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/reeves/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/houses/img/<filename>')
def houses(filename):
    return static_file(filename, root='./houses')

@route('/')
@view('home')
def home():
    return dict()

@route('/students')
@view('students')
def students():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students")
    rows = c.fetchall()
    
    return dict(rows=rows)

@route('/entries')
@view('entries')
def entries():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("""SELECT tbl_entries.EntryID, tbl_students.StudentID, tbl_students.FirstName, tbl_students.LastName, tbl_students.Gender, tbl_students.House, tbl_students.Age, tbl_events.EventID, tbl_events.Event, tbl_events.Type 
    FROM tbl_students, tbl_events
    INNER JOIN tbl_entries ON tbl_entries.EventID = tbl_events.EventID and tbl_entries.StudentID=tbl_students.StudentID
    ORDER BY EntryID""")
    rows = c.fetchall()
    
    return dict(rows=rows)
    
@route('/entries/delete', method='POST')
def deleteEntry():
    id = request.forms.get('id')
    conn = sqlite3.connect('IA1.db')
    conn.execute("DELETE FROM tbl_entries WHERE EntryID = ?", (id,))
    conn.commit()

    redirect ("/entries")

@route('/events')
@view('events')
def events():
    return dict()

@route('/events/track')
@view('track')
def track():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT Event FROM tbl_events WHERE Type='Track'")  
    rows = c.fetchall()
    
    return dict(rows=rows)

@route('/events/field')
@view('field')
def track():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT Event FROM tbl_events WHERE Type='Field'")  
    rows = c.fetchall()
    
    return dict(rows=rows)

@route('/houses')
@view('houses/houses')
def houses():
    return dict()


@route('/houses/burchill', method='GET')
@view('houses/burchill/burchill')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Age=18")
    eighteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Age=19")
    nineteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens, nineteens=nineteens)

@route('/houses/burchill/15m', method='GET')
@view('houses/burchill/15m')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/15m/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/15m")

@route('/houses/burchill/15f', method='GET')
@view('houses/burchill/15f')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/15f/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/15f")

@route('/houses/burchill/16m', method='GET')
@view('houses/burchill/16m')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/16m/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/16m")

@route('/houses/burchill/16f', method='GET')
@view('houses/burchill/16f')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/16f/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/16f")

@route('/houses/burchill/17m', method='GET')
@view('houses/burchill/17m')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/17m/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/17m")

@route('/houses/burchill/17f', method='GET')
@view('houses/burchill/17f')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/17f/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/17f")

@route('/houses/burchill/18m', method='GET')
@view('houses/burchill/18m')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/18m/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/18m")

@route('/houses/burchill/18f', method='GET')
@view('houses/burchill/18f')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/18f/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/18f")

@route('/houses/burchill/19f', method='GET')
@view('houses/burchill/19f')
def bl():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BL' AND Gender='F' AND Age=19")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burchill/19f/submit', method='POST')
def blsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burchill/19f")














@route('/houses/burling', method='GET')
@view('houses/burling/burling')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=18")
    eighteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=19")
    nineteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens, nineteens=nineteens)

@route('/houses/burling/15m', method='GET')
@view('houses/burling/15m')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/15m/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/15m")

@route('/houses/burling/15f', method='GET')
@view('houses/burling/15f')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/15f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/15f")

@route('/houses/burling/16m', method='GET')
@view('houses/burling/16m')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/16m/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/16m")

@route('/houses/burling/16f', method='GET')
@view('houses/burling/16f')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/16f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/16f")

@route('/houses/burling/17m', method='GET')
@view('houses/burling/17m')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/17m/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/17m")

@route('/houses/burling/17f', method='GET')
@view('houses/burling/17f')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/17f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/17f")

@route('/houses/burling/18m', method='GET')
@view('houses/burling/18m')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/18m/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/18m")

@route('/houses/burling/18f', method='GET')
@view('houses/burling/18f')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/18f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/18f")

@route('/houses/burling/19f', method='GET')
@view('houses/burling/19f')
def bg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=19")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/burling/19f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/burling/19f")












    

@route('/houses/day', method='GET')
@view('houses/day/day')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Age=18")
    eighteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Age=19")
    nineteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens, nineteens=nineteens)

@route('/houses/day/15m', method='GET')
@view('houses/day/15m')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/15m/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/15m")

@route('/houses/day/15f', method='GET')
@view('houses/day/15f')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/15f/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/15f")

@route('/houses/day/16m', method='GET')
@view('houses/day/16m')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/16m/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/16m")

@route('/houses/day/16f', method='GET')
@view('houses/day/16f')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/16f/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/16f")

@route('/houses/day/17m', method='GET')
@view('houses/day/17m')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/17m/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/17m")

@route('/houses/day/17f', method='GET')
@view('houses/day/17f')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/17f/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/17f")

@route('/houses/day/18m', method='GET')
@view('houses/day/18m')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/18m/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/18m")

@route('/houses/day/18f', method='GET')
@view('houses/day/18f')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/18f/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/18f")

@route('/houses/day/19f', method='GET')
@view('houses/day/19f')
def dy():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'DY' AND Gender='F' AND Age=19")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/day/19f/submit', method='POST')
def dysub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/day/19f")












    

@route('/houses/fradgley', method='GET')
@view('houses/fradgley/fradgley')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Age=18")
    eighteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Age=19")
    nineteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens, nineteens=nineteens)

@route('/houses/fradgley/15m', method='GET')
@view('houses/fradgley/15m')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/15m/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/15m")

@route('/houses/fradgley/15f', method='GET')
@view('houses/fradgley/15f')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/15f/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/15f")

@route('/houses/fradgley/16m', method='GET')
@view('houses/fradgley/16m')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/16m/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/16m")

@route('/houses/fradgley/16f', method='GET')
@view('houses/fradgley/16f')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/16f/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/16f")

@route('/houses/fradgley/17m', method='GET')
@view('houses/fradgley/17m')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/17m/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/17m")

@route('/houses/fradgley/17f', method='GET')
@view('houses/fradgley/17f')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/17f/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/17f")

@route('/houses/fradgley/18m', method='GET')
@view('houses/fradgley/18m')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/18m/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/18m")

@route('/houses/fradgley/18f', method='GET')
@view('houses/fradgley/18f')
def fg():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'FG' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/fradgley/18f/submit', method='POST')
def fgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/fradgley/18f")


    return dict(events=events, students=students)












    

@route('/houses/hobart', method='GET')
@view('houses/hobart/hobart')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Age=18")
    eighteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Age=19")
    nineteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens, nineteens=nineteens)

@route('/houses/hobart/15m', method='GET')
@view('houses/hobart/15m')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/15m/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/15m")

@route('/houses/hobart/15f', method='GET')
@view('houses/hobart/15f')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/15f/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/15f")

@route('/houses/hobart/16m', method='GET')
@view('houses/hobart/16m')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/16m/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/16m")

@route('/houses/hobart/16f', method='GET')
@view('houses/hobart/16f')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/16f/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/16f")

@route('/houses/hobart/17m', method='GET')
@view('houses/hobart/17m')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/17m/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/17m")

@route('/houses/hobart/17f', method='GET')
@view('houses/hobart/17f')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/17f/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/17f")

@route('/houses/hobart/18m', method='GET')
@view('houses/hobart/18m')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/18m/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/18m")

@route('/houses/hobart/18f', method='GET')
@view('houses/hobart/18f')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/18f/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/18f")

@route('/houses/hobart/19m', method='GET')
@view('houses/hobart/19m')
def ht():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'HT' AND Gender='M' AND Age=19")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/hobart/19m/submit', method='POST')
def htsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/hobart/19m")












    

@route('/houses/mcintosh', method='GET')
@view('houses/mcintosh/mcintosh')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Age=18")
    eighteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Age=19")
    nineteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens, nineteens=nineteens)

@route('/houses/mcintosh/15m', method='GET')
@view('houses/mcintosh/15m')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/15m/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/15m")

@route('/houses/mcintosh/15f', method='GET')
@view('houses/mcintosh/15f')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/15f/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/15f")

@route('/houses/mcintosh/16m', method='GET')
@view('houses/mcintosh/16m')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/16m/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/16m")

@route('/houses/mcintosh/16f', method='GET')
@view('houses/mcintosh/16f')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/16f/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/16f")

@route('/houses/mcintosh/17m', method='GET')
@view('houses/mcintosh/17m')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/17m/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/17m")

@route('/houses/mcintosh/17f', method='GET')
@view('houses/mcintosh/17f')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/17f/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/17f")

@route('/houses/mcintosh/18m', method='GET')
@view('houses/mcintosh/18m')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/18m/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/18m")

@route('/houses/mcintosh/18f', method='GET')
@view('houses/mcintosh/18f')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/18f/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/18f")

@route('/houses/mcintosh/19f', method='GET')
@view('houses/mcintosh/19f')
def mc():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'MC' AND Gender='F' AND Age=19")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/mcintosh/19f/submit', method='POST')
def mcsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/mcintosh/19f")












    

@route('/houses/rapp', method='GET')
@view('houses/rapp/rapp')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Age=18")
    eighteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens)

@route('/houses/rapp/15m', method='GET')
@view('houses/rapp/15m')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/15m/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/15m")

@route('/houses/rapp/15f', method='GET')
@view('houses/rapp/15f')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/15f/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/15f")

@route('/houses/rapp/16m', method='GET')
@view('houses/rapp/16m')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/16m/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/16m")

@route('/houses/rapp/16f', method='GET')
@view('houses/rapp/16f')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/16f/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/16f")

@route('/houses/rapp/17m', method='GET')
@view('houses/rapp/17m')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/17m/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/17m")

@route('/houses/rapp/17f', method='GET')
@view('houses/rapp/17f')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/17f/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/17f")

@route('/houses/rapp/18m', method='GET')
@view('houses/rapp/18m')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/18m/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/18m")

@route('/houses/rapp/18f', method='GET')
@view('houses/rapp/18f')
def rp():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RP' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/rapp/18f/submit', method='POST')
def rpsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/rapp/18f")












    

@route('/houses/reeves', method='GET')
@view('houses/reeves/reeves')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Age=18")
    eighteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Age=19")
    nineteens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, eighteens=eighteens, nineteens=nineteens)

    return dict(students=students, events=events)

@route('/houses/reeves/15m', method='GET')
@view('houses/reeves/15m')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/15m/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/15m")

@route('/houses/reeves/15f', method='GET')
@view('houses/reeves/15f')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/15f/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/15f")

@route('/houses/reeves/16m', method='GET')
@view('houses/reeves/16m')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/16m/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/16m")

@route('/houses/reeves/16f', method='GET')
@view('houses/reeves/16f')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/16f/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/16f")

@route('/houses/reeves/17m', method='GET')
@view('houses/reeves/17m')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/17m/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/17m")

@route('/houses/reeves/17f', method='GET')
@view('houses/reeves/17f')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/17f/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/17f")

@route('/houses/reeves/18m', method='GET')
@view('houses/reeves/18m')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='M' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/18m/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/18m")

@route('/houses/reeves/18f', method='GET')
@view('houses/reeves/18f')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='F' AND Age=18")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/18f/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/18f")

@route('/houses/reeves/19f', method='GET')
@view('houses/reeves/19f')
def rv():
    conn = sqlite3.connect('IA1.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'RV' AND Gender='F' AND Age=19")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/houses/reeves/19f/submit', method='POST')
def rvsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('IA1.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/houses/reeves/19f")


run(host='localhost', port=8080, debug=True)
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

@route('/burling/<filename>')
def burling(filename):
    return static_file(filename, root='./')

@route('/burling/img/<filename>')
def burling(filename):
    return static_file(filename, root='./burling')

@route('/')
@view('home')
def home():
    return dict()

@route('/entries')
@view('entries')
def entries():
    conn = sqlite3.connect('burling.db')
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
    conn = sqlite3.connect('burling.db')
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
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT Event FROM tbl_events WHERE Type='Track'")  
    rows = c.fetchall()
    
    return dict(rows=rows)

@route('/events/field')
@view('field')
def track():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT Event FROM tbl_events WHERE Type='Field'")  
    rows = c.fetchall()
    
    return dict(rows=rows)

@route('/burling', method='GET')
@view('burling/burling')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    
    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=15")
    fifteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=16")
    sixteens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age=17")
    seventeens=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Age>17")
    opens=c.fetchall()

    return dict(fifteens=fifteens, sixteens=sixteens, seventeens=seventeens, opens=opens)

@route('/burling/15m', method='GET')
@view('burling/15m')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/15m/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/15m")

@route('/burling/15f', method='GET')
@view('burling/15f')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=15")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/15f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/15f")

@route('/burling/16m', method='GET')
@view('burling/16m')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/16m/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/16m")

@route('/burling/16f', method='GET')
@view('burling/16f')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=16")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/16f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/16f")

@route('/burling/17m', method='GET')
@view('burling/17m')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/17m/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/17m")

@route('/burling/17f', method='GET')
@view('burling/17f')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age=17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/17f/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/17f")

@route('/burling/openm', method='GET')
@view('burling/openm')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='M' AND Age>17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/openm/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/openm")

@route('/burling/openf', method='GET')
@view('burling/openf')
def bg():
    conn = sqlite3.connect('burling.db')
    c = conn.cursor()
    c.execute("SELECT EventID, Event, Type FROM tbl_events")
    events=c.fetchall()

    c.execute("SELECT StudentID, FirstName, LastName, Gender, House, Age FROM tbl_students WHERE House = 'BG' AND Gender='F' AND Age>17")
    students=c.fetchall()


    return dict(events=events, students=students)

@route('/burling/openf/submit', method='POST')
def bgsub():
    StudentID = request.forms.get('StudentID')
    EventID = request.forms.get('EventID')
    conn = sqlite3.connect('burling.db')
    conn.execute("INSERT INTO tbl_entries (StudentID, EventID) VALUES (?, ?)", [StudentID, EventID])
    conn.commit()

    redirect ("/burling/openf")


run(host='localhost', port=8080, debug=True)
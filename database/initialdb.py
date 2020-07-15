from datetime import datetime
from firebase_admin import credentials, initialize_app, db
from process import isCamsOpen

cred = credentials.Certificate('database/cred.json')
initialize_app(cred, {
    'databaseURL': 'https://tryy-e6595.firebaseio.com/'
})
ref = db.reference('raspicam')
year = '{}'.format(datetime.today().year)
month = '{}'.format(datetime.today().month)
month = '0' + month if len(month) == 1 else month
day = '{}'.format(datetime.today().day)
day = '0' + day if len(day) == 1 else day
firebase = ref.child(year).child(month).child(day)


def initialdb():
    global ref
    data_today()
    return ref


def data_today():
    global ref
    global firebase
    # cam0 initialize data
    if firebase.child('in').get() is None:
        firebase.update({'in': 0})
    else:
        isCamsOpen.p_in = firebase.child('in').get()
    if firebase.child('out').get() is None:
        firebase.update({'out': 0})
    else:
        isCamsOpen.p_out = firebase.child('out').get()
    if firebase.child('time_end').get() is None:
        firebase.update({'time_end': str(datetime.now().strftime("%H:%M:%S"))})
    if firebase.child('time_start').get() is None:
        firebase.update({'time_start': str(datetime.now().strftime("%H:%M:%S"))})

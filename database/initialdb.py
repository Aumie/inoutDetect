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
    if firebase.child('in0').get() is None:
        firebase.update({'in0': 0})
    else:
        isCamsOpen.p_in = firebase.child('in0').get()
    if firebase.child('out0').get() is None:
        firebase.update({'out0': 0})
    else:
        isCamsOpen.p_out = firebase.child('out').get()
    if firebase.child('time_end').get() is None:
        firebase.update({'time_end': str(datetime.now().strftime("%H:%M:%S"))})
    if firebase.child('time_start').get() is None:
        firebase.update({'time_start': str(datetime.now().strftime("%H:%M:%S"))})
    # cam1 initialize data
    if firebase.child('in1').get() is None:
        firebase.update({'in1': 0})
    else:
        isCamsOpen.p_in1 = firebase.child('in1').get()
    if firebase.child('out1').get() is None:
        firebase.update({'out1': 0})
    else:
        isCamsOpen.p_out1 = firebase.child('out1').get()
    # cam2 initialize data
    if firebase.child('in2').get() is None:
        firebase.update({'in2': 0})
    else:
        isCamsOpen.p_in2 = firebase.child('in2').get()
    if firebase.child('out2').get() is None:
        firebase.update({'out2': 0})
    else:
        isCamsOpen.p_out2 = firebase.child('out2').get()
    # cam3 initialize data
    if firebase.child('in3').get() is None:
        firebase.update({'in3': 0})
    else:
        isCamsOpen.p_in3 = firebase.child('in3').get()
    if firebase.child('out3').get() is None:
        firebase.update({'out3': 0})
    else:
        isCamsOpen.p_out3 = firebase.child('out3').get()


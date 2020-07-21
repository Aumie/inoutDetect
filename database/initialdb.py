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
    global ref, month, day, year
    # delete data of 1 year before today 1 day 1 month
    oldday = str(int(day) - 1)
    oldmonth = str(int(month) - 1)
    oldyear = str(int(year) - 1)
    oldday = '0' + oldday if len(oldday) == 1 else oldday
    oldmonth = '0' + oldmonth if len(oldmonth) == 1 else oldmonth

    ref.child(oldyear).child(oldmonth).child(oldday).delete()

    data_today()
    return ref


def data_today():
    global ref
    global firebase
    # cam0 initialize data --------------------------------------------------------------
    if firebase.child('in0').get() is None:
        firebase.update({'in0': 0})
    else:
        if isCamsOpen.camdirect == 'lr':
            isCamsOpen.p_in = firebase.child('in0').get()
        else:
            isCamsOpen.p_in = firebase.child('out0').get()

    if firebase.child('out0').get() is None:
        firebase.update({'out0': 0})
    else:
        if isCamsOpen.camdirect == 'lr':
            isCamsOpen.p_out = firebase.child('out0').get()
        else:
            isCamsOpen.p_out = firebase.child('in0').get()
    # ----------------------------------------------------------------------------------
    if firebase.child('time_end').get() is None:
        firebase.update({'time_end': str(datetime.now().strftime("%H:%M:%S"))})
    if firebase.child('time_start').get() is None:
        firebase.update({'time_start': str(datetime.now().strftime("%H:%M:%S"))})

    # cam1 initialize data ---------------------------------------------------------------
    if firebase.child('in1').get() is None:
        firebase.update({'in1': 0})
    else:
        if isCamsOpen.camdirect1 == 'lr':
            isCamsOpen.p_in1 = firebase.child('in1').get()
        else:
            isCamsOpen.p_in1 = firebase.child('out1').get()

    if firebase.child('out1').get() is None:
        firebase.update({'out1': 0})
    else:
        if isCamsOpen.camdirect1 == 'lr':
            isCamsOpen.p_out1 = firebase.child('out1').get()
        else:
            isCamsOpen.p_out1 = firebase.child('in1').get()

    # ----------------------------------------------------------------------------------

    # cam2 initialize data ---------------------------------------------------------------
    if firebase.child('in2').get() is None:
        firebase.update({'in2': 0})
    else:
        if isCamsOpen.camdirect2 == 'lr':
            isCamsOpen.p_in2 = firebase.child('in2').get()
        else:
            isCamsOpen.p_in2 = firebase.child('out2').get()

    if firebase.child('out2').get() is None:
        firebase.update({'out2': 0})
    else:
        if isCamsOpen.camdirect2 == 'lr':
            isCamsOpen.p_out2 = firebase.child('out2').get()
        else:
            isCamsOpen.p_out2 = firebase.child('in2').get()

    # ----------------------------------------------------------------------------------

    # cam3 initialize data --------------------------------------------------------------
    if firebase.child('in3').get() is None:
        firebase.update({'in3': 0})
    else:
        if isCamsOpen.camdirect3 == 'lr':
            isCamsOpen.p_in3 = firebase.child('in3').get()
        else:
            isCamsOpen.p_in3 = firebase.child('out3').get()

    if firebase.child('out3').get() is None:
        firebase.update({'out3': 0})
    else:
        if isCamsOpen.camdirect3 == 'lr':
            isCamsOpen.p_out3 = firebase.child('out3').get()
        else:
            isCamsOpen.p_out3 = firebase.child('in3').get()

    # ----------------------------------------------------------------------------------



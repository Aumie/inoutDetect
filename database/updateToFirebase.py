import threading
from datetime import datetime
from process import isCamsOpen
from database import initialdb


# update to firebase every second
def loop_update_firebase():
    threading.Timer(1.0, loop_update_firebase).start()
    update_data()


def update_data():
    if isCamsOpen.iscamopen:
        initialdb.firebase.update({'in0': isCamsOpen.p_in})
        initialdb.firebase.update({'out0': isCamsOpen.p_out})
    elif isCamsOpen.iscam1open:
        initialdb.firebase.update({'in1': isCamsOpen.p_in1})
        initialdb.firebase.update({'out1': isCamsOpen.p_out1})
    elif isCamsOpen.iscam2open:
        initialdb.firebase.update({'in2': isCamsOpen.p_in2})
        initialdb.firebase.update({'out2': isCamsOpen.p_out2})
    elif isCamsOpen.iscam3open:
        initialdb.firebase.update({'in3': isCamsOpen.p_in3})
        initialdb.firebase.update({'out3': isCamsOpen.p_out3})
    initialdb.firebase.update({'time_end': str(datetime.now().strftime("%H:%M:%S"))})

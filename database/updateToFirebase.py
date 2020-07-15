import threading
from datetime import datetime
from process import isCamsOpen
from database import initialdb


# update to firebase every second
def loop_update_firebase():
    threading.Timer(1.0, loop_update_firebase).start()
    update_data()


def update_data():
    initialdb.firebase.update({'in': isCamsOpen.p_in})
    initialdb.firebase.update({'out': isCamsOpen.p_out})
    initialdb.firebase.update({'time_end': str(datetime.now().strftime("%H:%M:%S"))})

import threading
import time
from datetime import datetime
from process import isCamsOpen
from database import initialdb


# update to firebase every second
class Database(threading.Thread):
    isDataupdate = True

    def run(self) -> None:
        while self.isDataupdate:
            update_data()
            time.sleep(1)


def update_data():
    if isCamsOpen.iscamopen:
        if isCamsOpen.camdirect == 'lr':
            initialdb.firebase.update({'in0': isCamsOpen.p_in})
            initialdb.firebase.update({'out0': isCamsOpen.p_out})
        else:
            initialdb.firebase.update({'in0': isCamsOpen.p_out})
            initialdb.firebase.update({'out0': isCamsOpen.p_in})
    elif isCamsOpen.iscam1open:
        if isCamsOpen.camdirect1 == 'lr':
            initialdb.firebase.update({'in1': isCamsOpen.p_in1})
            initialdb.firebase.update({'out1': isCamsOpen.p_out1})
        else:
            initialdb.firebase.update({'in1': isCamsOpen.p_out1})
            initialdb.firebase.update({'out1': isCamsOpen.p_in1})
    elif isCamsOpen.iscam2open:
        if isCamsOpen.camdirect2 == 'lr':
            initialdb.firebase.update({'in2': isCamsOpen.p_in2})
            initialdb.firebase.update({'out2': isCamsOpen.p_out2})
        else:
            initialdb.firebase.update({'in2': isCamsOpen.p_out2})
            initialdb.firebase.update({'out2': isCamsOpen.p_in2})
    elif isCamsOpen.iscam3open:
        if isCamsOpen.camdirect3 == 'lr':
            initialdb.firebase.update({'in3': isCamsOpen.p_in3})
            initialdb.firebase.update({'out3': isCamsOpen.p_out3})
        else:
            initialdb.firebase.update({'in3': isCamsOpen.p_out3})
            initialdb.firebase.update({'out3': isCamsOpen.p_in3})
    initialdb.firebase.update({'time_end': str(datetime.now().strftime("%H:%M:%S"))})

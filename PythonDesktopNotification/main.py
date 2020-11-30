import time
from win10toast import ToastNotifier
while True:
    toaster = ToastNotifier()
    toaster.show_toast('Python', 'Nutan Drink Water!', duration=5)
    time.sleep(6)

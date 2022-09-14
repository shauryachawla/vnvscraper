from plyer import notification

def notifyNewBalance():
    notification.notify(
        title = "New Balance Kicks are in finally!",
        message = "Check if they're black tho",
        timeout  = 50
    )

def sendNotif():
    notification.notify(
        title = "New Kicks Available!",
        message = "Head over to VNV right now!!",
        timeout  = 50
    )
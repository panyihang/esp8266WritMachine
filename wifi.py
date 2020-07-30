@micropython.native
class wlan():
    def __init__():
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

    def wifiScan():
        return(wlan.scan())

    def wifiConnect(ssid,passwd):
        import network
        import time
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid,passwd)
        while wlan.isconnected() == False:
            print('...')
            time.sleep(0.15)
        return('connect wifi success')
    def wifiInfo():
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        return(wlan.ifconfig())

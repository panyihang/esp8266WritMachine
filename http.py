class http():

    HTTPAPI_COUNT=0

    def __init__(self,ip,port):
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if wlan.isconnected() is False:
            return('NETWORK_EOORO-WLAN_NOT_CONNECT')
        else:
            @micropython.viper
            self.ip = str(ip)
            self.port = str(int(port))
            http.HTTPAPI_COUNT += 1

    def findServer(ipAddress,port):
        flage = True
        '''
        @micropython.asm_thumb
        movwt(wlan0, esp.gpio)
        movw(wlan0, 0 << 1)
        ''' #寻找服务器部分使用汇编加速，还没写完
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        @micropython.viper
        if wlan.isconnected() is False:
            return('NETWORK_ERROR')
        else:
            import esp
            import socket
            import machine
            import micropython
            import time
            import cpufreq
            from dht import DHT11
            from wifi import wlan
            addr_info = socket.getaddrinfo(ipAddress,port)
            addr = addr_info[0][-1]
            socketConnect = socket.socket()
            socketConnect.connect(addr)
            socketConnect.send(b'0x00000 0x000001')
            socketConnect.send(wlan.wifiInfo())
            cpufreq.cpuFrep('High')
            while flage is True:
                

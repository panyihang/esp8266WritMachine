import cpufreq
from wifi import wlan
import dht
ssid = 'wifi的ssid'
passwd = 'ssid对应的密码'
wlan.wifiConnect(ssid,passwd)
cpufreq.cpufreq(1)

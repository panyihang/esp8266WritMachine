//py写的读取dht爆内存了
//考虑到esp8266的ram和flash大小，打算整个项目用cpp重写

#ifndef dht11_h
#define dht11_h

#include <Arduino.h>

#define DHTLIB_OK				0
#define DHTLIB_ERROR_CHECKSUM	-1
#define DHTLIB_ERROR_TIMEOUT	-2

class dht11
{
public:
    int read(int pin);
	int humidity;
	int temperature;
};

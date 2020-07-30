#include "dht11.h"

int dht11::read(int pin)
{
    uint8_t bits[5];
	uint8_t cnt = 7;
	uint8_t idx = 0;
    
    for (int i=0; i< 5; i++) bits[i] = 0;
    
    pinMode(pin, OUTPUT);
	digitalWrite(pin, LOW);
	delay(20);
	digitalWrite(pin, HIGH);
    
    
}

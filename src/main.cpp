#include <Arduino.h>

//LED1=K3, LED2 = K4, LED3=K5, LED4=K6.
#define LED PK_3

void setup() {
    // pinMode() doesn't work because "PK3" is not defined by default
    pin_function(LED, STM_PIN_DATA(STM_MODE_OUTPUT_PP, GPIO_NOPULL, 0));
}

void loop() {
    digitalWriteFast(LED, HIGH);
    delay(1000);
    digitalWriteFast(LED, LOW);
    delay(1000);
}

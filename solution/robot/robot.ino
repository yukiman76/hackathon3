#include <MeMCore.h>
#include <Arduino.h>

MeDCMotor motor1(M1);
MeDCMotor motor2(M2);

MePort port(PORT_4);
Servo arm;
int16_t s1 =  port.pin1();

uint8_t motorSpeed = 100; //might have to chagen this

void setup() {
  Serial.begin(115200);
  arm.attach(s1);
}

void stop_motors() {
    motor1.stop();
    motor2.stop();
}

void loop() {
  if(Serial.available()) {
    String incomingString = Serial.readStringUntil('\n');

    String action = String(incomingString.substring(0, 1));
    int distance = 0;

    if ( incomingString.length() > 1 )
    {//we have an action distance amount
      distance = incomingString.substring(1, incomingString.length()).toInt();
    }

    if (action == String('f') ) {
      Serial.println("ack: action_fwd(" + String(action) + ") distance: (" + String(distance) + ")");
      motor1.run(-motorSpeed);
      motor2.run(motorSpeed);
      delay(distance);
      stop_motors();
    }
    else if (action == String('b') ) {
      Serial.println("ack: action_bkw(" + String(action) + ") distance: (" + String(distance) + ")");
      motor1.run(motorSpeed);
      motor2.run(-motorSpeed);
      delay(distance);
      stop_motors();
    }
    else if (action == String('s') ) {
      Serial.println("ack: action_stp(" + String(action) + ") distance: (" + String(distance) + ")");
      stop_motors();
    }
    else if (action == String('a') ) {
      Serial.println("ack: action_arm(" + String(action) + ") distance: (" + String(distance) + ")");
      arm.write(distance);
    }
    else {
      Serial.println("ack: action_inv(" + String(action) + ")distance: (" + String(distance) + ")");
    }

  }
}

#include <Servo.h>
  Servo servoLeft;
  Servo servoRight;
//
//int turn_right = 0;
//int turn_left = 0;
//int counter = (turn_right + turn_left);
//int timer = 0;
  
void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(12);
  servoRight.attach(13);
  pinMode(7, INPUT);             
  pinMode(5, INPUT);

}
//
//int stuck() {
//  if ((turn_right > 0) and (turn_left > 0) and (counter == 5) and (timer < 500)) {
//   timer = 0;
////   if (turn_right > turn_left) {
//    servoRight.writeMicroseconds(1700);
//    servoLeft.writeMicroseconds(1300);
//    delay(300);
//    servoRight.writeMicroseconds(2000);
//    servoLeft.writeMicroseconds(2000);
//    delay(100);
//    turn_right = 0;
//    turn_left = 0;
////   }
////   else if (turn_left > turn_right) {
////    servoRight.writeMicroseconds(1700);
////    servoLeft.writeMicroseconds(1300);
////    delay(300);
////    servoRight.writeMicroseconds(1000);
////    servoLeft.writeMicroseconds(1000);
////    delay(200);  
////    turn_right = 0;
////    turn_left = 0;  
////   }
//  }
//}

void loop() {
  while (digitalRead(5) == HIGH and digitalRead(7) == HIGH) {
   servoRight.writeMicroseconds(1300);
   servoLeft.writeMicroseconds(1700);
//   timer += 1;
//   if (timer > 500) {
//     turn_right = 0;
//     turn_left = 0; 
//     timer = 0;
//   }
   
  }

  if (digitalRead(5) == LOW and digitalRead(7) == HIGH) {
//   turn_right += 1;
   servoRight.writeMicroseconds(1700);
   servoLeft.writeMicroseconds(1300);
   delay(300);
   servoRight.writeMicroseconds(2000);
   servoLeft.writeMicroseconds(2000);
   delay(350);
//   timer = 0;
//   
//   servoLeft.writeMicroseconds(1500);
//   servoRight.writeMicroseconds(1700);
   
  }
 

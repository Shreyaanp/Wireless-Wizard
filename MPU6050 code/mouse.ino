#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>

MPU6050 mpu;

int16_t ax, ay, az, gx, gy, gz;
void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  if(!mpu.testConnection()){
    while (1);
    }
}
void loop() {
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  Serial.print("ax = ");
  Serial.print(ax);
  Serial.print(" | ay = ");
  Serial.print(ay);
  Serial.print(" | az = ");
  Serial.print(az);
  Serial.print("\n");
  Serial.print("\n");
  Serial.print("gx = ");
  Serial.print(gx);
  Serial.print(" | gy = ");
  Serial.print(gy);
  Serial.print(" | gz = ");
  Serial.print(gz);
  Serial.print("\n");
  delay(500);
}

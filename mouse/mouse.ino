#include <MPU6050_tockn.h>
#include <Wire.h>

#define LeftB     5
#define RightB    2
#define MouseB    6

MPU6050 mpu6050(Wire); 

int X,Y,Z;               // Data Variables for mouse co-ordinates
int xinit=0;
int yinit = 0;
int Z_gyroX,Z_gyroY,Z_gyroZ;     
int lastState = LOW;      // the previous state from the input pin
int currentState;// Angle Variables for calucating gyroscope zero error
const int SENSOR_PIN = 3;

void setup() {

  Serial.begin(9600);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  mpu6050.update();
  Z_gyroX = mpu6050.getAngleX();
  Z_gyroY = mpu6050.getAngleY();
  Z_gyroZ = mpu6050.getAngleZ();



  pinMode(LeftB,INPUT);
  pinMode(RightB,INPUT);
  pinMode(MouseB,INPUT);
  pinMode(SENSOR_PIN, INPUT);
  digitalWrite(RightB, LOW);
  digitalWrite(LeftB, LOW);

  if(Z_gyroX < 0){                                                 // Inverting the sign of all the three offset values for zero error correction
    Z_gyroX = Z_gyroX *(-1);}
  else{
    Z_gyroX = (Z_gyroX-Z_gyroX)-Z_gyroX;}

  if(Z_gyroY < 0){
    Z_gyroY = (Z_gyroY *(-1));}
  else{
    Z_gyroY = ((Z_gyroY-Z_gyroY)-Z_gyroY)+8;}

  if(Z_gyroZ < 0){
    Z_gyroZ = Z_gyroZ *(-1);}
  else{
    Z_gyroZ = (Z_gyroZ-Z_gyroZ)-Z_gyroZ;}
}

void loop() {
  mpu6050.update();
  X = Z_gyroX + mpu6050.getAngleX();                                     // Getting current angle for X Y Z and correcting the zero error
  Y = Z_gyroY + mpu6050.getAngleY();
  Z = Z_gyroZ + mpu6050.getAngleZ();
  digitalWrite(MouseB,HIGH);
  currentState = digitalRead(SENSOR_PIN);
  if(digitalRead(MouseB) == HIGH ){
    delay(5);  // Mouse movement resolution delay
    if(X==xinit && Y==yinit){
      Serial.println("DATAL,"+String(0)+','+String(0)+','+String(0));
    }
    else{
      Serial.println("DATAL,"+String(X)+','+String(Y)+','+String(Z));
    }
     // Sends corrected gyro data to the Serial Port with the identifier "DATAL"
  }
  xinit= X;
  yinit = Y;
  if(lastState == LOW && currentState == HIGH){
    Serial.println("The sensor is touched");
    
  }
  else{
    if(digitalRead(LeftB) == HIGH){
      Serial.println("DATAB,L");
      digitalWrite(LeftB, LOW);
   }
   if(digitalRead(RightB) == HIGH){                                                  // Debounce delay
    Serial.println("DATAB,R");
    digitalWrite(LeftB, LOW);// Sends "L" stating the left button is pressed with the identifier "DATAB"
  }
  }
  
}

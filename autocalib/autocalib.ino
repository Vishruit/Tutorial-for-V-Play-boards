#include <RFduinoBLE.h>
#include <EEPROM.h>

int addr1=0;//stores the left side calibration value
int addr2=1;//stores the right side calibration value

int cmp_l,cmp_r; //comparison values for left and right
int mode; //mode=1 when calibration mode,mode=2 otherwise

void setup() {
  // Input pins
  // Left =2
  // Right =3
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  
  // this is the data we want to appear in the advertisement
  // (if the deviceName and advertisementData are too long to fix into the 31 byte
  // ble advertisement packet, then the advertisementData is truncated first down to
  // a single byte, then it will truncate the deviceName)
  RFduinoBLE.advertisementData = "assistive_board";
  
  // start the BLE stack
  RFduinoBLE.begin();
//  Serial.begin(9600);
}
void loop() { 
  int l_val = analogRead(3);
  int r_val = analogRead(2);
  Serial.println(String(l_val) + " " + String(r_val));
  if(mode==1)  //auto calibration mode
  {
  EEPROM.write(addr1,l_val);
  EEPROM.write(addr2,r_val);
  }
  if(mode==2)
  {
   cmp_l=EEPROM.read(addr1);
   cmp_r=EEPROM.read(addr2);
   
   /*the regular rfduino code, substitute the current comparison values with above*/
  }
 
  delay(50);
}


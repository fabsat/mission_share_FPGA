void setup () {
  Serial.begin (115200);
}

void loop () {
  if (Serial.available () > 0) {
    int value1 = Serial.read ();
    int value2 = Serial.read ();
    
    Serial.print ("a and b : ");
    Serial.println (value1 & value2);
    Serial.print ("a or b : ");
    Serial.println (value1 | value2);
    Serial.print ("a xor b : ");
    Serial.println (value1 ^ value2);
  }
  delay (100);
}

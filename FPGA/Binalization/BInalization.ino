void setup () {
  Serial.begin (115200);
}

void loop () {
  if (Serial.available () > 0) {
    char results [] = {0, 1};
    
    int value = Serial.read ();
    if (value >= 32) {
      Serial.print (results [1]);
    } else {
      Serial.print (results [0]);
    }
  }
}

int reading;
double tempC;
double tempF;

void setup() {

//Serial.begin(9600);
  // variable name max length is 12 characters long
  Particle.variable("analogvalue", reading);
  Particle.variable("tempC", tempC);
  Particle.variable("tempF", tempF);
  
  pinMode(A7, INPUT);
}

void loop() {

  // Read the analog value of the sensor (TMP36)
  reading = analogRead(A7);                         // I used analog Pin 7, labeled WKP
  tempC = (((reading * 3.3)/4095) - 0.5) * 100;     // Convert the reading into degree celcius
  tempF = ((tempC * 1.8) +32);                      // Convert from C to F

//Serial.print(reading); Serial.println(" reading");
//Serial.print(tempC); Serial.println(" degrees C");
//Serial.print(tempF); Serial.println(" degrees F");
 
 delay(5000); //waiting 5 second

}
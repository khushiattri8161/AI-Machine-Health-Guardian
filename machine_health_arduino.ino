#include <Servo.h>
#include <DHT.h>

#define DHT_PIN 2
#define DHT_TYPE DHT11

#define VIBRATION_PIN 3
#define ACS_PIN A0

#define GREEN_LED 5
#define YELLOW_LED 6
#define RED_LED 7
#define BUZZER 8

#define SERVO_PIN 9

DHT dht(DHT_PIN, DHT_TYPE);
Servo machineServo;

const float ACS_SENSITIVITY = 0.066;
const float ACS_ZERO = 2.530;

unsigned long vibrationCount = 0;
int lastVibrationState = LOW;

void setup() {

  Serial.begin(9600);

  dht.begin();
  machineServo.attach(SERVO_PIN);

  pinMode(VIBRATION_PIN, INPUT);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(YELLOW_LED, LOW);
  digitalWrite(RED_LED, LOW);
  noTone(BUZZER);

  machineServo.write(90);

  delay(2000);
}

void loop() {

  vibrationCount = 0;

  // =========================
  // SERVO / MACHINE CYCLE
  // =========================

  machineServo.write(20);
  monitorVibration(700);

  machineServo.write(70);
  monitorVibration(700);

  machineServo.write(120);
  monitorVibration(700);

  machineServo.write(160);
  monitorVibration(700);

  machineServo.write(90);
  monitorVibration(700);


  // =========================
  // DHT11
  // =========================

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    temperature = 0;
    humidity = 0;
  }


  // =========================
  // ACS712
  // =========================

  long total = 0;

  for (int i = 0; i < 100; i++) {
    total += analogRead(ACS_PIN);
    delayMicroseconds(500);
  }

  float averageADC = total / 100.0;

  float voltage =
      averageADC * 5.0 / 1023.0;

  float current =
      abs((voltage - ACS_ZERO) / ACS_SENSITIVITY);


  // =========================
  // HEALTH SCORE
  // =========================

  int healthScore = 100;

  if (temperature >= 45) {
    healthScore -= 40;
  }
  else if (temperature >= 35) {
    healthScore -= 20;
  }

  if (vibrationCount >= 20) {
    healthScore -= 40;
  }
  else if (vibrationCount >= 8) {
    healthScore -= 20;
  }

  if (current >= 0.50) {
    healthScore -= 20;
  }
  else if (current >= 0.25) {
    healthScore -= 10;
  }

  if (healthScore < 0) {
    healthScore = 0;
  }


  // =========================
  // LED + BUZZER
  // =========================

  if (healthScore >= 75) {

    // HEALTHY
    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(RED_LED, LOW);

    noTone(BUZZER);
  }

  else if (healthScore >= 45) {

    // WARNING
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(YELLOW_LED, HIGH);
    digitalWrite(RED_LED, LOW);

    tone(BUZZER, 1000, 200);
  }

  else {

    // CRITICAL
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(RED_LED, HIGH);

    tone(BUZZER, 1500, 500);
  }


  // =========================
  // PYTHON DATA
  // =========================

  Serial.print(temperature);
  Serial.print(",");

  Serial.print(humidity);
  Serial.print(",");

  Serial.print(vibrationCount);
  Serial.print(",");

  Serial.print(current, 3);
  Serial.print(",");

  Serial.println(healthScore);

}


// ======================================
// VIBRATION MONITOR
// ======================================

void monitorVibration(unsigned long duration) {

  unsigned long startTime = millis();

  while (millis() - startTime < duration) {

    int vibrationState =
        digitalRead(VIBRATION_PIN);

    if (vibrationState == HIGH &&
        lastVibrationState == LOW) {

      vibrationCount++;
    }

    lastVibrationState = vibrationState;

    delay(20);
  }
}
# 🔌 Wiring Documentation

## AI-Powered Smart Machine Health Guardian

This document describes the hardware connections used in the AI-Powered Smart Machine Health Guardian prototype.

---

## 1. Arduino UNO Pin Configuration

| Component | Connection | Arduino UNO Pin |
|---|---|---|
| DHT11 | DATA | D2 |
| SW-420 | DO | D3 |
| ACS712 30A | OUT | A0 |
| Green LED | Anode | D5 |
| Yellow LED | Anode | D6 |
| Red LED | Anode | D7 |
| Buzzer | Positive | D8 |
| SG90 Servo | Signal | D9 |

---

## 2. DHT11 Temperature and Humidity Sensor

The DHT11 sensor is used to measure temperature and humidity.

### Connections

| DHT11 Pin | Arduino UNO |
|---|---|
| VCC | 5V |
| GND | GND |
| DATA | D2 |

### Wiring

```text
DHT11 VCC   → Arduino 5V
DHT11 GND   → Arduino GND
DHT11 DATA  → Arduino D2
```

---

## 3. SW-420 Vibration Sensor

The SW-420 vibration sensor is used to detect mechanical vibration.

The **digital output (DO)** is used in the current prototype.

### Connections

| SW-420 Pin | Arduino UNO |
|---|---|
| VCC | 5V |
| GND | GND |
| DO | D3 |

### Wiring

```text
SW-420 VCC  → Arduino 5V
SW-420 GND  → Arduino GND
SW-420 DO   → Arduino D3
```

### Sensor Placement

The vibration sensor should be firmly attached to the machine or actuator mounting structure so that mechanical vibrations are transferred effectively to the sensor.

---

## 4. ACS712 30A Current Sensor

The ACS712 current sensor is used to monitor the electrical current of the monitored load.

### Arduino-side Connections

| ACS712 Pin | Arduino UNO |
|---|---|
| VCC | 5V |
| GND | GND |
| OUT | A0 |

### Wiring

```text
ACS712 VCC  → Arduino 5V
ACS712 GND  → Arduino GND
ACS712 OUT  → Arduino A0
```

The current-carrying terminals of the ACS712 must be connected in series with the monitored load according to the intended electrical configuration.

> **Safety:** Do not exceed the rated current of the ACS712 module. For mains-voltage applications, use proper electrical isolation and qualified supervision.

---

## 5. Green LED — Healthy Status

The green LED indicates that the machine is operating in the healthy range.

### Wiring

```text
Arduino D5
    ↓
Current-limiting resistor
    ↓
Green LED
    ↓
GND
```

---

## 6. Yellow LED — Warning Status

The yellow LED indicates that the machine health has entered the warning range.

### Wiring

```text
Arduino D6
    ↓
Current-limiting resistor
    ↓
Yellow LED
    ↓
GND
```

---

## 7. Red LED — Critical Status

The red LED indicates a critical machine-health condition.

### Wiring

```text
Arduino D7
    ↓
Current-limiting resistor
    ↓
Red LED
    ↓
GND
```

Each LED must use an appropriate current-limiting resistor.

---

## 8. Buzzer

The buzzer provides an audible alert when a warning or critical condition is detected.

### Wiring

```text
Arduino D8  → Buzzer +
Arduino GND → Buzzer -
```

---

## 9. SG90 Servo Motor

The SG90 servo is used as the mechanical actuator in the prototype.

### Connections

| SG90 Wire/Pin | Connection |
|---|---|
| Signal | Arduino D9 |
| VCC | 5V supply |
| GND | GND |

### Wiring

```text
SG90 Signal → Arduino D9
SG90 VCC    → 5V supply
SG90 GND    → GND
```

For stable servo operation, an external suitable 5V supply may be used.

If an external power supply is used, its ground must be connected to Arduino GND.

```text
External Power Supply GND
          │
          ├── Servo GND
          │
          └── Arduino GND
```

---

## 10. Complete Pin Summary

```text
DHT11 DATA       → D2
SW-420 DO        → D3
ACS712 OUT       → A0
Green LED        → D5
Yellow LED       → D6
Red LED          → D7
Buzzer           → D8
SG90 Servo       → D9
```

---

## 11. Complete System Connection

```text
                         ARDUINO UNO
                    ┌─────────────────┐
                    │                 │
DHT11 DATA ─────────┤ D2              │
SW-420 DO ──────────┤ D3              │
ACS712 OUT ─────────┤ A0              │
Green LED ──────────┤ D5              │
Yellow LED ─────────┤ D6              │
Red LED ────────────┤ D7              │
Buzzer ─────────────┤ D8              │
Servo Signal ───────┤ D9              │
                    │                 │
                    │ 5V / GND        │
                    └─────────────────┘
```

---

## 12. Power and Safety Notes

- Verify VCC and GND connections before powering the circuit.
- Use a suitable current-limiting resistor for every LED.
- Avoid drawing excessive servo current from the Arduino 5V rail.
- When using an external servo supply, connect its GND to Arduino GND.
- Do not exceed the rated current of the ACS712 module.
- Do not intentionally overload, short-circuit, or mechanically damage the prototype during testing.
- For mains-voltage current measurements, proper isolation and electrical safety procedures are required.

---

## 13. Hardware Summary

The prototype combines:

- Arduino UNO for control and processing
- DHT11 for temperature and humidity
- SW-420 for vibration detection
- ACS712 30A for current monitoring
- SG90 servo as the mechanical actuator
- LEDs for machine-health indication
- Buzzer for audible alerts

These components together form the hardware layer of the Smart Machine Health Guardian.

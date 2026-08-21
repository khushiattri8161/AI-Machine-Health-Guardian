# 🏗️ System Architecture

## AI-Powered Smart Machine Health Guardian

The AI-Powered Smart Machine Health Guardian is a multi-sensor machine-condition monitoring prototype.

The system collects machine-related parameters, processes them using an Arduino UNO, provides local alerts, and displays the information through a Python Tkinter dashboard.

---

# 1. Overall System Architecture

```text
                    MACHINE / ACTUATOR
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
           DHT11         SW-420       ACS712
        Temperature     Vibration     Current
        & Humidity
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                     Arduino UNO
                           │
                           ▼
                  Sensor Processing
                           │
                           ▼
                  Health Score Logic
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
           🟢 GREEN      🟡 YELLOW     🔴 RED
           HEALTHY       WARNING       CRITICAL
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                         Buzzer
                           │
                           ▼
                      USB Serial
                           │
                           ▼
                  Python Tkinter GUI
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
          Live Dashboard       CSV Data Logging
                                     │
                                     ▼
                              Future ML Dataset
```

---

# 2. Main System Modules

The complete system consists of the following modules:

1. Sensor Module
2. Arduino Processing Module
3. Health Evaluation Module
4. Alert Module
5. Serial Communication Module
6. Python Dashboard Module
7. Data Logging Module
8. Future AI/ML Module

---

# 3. Sensor Module

The sensor module collects information related to machine operating conditions.

### DHT11

Measures:

- Temperature
- Humidity

### SW-420

Detects:

- Mechanical vibration events

The digital output (DO) is used in the current prototype.

### ACS712

Measures:

- Electrical current associated with the monitored load

---

# 4. Arduino Processing Module

The Arduino UNO acts as the main controller.

Its responsibilities include:

- Reading sensor values
- Processing sensor information
- Calculating the machine health score
- Controlling LEDs
- Controlling the buzzer
- Controlling the servo
- Sending data to the Python application

---

# 5. Machine Health Evaluation

The current prototype uses a rule-based health scoring system.

The health score is divided into three operating states.

| Health Score | Machine Status | Indicator |
|---|---|---|
| 75–100% | Healthy | Green LED |
| 45–74% | Warning | Yellow LED |
| 0–44% | Critical | Red LED |

These thresholds are prototype-level values and can be calibrated according to the characteristics of a particular machine.

---

# 6. Local Alert System

The Arduino provides immediate visual and audible feedback.

```text
              MACHINE HEALTH
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
    HEALTHY       WARNING      CRITICAL
       │            │            │
       ▼            ▼            ▼
   🟢 GREEN      🟡 YELLOW     🔴 RED
                    │            │
                    └─────┬──────┘
                          ▼
                       BUZZER
```

### Healthy

Green LED indicates normal operation.

### Warning

Yellow LED indicates that the monitored condition requires attention.

### Critical

Red LED and buzzer indicate a critical condition.

---

# 7. Serial Communication

The Arduino communicates with the Python application through USB serial communication.

Current configuration:

```text
Communication: USB Serial
Baud Rate: 9600
```

The Arduino sends sensor information to the Python application.

The Python application then processes and displays the received information.

---

# 8. Python Tkinter Dashboard

The Python application provides a graphical user interface.

The dashboard displays:

- Machine health score
- Temperature
- Humidity
- Vibration
- Current
- Machine status
- Arduino connection status
- Live health graph

The dashboard is implemented using Python's Tkinter GUI framework.

PySerial is used for communication between Python and Arduino.

---

# 9. Data Logging

The Python dashboard automatically stores received sensor readings in CSV format.

The dataset contains fields such as:

```text
timestamp
temperature
humidity
vibration
current
health
```

Example:

```csv
timestamp,temperature,humidity,vibration,current,health
2026-08-21 14:20:01,31.0,54.0,2,0.041,100
2026-08-21 14:20:05,31.1,54.0,3,0.052,100
2026-08-21 14:20:09,31.2,53.0,5,0.061,90
```

The collected data can be used for future analysis and machine-learning development.

---

# 10. Complete Data Flow

```text
Machine / Actuator
       │
       ▼
    Sensors
       │
       ▼
 Arduino UNO
       │
       ├──────────────► LEDs
       │
       ├──────────────► Buzzer
       │
       ▼
 Health Score
       │
       ▼
 USB Serial
       │
       ▼
 Python
       │
       ├──────────────► Tkinter Dashboard
       │
       └──────────────► CSV Dataset
```

---

# 11. Current System

The current implementation follows:

```text
Sensors
   ↓
Arduino UNO
   ↓
Sensor Processing
   ↓
Rule-Based Health Score
   ↓
LED + Buzzer Alerts
   ↓
USB Serial
   ↓
Python Tkinter Dashboard
   ↓
CSV Data Logging
```

---

# 12. Future AI/ML System

The future version can use the collected dataset to train a machine-learning model.

```text
Sensor Data
     ↓
Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Machine Learning Model
     ↓
Fault Classification
     ↓
Early Fault Prediction
     ↓
Predictive Maintenance
```

Possible future machine-learning algorithms include:

- Random Forest
- Decision Tree
- Support Vector Machine
- Neural Network
- Isolation Forest

---

# 13. AI Readiness

The current system is designed to provide the data required for future AI development.

The data collection process provides multiple features:

```text
Temperature
Humidity
Vibration
Current
Health Score
Timestamp
```

These parameters can later be analyzed to identify patterns associated with abnormal machine behaviour.

---

# 14. System Advantages

The architecture provides:

- Low-cost implementation
- Multiple sensor monitoring
- Real-time health indication
- Local alerts
- Computer-based visualization
- Automatic data logging
- Expandability toward machine learning
- Easy prototyping using Arduino UNO

---

# 15. Architecture Summary

The project follows the concept:

```text
SENSE
  ↓
PROCESS
  ↓
EVALUATE
  ↓
ALERT
  ↓
VISUALIZE
  ↓
LOG
  ↓
LEARN
```

The current prototype implements the first six stages and provides the data foundation for the future machine-learning stage.

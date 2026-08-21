# 🤖 AI-Powered Smart Machine Health Guardian

> A low-cost, multi-sensor machine health monitoring and condition-monitoring prototype using Arduino UNO and Python Tkinter.

---

## 📌 Overview

The **AI-Powered Smart Machine Health Guardian** is a low-cost machine health monitoring prototype designed to continuously monitor important operating parameters of a machine and identify abnormal operating conditions.

The system uses multiple sensors to monitor:

- 🌡️ Temperature
- 💧 Humidity
- 📳 Vibration
- ⚡ Electrical current

An **Arduino UNO** collects the sensor data and calculates a real-time machine health score.

The data is transmitted to a **Python Tkinter desktop dashboard**, where the machine condition can be monitored in real time. The sensor readings are also automatically stored in CSV format for further analysis and future machine-learning development.

The current prototype uses a **rule-based health scoring system**. The collected dataset provides the foundation for future machine-learning-based predictive maintenance.

---

# 🎯 Objectives

The main objectives of this project are:

1. Monitor multiple machine-health parameters simultaneously.
2. Detect abnormal machine operating conditions.
3. Generate a real-time machine health score.
4. Provide immediate visual and audible alerts.
5. Display machine condition through a desktop dashboard.
6. Store sensor data for historical analysis.
7. Provide a foundation for future AI/ML-based predictive maintenance.

---

# ⚙️ System Architecture

```text
                    MACHINE / ACTUATOR
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
           DHT11         SW-420       ACS712
        Temperature     Vibration     Current
              │            │            │
              └────────────┼────────────┘
                           ▼
                     Arduino UNO
                           │
                           ▼
                  Health Score Logic
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           🟢 GREEN      🟡 YELLOW     🔴 RED
           Healthy       Warning      Critical
                                        │
                                        ▼
                                      Buzzer
                                        │
                                        ▼
                                   USB Serial
                                        │
                                        ▼
                                Python Tkinter
                                        │
                          ┌─────────────┴─────────────┐
                          ▼                           ▼
                    Live Dashboard              CSV Logging
                          │
                          ▼
                  Future ML Development

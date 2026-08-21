import tkinter as tk
from tkinter import ttk
import serial
import csv
import time
from datetime import datetime
from collections import deque

# ============================================================
# SETTINGS
# ============================================================

PORT = "COM7"          # Change if your Arduino uses another port
BAUD_RATE = 9600

CSV_FILE = "machine_health_dataset.csv"

# Number of graph points
MAX_POINTS = 50


# ============================================================
# ARDUINO CONNECTION
# ============================================================

try:
    arduino = serial.Serial(
        PORT,
        BAUD_RATE,
        timeout=1
    )

    time.sleep(2)

    connected = True

except serial.SerialException:
    arduino = None
    connected = False


# ============================================================
# CSV FILE
# ============================================================

csv_file = open(
    CSV_FILE,
    "a",
    newline=""
)

csv_writer = csv.writer(csv_file)

# Write header if file is empty
if csv_file.tell() == 0:
    csv_writer.writerow([
        "timestamp",
        "temperature",
        "humidity",
        "vibration",
        "current",
        "health"
    ])


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("AI-Powered Smart Machine Health Guardian")

root.geometry("1100x700")

root.configure(
    bg="#101820"
)

root.resizable(True, True)


# ============================================================
# COLORS
# ============================================================

BG = "#101820"
CARD = "#182630"
TEXT = "#FFFFFF"
GREEN = "#00C853"
YELLOW = "#FFD600"
RED = "#FF1744"
BLUE = "#00B0FF"
GRAY = "#9E9E9E"


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="AI-POWERED SMART MACHINE HEALTH GUARDIAN",
    font=("Arial", 24, "bold"),
    fg=TEXT,
    bg=BG
)

title.pack(
    pady=20
)


subtitle = tk.Label(
    root,
    text="Real-Time Machine Condition Monitoring System",
    font=("Arial", 12),
    fg=GRAY,
    bg=BG
)

subtitle.pack(
    pady=(0, 15)
)


# ============================================================
# STATUS CARD
# ============================================================

status_frame = tk.Frame(
    root,
    bg=CARD,
    bd=0
)

status_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


status_title = tk.Label(
    status_frame,
    text="MACHINE HEALTH",
    font=("Arial", 14, "bold"),
    fg=GRAY,
    bg=CARD
)

status_title.pack(
    pady=(15, 0)
)


health_label = tk.Label(
    status_frame,
    text="-- %",
    font=("Arial", 42, "bold"),
    fg=GREEN,
    bg=CARD
)

health_label.pack()


status_label = tk.Label(
    status_frame,
    text="WAITING FOR DATA",
    font=("Arial", 18, "bold"),
    fg=GRAY,
    bg=CARD
)

status_label.pack(
    pady=(0, 15)
)


# ============================================================
# SENSOR CARDS
# ============================================================

sensor_frame = tk.Frame(
    root,
    bg=BG
)

sensor_frame.pack(
    fill="x",
    padx=20,
    pady=15
)


def create_sensor_card(parent, title_text, value_text):

    frame = tk.Frame(
        parent,
        bg=CARD,
        width=220,
        height=120
    )

    frame.pack(
        side="left",
        expand=True,
        fill="both",
        padx=8
    )

    frame.pack_propagate(False)

    title = tk.Label(
        frame,
        text=title_text,
        font=("Arial", 12, "bold"),
        fg=GRAY,
        bg=CARD
    )

    title.pack(
        pady=(15, 5)
    )

    value = tk.Label(
        frame,
        text=value_text,
        font=("Arial", 22, "bold"),
        fg=TEXT,
        bg=CARD
    )

    value.pack()

    return value


temperature_value = create_sensor_card(
    sensor_frame,
    "🌡 TEMPERATURE",
    "-- °C"
)

humidity_value = create_sensor_card(
    sensor_frame,
    "💧 HUMIDITY",
    "-- %"
)

vibration_value = create_sensor_card(
    sensor_frame,
    "📳 VIBRATION",
    "--"
)

current_value = create_sensor_card(
    sensor_frame,
    "⚡ CURRENT",
    "-- A"
)


# ============================================================
# CONNECTION STATUS
# ============================================================

connection_frame = tk.Frame(
    root,
    bg=BG
)

connection_frame.pack(
    pady=5
)


connection_label = tk.Label(
    connection_frame,
    text=(
        "● ARDUINO CONNECTED"
        if connected
        else "● ARDUINO DISCONNECTED"
    ),
    font=("Arial", 11, "bold"),
    fg=GREEN if connected else RED,
    bg=BG
)

connection_label.pack()


# ============================================================
# GRAPH CANVAS
# ============================================================

graph_frame = tk.Frame(
    root,
    bg=CARD
)

graph_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=15
)


graph_title = tk.Label(
    graph_frame,
    text="LIVE HEALTH MONITOR",
    font=("Arial", 13, "bold"),
    fg=TEXT,
    bg=CARD
)

graph_title.pack(
    pady=5
)


canvas = tk.Canvas(
    graph_frame,
    bg="#0D141A",
    highlightthickness=0
)

canvas.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ============================================================
# GRAPH DATA
# ============================================================

health_data = deque(
    maxlen=MAX_POINTS
)


# ============================================================
# DRAW GRAPH
# ============================================================

def draw_graph():

    canvas.delete("all")

    width = canvas.winfo_width()
    height = canvas.winfo_height()

    if width <= 1 or height <= 1:
        root.after(500, draw_graph)
        return

    # Grid

    for i in range(0, 101, 20):

        y = height - (
            i / 100 * (height - 30)
        ) - 15

        canvas.create_line(
            40,
            y,
            width - 10,
            y,
            fill="#26343D"
        )

        canvas.create_text(
            20,
            y,
            text=str(i),
            fill=GRAY,
            font=("Arial", 8)
        )

    # Graph line

    if len(health_data) >= 2:

        points = []

        graph_width = width - 60
        graph_height = height - 30

        for index, value in enumerate(health_data):

            x = 40 + (
                index /
                (MAX_POINTS - 1)
            ) * graph_width

            y = height - (
                value / 100 * graph_height
            ) - 15

            points.extend([x, y])

        canvas.create_line(
            *points,
            fill=BLUE,
            width=3,
            smooth=True
        )


# ============================================================
# UPDATE HEALTH DISPLAY
# ============================================================

def update_health(health):

    health_label.config(
        text=f"{health}%"
    )

    health_data.append(health)

    if health >= 75:

        health_label.config(
            fg=GREEN
        )

        status_label.config(
            text="🟢 MACHINE HEALTHY",
            fg=GREEN
        )

    elif health >= 45:

        health_label.config(
            fg=YELLOW
        )

        status_label.config(
            text="🟡 WARNING - CHECK MACHINE",
            fg=YELLOW
        )

    else:

        health_label.config(
            fg=RED
        )

        status_label.config(
            text="🔴 CRITICAL - FAULT DETECTED",
            fg=RED
        )


# ============================================================
# READ ARDUINO DATA
# ============================================================

def read_arduino():

    if arduino is None:

        connection_label.config(
            text="● ARDUINO DISCONNECTED",
            fg=RED
        )

        root.after(
            500,
            read_arduino
        )

        return


    try:

        if arduino.in_waiting:

            line = (
                arduino.readline()
                .decode(
                    "utf-8",
                    errors="ignore"
                )
                .strip()
            )

            data = line.split(",")

            # Arduino sends:
            # temperature,
            # humidity,
            # vibration,
            # current,
            # health

            if len(data) == 5:

                try:

                    temperature = float(data[0])
                    humidity = float(data[1])
                    vibration = int(data[2])
                    current = float(data[3])
                    health = int(data[4])

                except ValueError:

                    root.after(
                        100,
                        read_arduino
                    )

                    return


                # ============================
                # UPDATE GUI
                # ============================

                temperature_value.config(
                    text=f"{temperature:.1f} °C"
                )

                humidity_value.config(
                    text=f"{humidity:.1f} %"
                )

                vibration_value.config(
                    text=str(vibration)
                )

                current_value.config(
                    text=f"{current:.3f} A"
                )


                update_health(
                    health
                )


                # ============================
                # SAVE CSV
                # ============================

                timestamp = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                csv_writer.writerow([
                    timestamp,
                    temperature,
                    humidity,
                    vibration,
                    current,
                    health
                ])

                csv_file.flush()


                connection_label.config(
                    text="● ARDUINO CONNECTED",
                    fg=GREEN
                )


                draw_graph()


    except serial.SerialException:

        connection_label.config(
            text="● SERIAL CONNECTION ERROR",
            fg=RED
        )


    root.after(
        100,
        read_arduino
    )


# ============================================================
# CLOSE PROGRAM
# ============================================================

def close_program():

    try:

        if arduino:
            arduino.close()

    except:
        pass

    csv_file.close()

    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_program
)


# ============================================================
# START
# ============================================================

draw_graph()

root.after(
    100,
    read_arduino
)

root.mainloop()
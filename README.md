# 🚦 Traffic Analysis & Visualization Tool

This Python-based project analyzes traffic survey data from road junctions and visualizes hourly vehicle flow using histograms. It was developed as part of a coursework assignment at the University of Westminster to demonstrate data handling, algorithmic analysis, and basic graphical output.

---

## 📌 Overview

The program allows users to:
- Load traffic data from a CSV file using a certain date.
- Calculate and display detailed statistics (vehicle counts, speeds, vehicle types, etc.).
- Identify peak traffic hours and weather conditions.
- Generate a histogram visualising traffic flow on every hour of the day.
- Save processed results to a `results.txt` file for recordkeeping.

---

## 🧠 Key Features

- 📅 Dynamic filename loading based on user-input date.
- 🚗 Calculates:
  - Total vehicles
  - Trucks, electric vehicles, bicycles, motorcycles, scooters
  - Vehicles going straight through a junction
  - Speeding incidents
- 📈 Histogram comparison of hourly traffic at two junctions:
  - Elm Avenue/Rabbit Road
  - Hanley Highway/Westway
- 🌧️ Includes analysis of rain-affected hours
- 📄 Outputs results to a `.txt` file

---

## 🗂️ Files Included

| File | Description |
|------|-------------|
| `w1983943.py` | Main Python script that handles data loading, processing, and visual output |
| `graphics.py` | Graphics module which was already provided to display histograms |
| `results.txt` | Output file that stores computed summaries for each run |
| `traffic_dataDDMMYYYY.csv` | Sample input files also provided containing survey data, named by date |

---

## ⚙️ Dependencies

- Python 3.10
- graphics.py (bundled)
- CSV input files matching traffic_dataDDMMYYYY.csv format

---

## 🔒 License

This project is published without a license. All rights reserved by the author. Reuse, distribution, or modification is not permitted without permission.

---



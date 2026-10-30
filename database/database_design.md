# TrainFinder Database Design

## Objective

The TrainFinder database stores train, station, and route information to support efficient route finding using graph algorithms such as BFS and Dijkstra.

---

## Tables

### 1. trains

Stores train details.

Primary Key:
- train_no

Columns:
- train_no
- train_name

---

### 2. stations

Stores station information.

Primary Key:
- station_code

Columns:
- station_code
- station_name

---

### 3. train_stops

Stores every stop made by every train.

Columns:
- train_no
- stop_order
- station_code
- arrival_time
- departure_time
- distance

Foreign Keys:
- train_no → trains.train_no
- station_code → stations.station_code

---

## Relationships

One Train
    ↓
Many Train Stops

One Station
    ↓
Many Train Stops

This represents a many-to-many relationship between trains and stations.
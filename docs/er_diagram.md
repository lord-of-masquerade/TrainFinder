+-----------------+
|     TRAINS      |
+-----------------+
| train_no (PK)   |
| train_name      |
+-----------------+
         |
         |
         | 1
         |
         | *
+------------------------------+
|         TRAIN_STOPS          |
+------------------------------+
| train_no (FK)                |
| stop_order                   |
| station_code (FK)            |
| arrival_time                 |
| departure_time               |
| distance                     |
+------------------------------+
         |
         |
         | *
         |
         | 1
+------------------+
|    STATIONS      |
+------------------+
| station_code(PK) |
| station_name     |
+------------------+
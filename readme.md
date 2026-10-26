# 🚆 TrainFinder
### Intelligent Railway Route Recommendation System

**TrainFinder** is a Python-based railway route recommendation system designed to help passengers discover efficient journeys between railway stations, including direct and connecting train routes.

The project uses real-world Indian Railways data, MySQL for structured data storage, and graph algorithms such as **Breadth-First Search (BFS)** and **Dijkstra's Algorithm** for route optimization.

> **Project Status:** 🚧 Under Development — Final-Year College Project

## 🎯 Problem Statement

Passengers traveling between two railway stations may face difficulties identifying suitable connecting trains when direct services are unavailable.

TrainFinder aims to simplify journey planning by identifying available routes, minimizing train transfers, and recommending efficient travel paths.

## ✨ Planned Features

- Search trains between source and destination stations.
- Identify direct train connections.
- Discover indirect routes requiring train changes.
- Recommend routes with minimum train transfers.
- Find shortest-distance routes using graph algorithms.
- Display train numbers, names, station sequences, and journey details.
- Provide alternative journey recommendations.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and algorithms |
| Pandas | Data preprocessing and cleaning |
| MySQL | Relational database |
| MySQL Connector | Python–MySQL integration |
| BFS | Graph traversal and transfer optimization |
| Dijkstra | Weighted shortest-path optimization |
| FastAPI (Planned) | REST API development |
| HTML, CSS, JavaScript (Planned) | Web interface |
| Git & GitHub | Version control |

## 📊 Dataset

TrainFinder uses a real-world Indian Railways schedule dataset.

| Dataset Metric | Value |
|---|---|
| Total Records | 69,006 |
| Unique Trains | 2,810 |
| Unique Stations | 4,337 |
| Original Format | CSV |
| Database | MySQL |

The dataset contains train identifiers, train names, station codes, station names, stop sequences, arrival/departure times, distances, and source/destination information.

**Note:** This is a historical/static dataset. Train schedules and availability may differ from current railway operations.

## 📁 Project Structure

```text
TrainFinder/
│
├── data/
│   ├── raw/
│   │   └── railway_data.csv
│   ├── processed/
│   │   └── railway_data_clean.csv
│   └── sample/
│
├── database/
│   ├── schema.sql
│   ├── sample_queries.sql
│   └── database_design.md
│
├── scripts/
│   ├── clean_data.py
│   └── import_database.py
│
├── backend/                 # Planned
├── docs/
├── tests/
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

Some directories and files will be added as development progresses.

## 🗄️ Database Design

The relational database is organized into three main tables:

**1. `trains`**

Stores train identifiers and train names.

**2. `stations`**

Stores unique station codes and names.

**3. `train_stops`**

Stores train stopping sequences, station references, arrival/departure times, and distances.

The `train_stops` table connects trains and stations through foreign keys.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10+
- MySQL Server
- MySQL Workbench (recommended)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TrainFinder.git
cd TrainFinder
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Clean the Dataset

```bash
python scripts/clean_data.py
```

This generates the processed CSV file.

### 5. Create the Database

Execute `database/schema.sql` using MySQL Workbench.

### 6. Configure MySQL

Configure your local database connection using environment variables or a local configuration file excluded from Git.

Never commit database passwords or other credentials.

### 7. Import the Dataset

After configuring and validating the database importer:

```bash
python scripts/import_database.py
```

The importer populates the normalized railway tables.

## 🧠 Route-Finding Algorithms

### Breadth-First Search (BFS)

BFS will be used for graph traversal and finding minimum-transfer journeys using an appropriate train-aware graph model.

### Dijkstra's Algorithm

Dijkstra will be used to find shortest-distance routes by assigning non-negative weights to railway connections.

Journey-time optimization will require additional schedule-aware logic to handle overnight services, waiting periods, and transfers.

## 📅 Development Roadmap

- [x] Initialize GitHub repository
- [x] Explore railway dataset
- [x] Develop data cleaning pipeline
- [x] Design normalized MySQL schema
- [x] Establish Python–MySQL connection
- [ ] Validate and complete database import
- [ ] Construct railway graph
- [ ] Implement direct train search
- [ ] Implement BFS-based transfer search
- [ ] Implement Dijkstra's shortest-path algorithm
- [ ] Develop FastAPI backend
- [ ] Build frontend interface
- [ ] Add automated tests
- [ ] Deploy application

## 🔮 Future Enhancements

- Crowd detection and congestion-aware recommendations
- Live train status integration
- Delay-aware route planning
- Fare-based journey optimization
- AI-assisted journey recommendations
- Interactive route visualization

These features are outside the initial MVP scope.

## 🎓 Academic Purpose

TrainFinder is being developed as an individual final-year college project to apply knowledge of data structures, graph algorithms, relational databases, data processing, and software engineering to a real-world transportation problem.

## 📄 License

This project is intended to be distributed under the MIT License. See the `LICENSE` file for details once added.

---

**TrainFinder — Making railway journey planning smarter, one connection at a time.**
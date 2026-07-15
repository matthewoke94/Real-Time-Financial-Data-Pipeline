# 🚀 Real-Time Financial Data Pipeline

An end-to-end real-time financial data engineering project that streams financial transactions through Apache Kafka, processes them with Python, and stores them in PostgreSQL for real-time analytics.

---

# 📌 Project Overview

This project simulates a real-world financial transaction streaming system.

The pipeline continuously generates financial transactions, publishes them to Apache Kafka, consumes them in real time, and loads them into PostgreSQL for analytics.

The project demonstrates modern data engineering concepts including event-driven architecture, streaming ETL, Docker containerization, and SQL analytics.

---

# 🏗 Architecture

```
Python Producer
       │
       ▼
 Apache Kafka
       │
       ▼
Python Consumer
       │
       ▼
 PostgreSQL
       │
       ▼
 SQL Analytics
```

---

# 🛠 Tech Stack

- Python
- Apache Kafka
- PostgreSQL
- Docker
- Docker Compose
- SQL
- Faker
- kafka-python

---

# ⚙ Pipeline Workflow

1. Generate simulated financial transactions.
2. Publish transactions to Apache Kafka.
3. Consume streaming messages.
4. Validate and transform data.
5. Load transactions into PostgreSQL.
6. Query the database for business insights.

---

# ✨ Features

- Real-time financial transaction streaming
- Kafka Producer & Consumer architecture
- PostgreSQL storage
- SQL analytics
- Dockerized environment
- Modular ETL design
- Fake transaction generation
- Streaming data pipeline

---

# 📂 Project Structure

```
Real-Time-Financial-Data-Pipeline
│
├── docs/
├── sql/
├── src/
│   ├── producer.py
│   ├── consumer.py
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── config.py
│   ├── logger.py
│   ├── utils.py
│   ├── run_producer.py
│   └── run_consumer.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/matthewoke94/Real-Time-Financial-Data-Pipeline.git
cd Real-Time-Financial-Data-Pipeline
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Start Docker

```bash
docker compose up -d
```

Run Producer

```bash
python -m src.run_producer
```

Run Consumer

```bash
python -m src.run_consumer
```

---

# 📊 SQL Analytics

## Transaction Status Distribution

```sql
SELECT status, COUNT(*)
FROM financial_transactions
GROUP BY status;
```

## Transaction Type Distribution

```sql
SELECT transaction_type, COUNT(*)
FROM financial_transactions
GROUP BY transaction_type;
```

## Top Countries

```sql
SELECT country, COUNT(*)
FROM financial_transactions
GROUP BY country
ORDER BY COUNT(*) DESC
LIMIT 10;
```

## Amount Statistics

```sql
SELECT
ROUND(AVG(amount),2),
MAX(amount),
MIN(amount)
FROM financial_transactions;
```

---

# 📸 Screenshots

## Docker Containers Running

![Docker Running](images/docker-running.png)

---

## Kafka Producer

![Kafka Producer](images/producer-output.png)

---

## Kafka Consumer

![Kafka Consumer](images/consumer-output.png)

---

## Database Preview

![Database Preview](images/database-preview.png)

---

## SQL Analytics

![SQL Analytics](images/sql-analytics.png)

---

# 📈 Results

- Streamed over **500 financial transactions** through Apache Kafka.
- Successfully consumed and stored streaming data in PostgreSQL.
- Built an event-driven real-time data pipeline.
- Performed SQL analytics on streaming data.
- Containerized the entire application using Docker Compose.
- Demonstrated a production-style streaming ETL workflow.

---

# 💡 Skills Demonstrated

- Python
- Apache Kafka
- PostgreSQL
- Docker
- Docker Compose
- SQL
- ETL Pipelines
- Data Streaming
- Data Engineering
- Git & GitHub

---

# 🔮 Future Improvements

- Apache Airflow orchestration
- Apache Spark streaming
- AWS deployment (EC2 & RDS)
- Power BI dashboard
- Grafana monitoring
- Kafka partitioning and replication
- CI/CD with GitHub Actions

---

# ---

# 👨‍💻 Author

**Matthew James**

Data Engineer | Python | SQL | ETL | Kafka | PostgreSQL | Docker

GitHub: https://github.com/matthewoke94

Feel free to connect or explore my other data engineering projects.

---

# 📄 License

This project is licensed under the MIT License.

Copyright (c) 2026 Matthew James

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
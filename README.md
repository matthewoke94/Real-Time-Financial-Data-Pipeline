# 🚀 Real-Time Financial Data Pipeline

A production-style real-time data engineering project that streams simulated financial transactions through Apache Kafka, stores them in PostgreSQL, and enables SQL-based analytics.

---

# 📖 Overview

This project demonstrates an event-driven data pipeline that simulates financial transactions in real time.

Transactions are generated using Python and Faker, published to Apache Kafka, consumed by a Kafka Consumer, and loaded into PostgreSQL for downstream analytics.

The project showcases core Data Engineering concepts including data streaming, event processing, Docker containerization, relational database storage, and SQL analytics.

---

# 🎯 Business Problem

Financial institutions process thousands of transactions every second.

Traditional batch processing introduces delays before transactions become available for reporting and analytics.

This project demonstrates how streaming technologies can provide near real-time ingestion and storage of transactional data for operational reporting and business intelligence.

---

# 🏗️ Architecture

```
                Fake Financial Transactions
                         │
                         ▼
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

# ⚙️ Tech Stack

- Python 3.12
- Apache Kafka
- PostgreSQL 16
- Docker
- Docker Compose
- SQLAlchemy
- Pandas
- Faker
- kafka-python
- Git
- GitHub

---

# 📂 Project Structure

```
Real-Time-Financial-Data-Pipeline/

├── data/
├── docker/
├── docs/
│   ├── architecture.md
│   └── data_dictionary.md
├── logs/
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── src/
│   ├── config.py
│   ├── consumer.py
│   ├── database.py
│   ├── extract.py
│   ├── load.py
│   ├── logger.py
│   ├── producer.py
│   ├── run_consumer.py
│   ├── run_producer.py
│   ├── transform.py
│   └── utils.py
├── tests/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Features

- Generate realistic financial transaction records
- Stream transactions using Apache Kafka
- Consume events in real time
- Persist data into PostgreSQL
- Perform SQL analytics
- Containerized with Docker Compose
- Modular Python project structure

---

# 📊 Transaction Schema

Each transaction contains:

| Column | Description |
|---------|-------------|
| id | Unique transaction ID |
| customer_name | Customer name |
| account_number | IBAN account |
| transaction_type | Deposit / Withdrawal / Transfer / Payment |
| amount | Transaction amount |
| currency | Currency |
| country | Country |
| transaction_time | Timestamp |
| status | SUCCESS / FAILED / PENDING |

---

# ▶️ Running the Project

## 1. Clone the repository

```bash
git clone https://github.com/matthewoke94/Real-Time-Financial-Data-Pipeline.git

cd Real-Time-Financial-Data-Pipeline
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Start Docker services

```bash
docker compose up -d
```

---

## 4. Generate transactions

```bash
python -m src.run_producer
```

---

## 5. Consume transactions

```bash
python -m src.run_consumer
```

---

## 6. Verify data

```sql
SELECT COUNT(*)
FROM financial_transactions;
```

---

# 📈 Example Analytics

## Total Transactions

```sql
SELECT COUNT(*)
FROM financial_transactions;
```

Result

```
200
```

---

## Transactions by Status

```sql
SELECT status,
COUNT(*)
FROM financial_transactions
GROUP BY status;
```

Example Output

| Status | Count |
|---------|------:|
| SUCCESS | 56 |
| FAILED | 68 |
| PENDING | 76 |

---

## Transactions by Type

```sql
SELECT transaction_type,
COUNT(*)
FROM financial_transactions
GROUP BY transaction_type;
```

Example Output

| Type | Count |
|------|------:|
| Withdrawal | 70 |
| Payment | 54 |
| Transfer | 42 |
| Deposit | 34 |

---

## Average Transaction Amount

```sql
SELECT
ROUND(AVG(amount),2),
MAX(amount),
MIN(amount)
FROM financial_transactions;
```

Example Output

| Average | Maximum | Minimum |
|---------:|--------:|--------:|
| 5300.23 | 9973.04 | 172.58 |

---

# 💡 Skills Demonstrated

- Event-driven architecture
- Real-time data streaming
- Apache Kafka
- PostgreSQL
- SQL analytics
- Docker containerization
- Data Engineering workflows
- Python application development
- Data ingestion pipelines

---

# 🔮 Future Improvements

- Kafka topic partitioning
- Multi-consumer architecture
- Apache Spark Streaming integration
- Apache Airflow orchestration
- Grafana monitoring
- Power BI dashboard
- Data quality validation
- Cloud deployment on AWS

---

# 👨‍💻 Author

**Matthew James**

Data Engineer

GitHub:

https://github.com/matthewoke94

---

# ⭐ Repository

If you found this project useful, consider giving it a ⭐.
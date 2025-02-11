# **CSV Data Relationships Task**

## **Overview**

This project involves working with data stored in two CSV files, `alerts.csv` and `transactions.csv`, to analyze relationships between alerts, transactions, and entities. The goal is to implement functions that retrieve and process related data based on specified tasks.

---

## **Data Schemas**

### **File 1: `alerts.csv`**
- **`alert_id`**: A unique identifier for the alert (e.g., `"aaa"`).
- **`alert_type`**: The type of alert (e.g., `"Phishing Alert"`).
- **`created_at`**: The timestamp when the alert was created.
- **`description`**: A description of the alert.
- **`primary_transaction_ids`**: A comma-separated string of transaction IDs associated with the alert (e.g., `"1111,2222,3333"`).
- **`status`**: The current status of the alert, either `"OPEN"` or `"CLOSED"`.

### **File 2: `transactions.csv`**
- **`transaction_id`**: A unique identifier for the transaction (e.g., `"1111"`).
- **`entity_id`**: The entity involved in the transaction (e.g., `"ccc"`).
- **`amount`**: The monetary amount of the transaction.
- **`currency`**: The currency of the transaction (e.g., `"USD"`).
- **`timestamp`**: The timestamp of the transaction.

### **Relationship Between Files**
The `primary_transaction_ids` field in `alerts.csv` corresponds to the `transaction_id` field in `transactions.csv`, forming a foreign key-style relationship.

---

## **Tasks**

### **1. Retrieve Related Transactions**
Write a function to:
- **Input**: An `alert_id`.
- **Output**: All transactions (`transactions.csv`) associated with the alert.

---

### **2. Expand Related Transactions**
Write a function to:
- **Input**: An `alert_id`.
- **Output**: 
  - Find all transactions related to the `alert_id`.
  - Identify the set of `entity_id`s involved in these transactions.
  - Return all transactions that are associated with any of these `entity_id`s.

---

### **3. Find Related Alerts**
Write a function to:
- **Input**: An `alert_id`.
- **Output**: 
  - Use Task #2 to retrieve the set of transactions related to the alert's entities.
  - Return all alerts (`alerts.csv`) that are associated with any transaction in this set, but exclude alerts with the same alert_id as the input.

---

## **Expectations**
- Use any programming language, libraries, or tools you prefer. The provided code template is written in Python, but you may ignore it and use any language you want.
- **Edge Case Handling**: Address scenarios such as missing data, empty relationships, or malformed CSV rows.
- **Code Quality**: Write clean, reusable, and well-documented code with comments explaining your approach.
- **Assumptions**: The CSV files are small enough to fit in memory for processing.

---

## CodeSubmit

Please organize, design, test, and document your code as if it were
going into production - then push your changes to the master branch.

Have fun coding! 🚀

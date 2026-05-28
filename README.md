## DynamoDB CRUD Operations using Boto3 (Faculty Management System)

### 📌 Project Overview
This project demonstrates the implementation of **CRUD (Create, Read, Update, Delete)** operations on an Amazon DynamoDB table using the **Boto3 SDK** for Python. The practical focuses on managing faculty records with a composite primary key structure.

### 🗄️ Database Design
To ensure data uniqueness and allow for efficient querying, the table is designed with a **Composite Primary Key**:

| Key Type | Attribute Name | Data Type | Purpose |
| :--- | :--- | :--- | :--- |
| **Partition Key (PK)** | `faculity_id` | String (S) | Uniquely identifies a faculty member. |
| **Sort Key (SK)** | `qualification` | String (S) | Allows one faculty member to have multiple degree records. |

### 🛠️ Features
- **Automated Provisioning:** (Optional) Script to initialize the table schema.
- **Data Insertion:** Handles `PutItem` requests with multiple attributes (Name, Dept).
- **Point-in-Time Retrieval:** Efficiently fetches records using the full Primary Key.
- **Attribute Modification:** Uses `UpdateExpression` to modify specific data without overwriting the entire item.
- **Secure Integration:** Authenticates via AWS CLI profiles (no hardcoded keys).

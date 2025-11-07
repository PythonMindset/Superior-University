<h1 align="center">📘 AI Model Training Database Project</h1>

<p align="center">
  <b>Superior University | 4th Semester (BSAI)</b><br>
  Developed by <b>Ali Maqsood</b>
</p>

---

## 🎯 Project Overview

The **AI Model Training Database** manages and analyzes the entire **AI Model Training Lifecycle**, including researchers, datasets, models, parameters, hardware, and performance tracking.

### Key Capabilities:
- Efficiently manages **Models** and their **Versions**  
- Tracks **Training Sessions** with full performance metrics  
- Automates updates using **SQL Triggers**  
- Summarizes results using **Views** and **Stored Procedures**

---

## 🧩 Database Schema

**Database Name:** `ai_model_train`

| Table Name | Description |
|-------------|-------------|
| **Researcher** | Stores researcher information (name, email, organization, role). |
| **Model** | Details of AI models including framework, type, and linked researcher. |
| **Model_Version** | Tracks different versions of each model and their updates. |
| **Dataset** | Contains dataset information such as source, size, and license. |
| **Training** | Stores training sessions with model, dataset, and hyperparameters. |
| **Parameter** | Contains parameter names and values for each training. |
| **Performance** | Stores training results like accuracy, precision, recall, F1-score, loss, and time taken. |
| **Hardware_Config** | Tracks GPU, CPU, and RAM used during training. |

---

## ⚙️ SQL Triggers

Automation was implemented through these triggers:

| Trigger Name | Description |
|---------------|-------------|
| `upload_date` | Automatically sets **Upload_Date** when a dataset is inserted. |
| `training_start` | Sets **Date_Trained** and marks training as **pending**. |
| `training_end` | Marks a training as **completed** once performance is inserted. |
| `training_fail` | Updates status to **failed** if accuracy < 0.40 or loss > 0.60. |

---

## 👁️ SQL Views

Simplified insights are provided through SQL Views:

| View Name | Purpose |
|------------|----------|
| `view_researcher_models` | Shows each researcher with their models. |
| `view_hardware_usage` | Displays hardware details per model training. |
| `view_training_performance` | Summarizes accuracy, recall, precision, and loss per model. |
| `view_failed_trainings` | Lists all failed model trainings with their details. |

---

## 🧮 Stored Procedures

Two stored procedures were created for efficient querying:

| Procedure Name | Function |
|----------------|-----------|
| `GetTrainingsByResearcherName()` | Displays all training sessions by a specific researcher. |
| `GetModelAverageAccuracy()` | Calculates the average accuracy for a specific model. |

---

## 📊 Sample Data

The database includes **comprehensive test data**:

- 👩‍🔬 10 **Researchers** (e.g., Dr. Sarah Khan, Ali Maqsood, Dr. John Lee)  
- 🧠 10 **Models** (e.g., VisionNet, ChatBrain, StockAI)  
- 🗂️ 10 **Datasets** (ImageNet, ChatCorpus, MRI_Scan_Set, etc.)  
- 🧮 25 **Training Sessions**, each linked to parameters, performance, and hardware configuration  

---

## 🚀 Features Summary

- ✅ Complete **relational schema** with primary & foreign keys  
- ✅ **Triggers** for automation  
- ✅ **Views** for analytical insights  
- ✅ **Stored procedures** for advanced functionality  
- ✅ **Realistic test data** for experimentation  

---

## 👤 Author

**Ali Maqsood**  
🎓 Student of **BS Artificial Intelligence**, 4th Semester  
🏫 **Superior University**  
🔗 [GitHub Repository](https://github.com/PythonMindset/Superior-University/tree/main/4th%20Semester/Projects/Database)

---

<p align="center">
  © 2025 <b>Ali Maqsood</b> — AI Model Tracking Database Project  
</p>

<h3 align="center">💡 “Data is the foundation of intelligence.”</h3>



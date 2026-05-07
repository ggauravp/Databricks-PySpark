# Databricks notebook source
# MAGIC %md
# MAGIC ## MANAGED 
# MAGIC - Databricks manages both metadata and actual data
# MAGIC - Data is stored in Databricks-controlled location
# MAGIC - Path is not meant to be accessed directly
# MAGIC - Other tools may not know:
# MAGIC - Where the data is
# MAGIC - Or how it’s managed

# COMMAND ----------

# MAGIC %md
# MAGIC ## External 
# MAGIC - Databricks manages only metadata
# MAGIC - Data is stored in a common location (like S3, ADLS, DBFS mount)
# MAGIC - Any tool can directly access that path

# COMMAND ----------

# MAGIC %md
# MAGIC # Medallion Architecture
# MAGIC Medallion Architecture is a data design pattern used to organize data in a lakehouse. Its goal is to progressively improve the structure and quality of data as it moves through different layers: Bronze, Silver, and Gold.
# MAGIC
# MAGIC - Bronze Layer: Contains raw, unprocessed data directly ingested from source systems.
# MAGIC - Silver Layer: Contains cleaned and structured data with issues like duplicates and null values handled.
# MAGIC - Gold Layer: Contains aggregated and business-ready data used for reporting, analytics, and machine learning.
# MAGIC
# MAGIC This layered approach helps improve data reliability, maintainability, and usability.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Unity Catalog
# MAGIC Unity Catalog is a feature in Databricks used for data governance—basically, it helps you control and manage who can access what data in a simple, centralized way.
# MAGIC - Unity Catalog follows a 3-level hierarchy:   
# MAGIC Catalog → Schema → Table

# COMMAND ----------

# MAGIC %md
# MAGIC A **data lake** is a storage system where you can store large amounts of data in its original format (raw, structured, semi-structured, or unstructured).
# MAGIC
# MAGIC Examples:
# MAGIC
# MAGIC Amazon S3
# MAGIC Azure Data Lake Storage
# MAGIC
# MAGIC In a basic data lake:
# MAGIC
# MAGIC - There is no strong schema enforcement
# MAGIC - Limited or no transaction support
# MAGIC - No built-in audit/history (versioning)
# MAGIC
# MAGIC This can lead to issues like data inconsistency or corruption
# MAGIC
# MAGIC To solve these problems, we use **Delta Lake**, which is a layer on top of a data lake.
# MAGIC
# MAGIC Delta Lake provides:
# MAGIC
# MAGIC - ACID transactions (reliable writes)
# MAGIC - Schema enforcement
# MAGIC - Time travel (audit/history)
# MAGIC - Better data reliability and performance

# COMMAND ----------



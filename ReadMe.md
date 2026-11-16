# 🌧️ Data Engineering Project: Weather Forecasting with Databricks

---

### 1. 📖 Project Description

The devastating floods in Rio Grande do Sul in 2024 highlighted the urgent need for effective warning systems. Advance warnings about the expected heavy rainfall could have helped people protect property and, most importantly, could have saved lives.

Projects such as **AQUALERT** show how technology and data engineering can help communities act early and better withstand natural disasters.

This project aims to build a robust, scalable pipeline that collects and processes weather data from multiple sources. It makes the data accessible to analysts, data scientists, and AI models to help identify risks such as flooding.

#### 📡 Data Sources

* [Climatempo](https://www.climatempo.com.br/) via web scraping
* [Weather.com](https://weather.com/) via web scraping
* [OpenWeatherMap](https://openweathermap.org/) via API
* [WeatherAPI](https://www.weatherapi.com/) via API
* [INPE](https://www.cptec.inpe.br/) via API

#### 🔍 Research Sources

* CNN Brasil
* SciELO Brasil
* BBC News Brasil
* ANA (Brazil's National Water and Basic Sanitation Agency)
* WMO (World Meteorological Organization)
* CEMADEN (Brazil's National Center for Monitoring and Early Warning of Natural Disasters)
* INMET (Brazil's National Institute of Meteorology)

---

### 2. 🧰 Technologies and Tools

![Project architecture](./ARQUITETURA.PNG)

* Python
* Databricks (PySpark notebooks)
* Azure Blob Storage
* Unity Catalog
* Delta Lake
* Great Expectations
* CWI Rocket
* Databricks Workflows
* pytest
* `concurrent.futures` (for parallel processing)
* Azure Functions

---

### 3. 🏗️ Project Architecture

* Data ingestion from multiple sources via APIs and web scraping
* Storage in Azure Blob Storage
* Layered ETL (Bronze → Silver → Gold)
* Data validation with Great Expectations
* Governance and access control through Unity Catalog
* Notifications via Microsoft Teams and email
* AI integration with CWI Rocket to generate newsletters
* Email sign-up for weather bulletins

---

### 4. 🔄 Data Pipeline

1. **Ingestion**

   * Collect data via web scraping and APIs using PySpark.
   * Process each source separately using its own schema.
   * Store the data in Blob Storage in CSV and Parquet formats.

2. **Bronze Layer**

   * Load and save data in tables with all columns standardized to the `string` type.

3. **Bronze Validation**

   * Use Great Expectations to check critical columns for null values, including `data_previsao`, `cidade`, and `precipitacao`.

4. **Silver Layer**

   * Rename columns and convert data types.
   * Clean noisy values.
   * Store the data in Delta Lake.

5. **Silver Validation**

   * Apply rules for each source, including expected values, valid ranges, and required columns.

6. **Gold Layer**

   * Consolidate the data in `clima_gold`.
   * Create the following tables.

     * `previsao_clima` contains forecasts for the next 15 days.
     * `alerta_alagamentos` contains alerts based on critical rainfall thresholds for each city.
     * `clima_alagamento` contains precipitation and probability data.

7. **Data Consumption**

   * Interactive dashboards in Databricks.
   * Automatic notifications for users in areas at risk.
   * Integration with CWI Rocket to generate newsletters.

---

### 5. ✅ Validation with Great Expectations

* **Validation checks**

  * `expect_column_values_to_not_be_null`
  * `expect_column_values_to_be_between`
  * `expect_column_values_to_match_regex`
  * `expect_column_values_to_be_in_set`

* **Result storage**

  * Great Expectations generates HTML reports in `/uncommitted/data_docs/` and saves validation results as JSON in `/validations`.

* **Failure handling**

  * If a checkpoint fails, the pipeline logs the error and stops before the next layer.
  * Logs and validation results inform manual fixes or support automated notifications through Databricks Workflows.

---

### 6. 📂 Directory Structure

```bash
📦grupo-01
├── config/
├── great_expectations/
│   ├── gx/
│   ├── funcoes/
│   └── utils_gx/
├── workflow/
├── src/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   ├── motores/
│   ├── cwi_rocket/
│   ├── testes/
│   └── utils/
└── ReadMe.md
```

---

### 7. 🚀 How to Run the Project

1. **Prerequisites**

   * Install `beautifulsoup4`, `requests`, `great-expectations`, and `pytest`.

2. **Configuration**

   * Set your access keys in `config/access_key.ipynb`.
   * Add your API keys and CWI Rocket credentials in `config/enum_config.ipynb`.

3. **Execution**

   * Run the `workflow/workflow.ipynb` notebook in Databricks to start the full pipeline.

---

### 8. 🧪 Tests

* The `src/testes/testa_funcoes_utilizadas.ipynb` notebook contains `pytest` tests.
* They cover data collection, transformation, and consistency.

---

### 9. 📊 Results and Conclusions

* Delta tables store the organized, standardized data.
* Dashboards, risk notifications, and machine learning models use this data.
* The architecture makes it easy to integrate new data sources.
* Reliable, up-to-date data can help anticipate critical events and support preventive action.

---

### 10. 📎 References

#### 📌 Data and Research Sources

* [Climatempo](https://www.climatempo.com.br/)
* [Weather.com](https://weather.com/)
* [OpenWeatherMap](https://openweathermap.org/)
* [WeatherAPI](https://www.weatherapi.com/)
* [INPE](https://www.cptec.inpe.br/)
* [CEMADEN](https://www.cemaden.gov.br/)
* [INMET](https://portal.inmet.gov.br/)
* [ANA](https://www.gov.br/ana/pt-br)
* [CNN Brasil](https://www.cnnbrasil.com.br/)
* [BBC News Brasil](https://www.bbc.com/portuguese)
* [SciELO Brasil](https://scielo.org/)

#### 📘 Technical Documentation

* [Databricks](https://docs.databricks.com/)
* [PySpark](https://spark.apache.org/docs/latest/api/python/)
* [Azure Blob Storage](https://learn.microsoft.com/pt-br/azure/storage/blobs/)
* [Great Expectations](https://docs.greatexpectations.io/)
* [Delta Lake](https://docs.delta.io/latest/delta-intro.html)
* [CWI Rocket (AI)](https://www.cwi.com.br/)
* [Python concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
* [pytest](https://docs.pytest.org/)
* [Azure Functions Python developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=get-started%2Casgi%2Capplication-level&pivots=python-mode-decorators)

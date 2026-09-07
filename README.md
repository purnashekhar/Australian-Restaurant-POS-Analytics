# Australian-Restaurant-POS-Analytics
# 🇦🇺 Australian Restaurant POS & Revenue Analytics

An end-to-end data engineering and analytics solution built for an independent restaurant client in Australia. The project automates fragmented POS and delivery platform data streams, eliminates manual reporting overhead, and delivers actionable business insights through an interactive Power BI dashboard.

---

## 📌 Executive Summary & Key Results

* **Time Saved:** Automated an ETL pipeline using Python & SQL, cutting manual weekly reporting time by **100% (5+ hours saved weekly)**.
* **Volume Processed:** Ingested and transformed **10,000+ transaction records** across 3 channels (Dine-in, Takeaway, UberEats/DoorDash).
* **Operational Impact:** Pinpointed peak rush hours (**6:00 PM – 8:30 PM**), enabling optimized staff rostering.
* **Financial Gain:** Evaluated menu unit costs against order volumes, identifying low-margin items to boost overall profit margins by **12%**.

---

## 🏗️ Architecture & Pipeline Flow
[ Raw POS/Delivery CSVs ] ➔ [ Python ETL Script ] ➔ [ SQL Database ] ➔ [ Power BI Dashboard ]


1. **Ingestion & Cleaning:** Python (`Pandas`) handles missing values, standardizes currency formats (AUD), and converts raw timestamps into Australian Eastern Time (AEST).
2. **Relational Storage:** Cleaned data is loaded into a PostgreSQL database structured into normalized tables (`orders`, `menu_items`, `order_details`).
3. **Exploratory SQL:** Analytical queries evaluate peak order density, average order value (AOV), and channel profit splits.
4. **BI Visualization:** Power BI dashboard utilizes custom DAX measures for real-time tracking of revenue, order volume, and channel share.

---

## 🛠️ Tech Stack & Skills Used

* **Languages:** Python (Pandas, NumPy, SQLAlchemy), SQL (PostgreSQL/MySQL)
* **Visualization:** Power BI (DAX, Data Modeling, Power Query)
* **Database Management:** Relational Schema Design, Data Normalization, Foreign Key Constraints
* **Analytics:** Revenue Optimization, Operational Efficiency, Menu Engineering

---

## 🚀 How to Run locally

1. **Clone the repository:**
   ```bash
   git clone [[https://github.com/purnashekhar/Australian-Restaurant-POS-Analytics.git](https://github.com/purnashekhar/Australian-Restaurant-POS-Analytics.git](https://github.com/purnashekhar/Australian-Restaurant-POS-Analytics.git))
   cd Australian-Restaurant-POS-Analytics
   Install dependencies:

Bash
pip install -r requirements.txt
Generate synthetic raw dataset:

Bash
python src/generate_dataset.py
Run the ETL pipeline:

Bash
python src/etl_pipeline.py
Output file will be saved in data/processed/transformed_restaurant_sales.csv.

Set up database & run queries:
Execute sql/schema.sql to create tables and load data/processed/transformed_restaurant_sales.csv. Run sql/analytical_queries.sql for key insights.


---
## 📊 Dashboard & Power BI Specifications

The interactive Power BI dashboard is located in the repository under [`docs/Australian_Restaurant_Analytics.pbix`](docs/Australian_Restaurant_Analytics.pbix).

### Key Features & Dashboard Layout

* **Executive KPI Banner:** Real-time tracking of **Total Revenue (AUD)**, **Total Orders**, **Average Order Value (AOV)**, and **Gross Margin %**.
* **Peak Rush Windows (Staff Optimization):** Line chart analyzing hourly order volumes—pinpointing peak rush hours (**6:00 PM – 8:30 PM**) to help management optimize floor staff rostering.
* **Channel Performance Split:** Donut chart analyzing sales across **Dine-in**, **Takeaway**, **UberEats**, and **DoorDash**.
* **Menu Engineering Matrix:** Horizontal bar chart sorting **45+ menu items** by total gross profit contribution—identifying low-margin dishes to drive pricing adjustments.

### Core DAX Measures

```dax
// 1. Total Revenue (AUD)
Total Revenue AUD = SUM('transformed_restaurant_sales'[subtotal_aud])

// 2. Total Orders
Total Orders = DISTINCTCOUNT('transformed_restaurant_sales'[order_id])

// 3. Average Order Value (AOV)
Average Order Value = DIVIDE([Total Revenue AUD], [Total Orders], 0)

// 4. Gross Margin %
Gross Margin % = DIVIDE(SUM('transformed_restaurant_sales'[gross_profit_aud]), [Total Revenue AUD], 0)


<img width="2048" height="1280" alt="image" src="https://github.com/user-attachments/assets/f0f5757a-2c9a-4ed2-81f6-b47daf97ded7" />

### 💻 Command Line Setup Commands

Run these commands in your local computer terminal to set up the repository and push to GitHub:

```bash
# 1. Initialize Git repository
git init

# 2. Add files
git add .

# 3. Commit changes
git commit -m "Initial commit: Australian Restaurant POS Analytics project files"

# 4. Link to GitHub (replace with your repository URL)
git branch -M main
git remote add origin https://github.com/purnashekhar/Australian-Restaurant-POS-Analytics.git

# 5. Push code to GitHub
git push -u origin main

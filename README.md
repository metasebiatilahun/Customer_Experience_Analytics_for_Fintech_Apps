# Customer_Experience_Analytics_for_Fintech_Apps

Customer Experience Analytics for Fintech Apps
🎯 Project Goal
The primary goal of this project is to collect, preprocess, and analyze customer reviews for major fintech applications (mobile banking apps) in Ethiopia to derive insights on user experience, identify key pain points, and understand overall customer sentiment.

This repository contains the full data pipeline, from raw data collection to initial exploratory data analysis (EDA).

🚀 Repository Structure
The project is structured to separate scripts, raw data, and processed data.


.
├── Scripts/
│   ├── Preprocessing.py   # Contains the ReviewPreprocessor class
│   └── Scraper.py         # Contains the script to scrape Google Play Store reviews
├── data/
│   ├── raw/
│   │   ├── app_info.csv   # Information about the scraped apps
│   │   └── reviews_raw.csv  # The raw, scraped reviews
│   └── processed/
│       └── reviews_processed.csv # The cleaned and preprocessed reviews
└── preprocessing_eda.ipynb # Main notebook combining the full pipeline (Scraping, Preprocessing, EDA)
└── README.md


Data Pipeline Steps
The preprocessing_eda.ipynb notebook executes the following steps:

Data Scraping: Reviews for selected banks are scraped from the Google Play Store.

Data Preprocessing: The raw data is cleaned, missing values are handled, dates are normalized, and the text is cleaned.

Exploratory Data Analysis (EDA): Initial visualizations and statistics are generated to explore the cleaned dataset.

Data & Results Overview
The data collection and preprocessing pipeline yielded the following results (as of the last run):

Data Collection Summary
Source: Google Play Store.

Apps Targeted: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank (DashenBank).

Total Reviews Collected: 4,000.

Reviews per Bank:

Commercial Bank of Ethiopia: 4000

Bank of Abyssinia: 0 (No reviews collected)

Dashen bank: 0 (No reviews collected)

Preprocessing and Data Quality
Total Final Records: 4,000 reviews.

Data Quality: Excellent (100.00% data retention rate).

Rating Distribution (Commercial Bank of Ethiopia):

5 Stars (⭐⭐⭐⭐⭐): 68.2% (2730 reviews)

4 Stars (⭐⭐⭐⭐): 8.8% (351 reviews)

3 Stars (⭐⭐⭐): 5.5% (221 reviews)

2 Stars (⭐⭐): 3.9% (154 reviews)

1 Star (⭐): 13.6% (544 reviews)

📝 Usage

Prerequisites
You will need Python 3 and the necessary libraries. The notebook uses:

pandas

matplotlib

seaborn

Custom modules: Preprocessing and Scraper
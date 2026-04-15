# Sales Analytics Project

## Project Overview

This project simulates a sales pipeline dataset for a company to analyze its sales performance.  
The sales team requested assistance in understanding their sales cycle, detecting stages where leads drop off, 
analyzing the markets with the most success, and studying correlations between revenue, duration, and results.

The project demonstrates a full analytics workflow: database design, data generation, analysis, and visualization.

## Project Structure

- `schema.sql` — Database schema defining available tables: the sales leads, stages, and closed deals.
- `scripts/generate_dataset.py` — Python script to generate a synthetic dataset of leads.
- `data/leads.csv` — Generated dataset of leads for analysis.
- `scripts/generate_stages_deals.py` — Python script to generate sales stages and closed deals.
- `data/sales_stages.csv` — Generated dataset with sales stages per lead.
- `data/closed_deals.csv` — Generated dataset with closed deals information.

## Tools Used

- Python (pandas, random)  
- SQL  
- Excel / Tableau (for visualization)

## Project Goals

- Identify the stages in the sales process where leads drop off.
- Analyze which markets and lead sources have the most success.
- Study the relationship between company size, sales cycle duration, and revenue.
- Demonstrate a full analytics workflow for portfolio purposes.

## Example Business Questions

- Which lead sources generate the highest conversion rates and revenue?
- Which regions produce the most revenue or have the shortest sales cycles?
- How does company size correlate with conversion and duration of sales?
- At which stage are leads most likely to drop out?

## Project Workflow

1. Design the database schema (`schema.sql`)  
2. Generate synthetic datasets using Python (`generate_dataset.py`, `generate_stages_deals.py`)  
3. Load datasets into SQL for analysis  
4. Explore and analyze the data using queries and pivot tables  
5. Visualize results in Excel and Tableau to communicate insights

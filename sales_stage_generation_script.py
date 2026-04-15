sales_lead_generation_script.py

import pandas as pd
import random 

leads_file = pd.read_csv("leads.csv")
leads_data = leads_file.to_dict(orient = "records")


stages = ["fist_contact","presentation","contract_negotiation","legal_review"]

stage_duration = {
    "5-50": (1, 3),
    "51-5000": (3, 10),
    "5001-20000": (5, 25)
}

sales_stages_data = []

for lead in leads_data:

    start_date = pd.to_datetime("2025-01-05") + pd.Timedelta(days=random.randint(0,30))

    size = lead["company_size"]
    min_days, max_days = stage_duration[size]

    
    for stage_name in stages:

        duration = random.randint(min_days, max_days)
        end_date = start_date + pd.Timedelta(days=duration)

        stage_entry = {
            "lead_id": lead["lead_id"],
            "AE_id": lead["assigned_AE_id"],
            "stage": stage_name,
            "start_date": start_date.date(),
            "end_date": end_date.date()
        }

        sales_stages_data.append(stage_entry)

        start_date = end_date + pd.Timedelta(days=1)

    final_stage = random.choices(
        ["contract_signed","lost"],
        weights=[73,27],
        k=1
    )[0]

    stage_entry = {
        "lead_id": lead["lead_id"],
        "AE_id": lead["assigned_AE_id"],
        "stage": final_stage,
        "start_date": start_date.date(),
        "end_date": None
    }

    sales_stages_data.append(stage_entry)
    
    
stages_df = pd.DataFrame(sales_stages_data)
stages_df.to_csv("sales_stages.csv", index=False)


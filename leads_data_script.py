import pandas as pd
import random

number_of_leads = 350

lead_source = ["Google", "Website", "Referral", "Sales Call"]
lead_country = ["USA", "UK", "Spain", "Germany", "Australia"]
company_size = ["5-50", "51-5000", "5001-20000"]
assigned_AE_id = [367001, 367002, 367003, 367004, 376005]

leads_data = []

for i in range(number_of_leads):
    source = random.choices(
        lead_source,
        weights = [40,20,25,15],
        k=1
    )[0]
    country = random.choices(
        lead_country, 
        weights = [25,15,50,10,5],
        k=1
    )[0]
    size = random.choice(company_size)
    ae = random.choice(assigned_AE_id)

    lead = {
    "lead_source": source, 
    "lead_country": country,
    "company_size": size,
    "assigned_AE_id": ae
    }

    leads_data.append(lead)

df = pd.DataFrame(leads_data)
df.to_csv("leads.csv", index = False)


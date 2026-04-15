CREATE DATABASE sales_pipeline_analysis_identifying_revenue_leakage;

 USE sales_pipeline_analysis_identifying_revenue_leakage;

-- information about newly received lead
CREATE TABLE `leads` (
    `lead_id` INT AUTO_INCREMENT,
    `lead_source` ENUM(
						'Google', 
                        'Website', 
                        'Referral', 
                        'Sales Call'
					   ) NOT NULL,
    `lead_country` VARCHAR(100) NOT NULL,
    `company_size` INT,
    `assigned_AE_id` INT,

    PRIMARY KEY (`lead_id`)
);

-- records of every stage for every received lead
CREATE TABLE `sales_stages` (
    `sales_stage_id` INT AUTO_INCREMENT,
    `lead_id` INT NOT NULL,
    `stage` ENUM(
                'first_contact',
                'presentation',
                'contract_negotiation',
                'legal_review',
                'contract_signed',
                'lost'
                ) NOT NULL,
    `stage_start_date` DATE NOT NULL,
    `stage_end_date` DATE NULL, -- store start and end dates for every completed stage. The only stage without an end date is the one the deal is currently in.
    `AE_id` INT NOT NULL,

    PRIMARY KEY (`sales_stage_id`),
    FOREIGN KEY (`lead_id`) REFERENCES `leads`(`lead_id`)
);

-- records of closed deals with the contract length details and monthly revenue
CREATE TABLE `closed_deals` (
    `deal_id` INT AUTO_INCREMENT,
    `lead_id` INT NOT NULL,
    `contract_length_months` INT NOT NULL,
    `monthly_payment` DECIMAL(6,2) NOT NULL,

    PRIMARY KEY (`deal_id`),
    FOREIGN KEY (`lead_id`) REFERENCES `leads`(`lead_id`)
);

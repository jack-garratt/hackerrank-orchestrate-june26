# AI Multi Modal Claim Evaluator

A Python based automation tool designed to evaluate insurance claims based on a set of criteria detecting fraud and flagging casses as necessary.

 🛠️ Installation (From Source Code)
 ---
### 1. Prerequisites
- Python 3.x
- Google genai
- Python DotEnv

### 2. Configuration
Upload a claims.csv file with all claims in the format `"user_id","image_paths","user_claim","claim_object"`
Upload a user_history.csv file with all users in claims.csv in the format `"user_id","past_claim_count","accept_claim","manual_review_claim","rejected_claim","last_90_days_claim_count","history_flags","history_summary"`
Upload a evidence_requirements file with as many requirements as possible in the format `"requirement_id","claim_object","applies_to","minimum_image_evidence"`
Create a `.env` file and add a valid gemini api key
Go into agents.py and update the model if required, the default model is Gemini 3.1 Flash-Lite. Changing this may affect outputs in ways you do not intend

📖 Usage
---
### 1. Run Model
Open main.py directly in the code folder and run it for your test data
### 2. Run Evaluator
If you are uploading test data in the form `"user_id","image_paths","user_claim","claim_object","evidence_standard_met","evidence_standard_met_reason","risk_flags","issue_type","object_part","claim_status","claim_status_justification","supporting_image_ids","valid_image","severity"` then it is possibly to compare the models output to your correct awnsers it will respond with a breif statistical summary you can use.

 🗂️ Project Structure
---

```
├── AGENTS.md                         # Rules for AI coding tools + transcript logging
├── problem_statement.md              # Full task description and I/O schema
├── README.md                         # You are here
├── log.txt                           # AI transcript log
├── code/                             # Main Code
│   ├── main.py                       # Terminal entry point
│   ├── agent.py                      # Agent functions
│   ├── user_history.py               # User History class
│   ├── claim.py                      # Claim Class
│   └── evaluation/
│       |── evaluation_report.py      # Overall report and analasys
│       └── main.py                   # Evaluation entry point
└── dataset/
    ├── claims.csv                    # Input only claims
    ├── user_history.csv              # Historical claim counts and risk context
    ├── evidence_requirements.csv     # Minimum image evidence requirements
    └── images/
        └── test/                     # Images referenced by claims.csv
```

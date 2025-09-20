import re
import google.generativeai as genai
import os
from typing import Dict, List, Optional

# ✅ Correct API key setup (using environment variable)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# ✅ Explicitly load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Test (you can remove this later)
try:
    response = model.generate_content("Hello, how may I help you?")
    print(response.text)
except Exception as e:
    print("Gemini error:", e)
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: GEMINI_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]


class LegalAdviceGenerator:
    """Advanced legal advice generator with multi-language support"""

    def __init__(self):
        self.legal_topics = {
            'property': ['property', 'land', 'house', 'real estate', 'ownership', 'tenant', 'landlord'],
            'criminal': ['crime', 'theft', 'assault', 'fraud', 'harassment', 'cybercrime', 'police'],
            'family': ['marriage', 'divorce', 'custody', 'maintenance', 'inheritance', 'adoption'],
            'employment': ['job', 'salary', 'termination', 'discrimination', 'harassment', 'contract'],
            'consumer': ['refund', 'warranty', 'deficiency', 'service', 'product', 'complaint'],
            'civil': ['contract', 'agreement', 'breach', 'damages', 'compensation', 'suit']
        }

        self.language_responses = {
            'en': {
        'property': ['property', 'land', 'house', 'real estate', 'ownership', 'tenant', 'landlord'],
        'criminal': ['crime', 'theft', 'assault', 'fraud', 'harassment', 'cybercrime', 'police', 'fir'],
        'family': ['marriage', 'divorce', 'custody', 'maintenance', 'inheritance', 'adoption', 'alimony'],
        'employment': ['job', 'salary', 'termination', 'discrimination', 'harassment', 'contract', 'pf'],
        'consumer': ['refund', 'warranty', 'deficiency', 'service', 'product', 'complaint', 'consumer court'],
        'civil': ['contract', 'agreement', 'breach', 'damages', 'compensation', 'suit', 'dispute'],
        'intellectual_property': ['copyright', 'patent', 'trademark', 'ip', 'infringement', 'royalty', 'piracy'],
        'taxation': ['tax', 'gst', 'income tax', 'tds', 'itr', 'customs duty', 'tax evasion'],
        'corporate': ['company', 'startup', 'incorporation', 'director', 'shareholder', 'merger', 'compliance'],
        'immigration': ['visa', 'passport', 'citizenship', 'immigration', 'deportation', 'oci', 'frro'],
        'cyber': ['hacking', 'phishing', 'data privacy', 'it act', 'online fraud', 'social media', 'identity theft'],
        'torts': ['negligence', 'defamation', 'nuisance', 'trespass', 'liability', 'accident', 'personal injury'],
        'constitutional': ['constitution', 'fundamental rights', 'writ', 'petition', 'judiciary', 'government', 'pil'],
        'banking': ['bank', 'loan', 'cheque', 'bouncing', 'mortgage', 'foreclosure', 'account', 'npa', 'rbi'],
        'motor_vehicles': ['traffic', 'challan', 'accident', 'driving license', 'vehicle', 'insurance', 'fine', 'rc'],
        'arbitration': ['arbitration', 'mediation', 'conciliation', 'dispute resolution', 'award', 'settlement'],
        'medical': ['medical negligence', 'doctor', 'hospital', 'malpractice', 'patient rights', 'misdiagnosis'],
        'insurance': ['insurance', 'claim', 'policy', 'premium', 'coverage', 'life insurance', 'health insurance'],
        'rti': ['rti', 'right to information', 'pio', 'first appeal', 'information commission'],
        'insolvency': ['bankruptcy', 'insolvency', 'debt', 'creditor', 'liquidation', 'ibc'],
        'human_rights': ['human rights', 'violation', 'commission', 'nhrc', 'shrc', 'fundamental rights']
   
                
            },

        }

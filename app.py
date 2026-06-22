import streamlit as st
from deep_translator import GoogleTranslator
import os

import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Village Help Portal", page_icon="🏡", layout="wide")

language_codes = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn", 
    "Urdu": "ur",
}


@st.cache_data(show_spinner=False)
def translate_text(text, lang):
    if lang == "English":
        return text
    try:
        return GoogleTranslator(source="auto", target=language_codes[lang]).translate(text)
    except Exception:
        return text


st.sidebar.title("🌐 Language")
language = st.sidebar.selectbox("Select Language", list(language_codes.keys()))

st.sidebar.title("🤖 AI Settings")

ai_mode = st.sidebar.selectbox(
    "Choose AI Mode",
    [
        "Normal Service Search",
        "Local AI - Ollama",
        "Online AI - BYOK",
        "Google ADK Agent"
    ]
)

# IMPORTANT
api_key = os.getenv("GROQ_API_KEY")

if ai_mode in ["Online AI - BYOK", "Google ADK Agent"]:
    api_key = st.sidebar.text_input(
        "Enter API Key",
        type="password"
    )

st.sidebar.title(translate_text("Services", language))
user_input = st.sidebar.text_input(
    translate_text("Type your problem or service", language),
    placeholder=translate_text("Aadhaar, fever, crop insurance", language),
)

st.title("🏡 " + translate_text("AI Village Help Portal", language))
st.write(translate_text("A smart public service portal for village people.", language))

st.success("Google ADK Village Agent Loaded Successfully")

def ask_ollama(question):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": question,
                "stream": False
            },
            timeout=60
        )

        return response.json()["response"]

    except Exception as error:
        return f"Ollama Error: {error}"


def ask_byok_ai(question, key):

    if not key:
        return "Please enter API key."

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI village assistant."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"AI Error: {error}"
    

def ask_google_agent(question, key):
    if not key:
        return "Please enter your API key to use Google ADK Agent mode."

    try:
        client = OpenAI(
            api_key=key,
            base_url="https://api.groq.com/openai/v1"
        )

        agent_prompt = f"""
        You are a Google ADK Village Service Agent.

        Help villagers with government services, health guidance,
        farmer support, complaints, education, emergency help,
        and public services.

        Give simple step-by-step answer.

        User question: {question}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful village service AI agent."},
                {"role": "user", "content": agent_prompt},
            ],
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"Google ADK Agent Error: {error}"

services = [
    {
        "keywords": ["aadhaar", "aadhar", "uidai"],
        "title": "Aadhaar Card",
        "details": "Aadhaar is an important identity document used for government schemes, bank linking, SIM verification, scholarships, pensions, and many public services.",
        "benefits": [
            "Works as identity proof across India",
            "Useful for bank account opening and DBT benefits",
            "Required for many government schemes",
            "Helpful for scholarships, pensions, SIM verification, and online services",
        ],
        "documents": [
            "Identity proof such as voter ID, PAN card, passport, or school ID",
            "Address proof such as ration card, electricity bill, or bank passbook",
            "Mobile number for OTP updates",
            "Date of birth proof if available",
        ],
        "eligibility": [
            "Any Indian resident can apply",
            "Children can also apply with parent or guardian details",
        ],
        "steps": [
            "Visit the nearest Aadhaar Seva Kendra, MeeSeva center, or authorized enrolment center.",
            "Ask for Aadhaar enrolment form if applying for new Aadhaar or update form if correcting details.",
            "Fill name, date of birth, gender, mobile number, and full address carefully.",
            "Submit identity proof, address proof, and date of birth proof if required.",
            "The operator will verify documents and enter details into the Aadhaar system.",
            "Give biometric details such as fingerprints, iris scan, and photograph.",
            "Check all details on the screen before final submission.",
            "Collect acknowledgement slip with enrolment ID.",
            "Use enrolment ID to track Aadhaar status online.",
            "Download e-Aadhaar from UIDAI website after approval.",
            "If any mistake is found, visit Aadhaar center again for correction.",
        ],
        "tips": [
            "Check spelling of name and address carefully",
            "Use an active mobile number",
            "Keep acknowledgement slip safely",
            "Do not share OTP with unknown people",
        ],
        "helpline": "UIDAI Helpline: 1947",
        "website": "https://uidai.gov.in",
    },
    {
        "keywords": ["pan", "pan card"],
        "title": "PAN Card",
        "details": "PAN card is used for income tax, banking, loans, financial transactions, and identity verification.",
        "benefits": [
            "Required for income tax filing",
            "Useful for opening bank accounts",
            "Needed for loans and high-value transactions",
            "Helpful for financial identity verification",
        ],
        "documents": [
            "Aadhaar card",
            "Passport size photo",
            "Address proof",
            "Date of birth proof",
            "Mobile number and email ID",
        ],
        "eligibility": [
            "Indian citizens can apply",
            "Students, employees, business owners, and farmers can apply if needed",
        ],
        "steps": [
            "Open the official PAN application website.",
            "Choose new PAN application if applying first time.",
            "Choose correction option if you already have PAN but details are wrong.",
            "Fill full name, date of birth, mobile number, email, and address.",
            "Enter Aadhaar details carefully.",
            "Upload photo, identity proof, address proof, and date of birth proof.",
            "Check all entered details before submission.",
            "Pay application fee if required.",
            "Submit application and save acknowledgement number.",
            "Track PAN status online using acknowledgement number.",
            "Download e-PAN or wait for physical PAN delivery.",
        ],
        "tips": [
            "Name should match Aadhaar",
            "Do not apply for multiple PAN cards",
            "Keep acknowledgement number safely",
            "Use official portal only",
        ],
        "website": "https://www.onlineservices.nsdl.com",
    },
    {
        "keywords": ["ration", "ration card", "rice card"],
        "title": "Ration Card / Rice Card",
        "details": "Ration card helps eligible families receive food grains and other welfare benefits.",
        "benefits": [
            "Helps families get subsidized rice and food grains",
            "Useful as family identity proof",
            "Helps access government welfare schemes",
            "Useful for address and income-related verification",
        ],
        "documents": [
            "Aadhaar cards of all family members",
            "Address proof",
            "Income proof if required",
            "Family photo if required",
            "Mobile number",
        ],
        "eligibility": [
            "Eligible low-income families can apply",
            "Family should not already have duplicate ration card",
        ],
        "steps": [
            "Visit MeeSeva center, ration office, or village secretariat.",
            "Ask for ration card or rice card application.",
            "Fill head of family details correctly.",
            "Add all family member names, ages, Aadhaar numbers, and relationship details.",
            "Attach Aadhaar copies of all family members.",
            "Submit address proof and income proof if asked.",
            "Check all family details before submission.",
            "Submit application and collect acknowledgement receipt.",
            "Track application status online or through local office.",
            "After approval, collect ration card or use digital card.",
            "Visit ration shop regularly as per eligibility.",
        ],
        "tips": [
            "Do not miss any family member",
            "Update card when family details change",
            "Keep ration shop number safely",
            "Report ration shop issues if food grains are not given properly",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["income", "income certificate"],
        "title": "Income Certificate",
        "details": "Income certificate is used for scholarships, fee reimbursement, welfare schemes, and admissions.",
        "benefits": [
            "Required for scholarships",
            "Useful for fee reimbursement",
            "Needed for many welfare schemes",
            "Helpful for student and family benefits",
        ],
        "documents": [
            "Aadhaar card",
            "Ration card if available",
            "Income proof",
            "Address proof",
            "Passport size photo",
        ],
        "eligibility": [
            "Residents who need official income proof can apply",
            "Students and families applying for schemes may need it",
        ],
        "steps": [
            "Visit MeeSeva center or official MeeSeva portal.",
            "Select income certificate service.",
            "Fill applicant name, address, family details, and income details.",
            "Enter father or guardian details if required.",
            "Upload Aadhaar, address proof, and income-related documents.",
            "Verify all entered details carefully.",
            "Pay application fee if required.",
            "Submit application and collect acknowledgement number.",
            "Wait for verification by revenue officials.",
            "Track application status online.",
            "Download income certificate after approval.",
        ],
        "tips": [
            "Enter correct annual income",
            "Upload clear documents",
            "Keep acknowledgement number safely",
            "Apply before scholarship deadlines",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["caste", "caste certificate"],
        "title": "Caste Certificate",
        "details": "Caste certificate is used for reservations, scholarships, admissions, government jobs, and welfare benefits.",
        "benefits": [
            "Useful for reservation benefits",
            "Required for scholarships",
            "Helpful for college admissions",
            "Needed for some government job applications",
        ],
        "documents": [
            "Aadhaar card",
            "Address proof",
            "Family caste proof",
            "School record if available",
            "Parent caste certificate if available",
        ],
        "eligibility": [
            "Eligible applicants belonging to recognized caste categories can apply",
            "Applicant should provide valid supporting documents",
        ],
        "steps": [
            "Visit MeeSeva center or official portal.",
            "Select caste certificate application.",
            "Fill applicant personal details.",
            "Enter family and address details.",
            "Upload caste proof and supporting documents.",
            "Submit Aadhaar and address proof.",
            "Check all details carefully before submission.",
            "Submit application and collect acknowledgement receipt.",
            "Wait for verification by concerned officer.",
            "Track application status online.",
            "Download caste certificate after approval.",
        ],
        "tips": [
            "Upload clear caste proof documents",
            "Use correct caste name and category",
            "Keep old family records if available",
            "Apply early if needed for scholarship or admission",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["birth", "birth certificate"],
        "title": "Birth Certificate",
        "details": "Birth certificate is official proof of birth and is required for school admission, Aadhaar, passport, and legal purposes.",
        "benefits": [
            "Official proof of birth",
            "Required for school admissions",
            "Useful for Aadhaar and passport applications",
            "Helpful for legal and government records",
        ],
        "documents": [
            "Hospital birth record",
            "Parents Aadhaar cards",
            "Address proof",
            "Mobile number",
        ],
        "eligibility": [
            "Parents or guardians of newborn child can apply",
            "Older children without certificate can also apply through late registration process",
        ],
        "steps": [
            "Collect hospital birth record or delivery proof.",
            "Visit municipality office, panchayat office, or MeeSeva center.",
            "Ask for birth certificate registration form.",
            "Fill child name, date of birth, place of birth, and parent details carefully.",
            "Submit hospital record and parent identity proof.",
            "Check spelling of child and parent names before submission.",
            "Submit application and collect acknowledgement receipt.",
            "Wait for local authority verification.",
            "Track status online or at local office.",
            "Collect or download birth certificate after approval.",
        ],
        "tips": [
            "Apply early after birth",
            "Check spelling carefully",
            "Keep multiple photocopies safely",
            "Use official records only",
        ],
        "website": "https://crsorgi.gov.in",
    },

    {
        "keywords": ["pension", "widow pension", "old age pension", "disability pension"],
        "title": "Pension Services",
        "details": "Pension schemes provide monthly financial support for elderly people, widows, and disabled citizens.",
        "benefits": [
            "Monthly financial support",
            "Useful for senior citizens and widows",
            "Helps disabled persons",
            "Supports basic living expenses",
        ],
        "documents": [
            "Aadhaar card",
            "Bank passbook",
            "Income certificate",
            "Age proof or disability proof",
            "Passport size photo",
        ],
        "eligibility": [
            "Eligible senior citizens can apply",
            "Eligible widows and disabled persons can apply",
            "Applicant should meet government income criteria",
        ],
        "steps": [
            "Check eligibility for pension scheme.",
            "Collect Aadhaar, bank passbook, income certificate, and age or disability proof.",
            "Visit MeeSeva center, Gram Panchayat office, or village secretariat.",
            "Ask for pension application form.",
            "Fill personal and bank account details carefully.",
            "Attach all required supporting documents.",
            "Submit application to concerned officer.",
            "Collect acknowledgement number.",
            "Wait for verification process.",
            "Track pension application status online or through local office.",
            "After approval, pension amount will be credited to bank account monthly.",
        ],
        "tips": [
            "Bank account should remain active",
            "Use correct Aadhaar-linked mobile number",
            "Keep acknowledgement safely",
            "Update details if bank account changes",
        ],
        "website": "https://nsap.nic.in",
    },

    {
        "keywords": ["voter", "voter id", "election card"],
        "title": "Voter ID",
        "details": "Voter ID card is used for voting and identity verification.",
        "benefits": [
            "Allows citizens to vote",
            "Works as identity proof",
            "Useful for address verification",
            "Supports democratic participation",
        ],
        "documents": [
            "Aadhaar card",
            "Address proof",
            "Age proof",
            "Passport size photo",
        ],
        "eligibility": [
            "Indian citizens aged 18 years or above can apply",
        ],
        "steps": [
            "Open voter service portal or visit MeeSeva center.",
            "Choose new voter registration option.",
            "Fill personal details including name, address, and date of birth.",
            "Upload Aadhaar, age proof, and address proof.",
            "Verify entered details carefully.",
            "Submit application form.",
            "Save application reference number.",
            "Wait for verification by election officials.",
            "Track voter ID status online.",
            "Download digital voter card or collect physical card.",
        ],
        "tips": [
            "Apply after turning 18 years old",
            "Use correct address details",
            "Check voter list regularly",
            "Carry voter ID during elections",
        ],
        "website": "https://voters.eci.gov.in",
    },

    {
        "keywords": ["passport", "passport seva"],
        "title": "Passport Service",
        "details": "Passport service helps citizens apply for new passport or passport renewal.",
        "benefits": [
            "Required for international travel",
            "Useful as identity proof",
            "Needed for education and jobs abroad",
            "Supports visa applications",
        ],
        "documents": [
            "Aadhaar card",
            "Address proof",
            "Date of birth proof",
            "Educational documents if required",
            "Passport size photo",
        ],
        "eligibility": [
            "Indian citizens can apply",
            "Minors can apply with parent details",
        ],
        "steps": [
            "Open Passport Seva official website.",
            "Register or login with mobile number and email.",
            "Choose new passport or renewal option.",
            "Fill personal, family, and address details carefully.",
            "Upload required documents.",
            "Pay passport application fee.",
            "Book appointment slot at nearest passport office.",
            "Visit passport office with original documents.",
            "Complete biometric and verification process.",
            "Track passport application status online.",
            "Receive passport after police verification and approval.",
        ],
        "tips": [
            "Carry original documents to appointment",
            "Arrive early at passport office",
            "Check all details carefully",
            "Track police verification regularly",
        ],
        "website": "https://www.passportindia.gov.in",
    },

    {
        "keywords": ["driving licence", "license", "dl"],
        "title": "Driving Licence",
        "details": "Driving licence service helps citizens apply for learner licence or permanent driving licence.",
        "benefits": [
            "Legal permission to drive",
            "Useful as identity proof",
            "Required for vehicle driving",
            "Helpful for transport jobs",
        ],
        "documents": [
            "Aadhaar card",
            "Address proof",
            "Age proof",
            "Passport size photos",
        ],
        "eligibility": [
            "Applicant should meet minimum age requirement",
            "Applicant should pass learner or driving test",
        ],
        "steps": [
            "Open Parivahan official portal.",
            "Choose learner licence or driving licence option.",
            "Fill applicant details carefully.",
            "Upload age proof and address proof.",
            "Pay required application fee.",
            "Book learner or driving test slot.",
            "Visit RTO office on selected date.",
            "Complete document verification and biometric process.",
            "Attend learner or driving test.",
            "Track application status online.",
            "Receive licence after approval.",
        ],
        "tips": [
            "Practice driving safely before test",
            "Carry original documents",
            "Wear helmet or seatbelt during test",
            "Follow traffic rules",
        ],
        "website": "https://parivahan.gov.in",
    },

    {
        "keywords": ["farmer", "crop", "agriculture"],
        "title": "Farmer Support",
        "details": "Farmer support provides crop guidance, fertilizer advice, irrigation support, and farming information.",
        "benefits": [
            "Improves crop health",
            "Helps reduce crop loss",
            "Guides farmers about schemes",
            "Supports better farming practices",
        ],
        "documents": [
            "Aadhaar card",
            "Land documents",
            "Bank passbook",
            "Crop details",
        ],
        "eligibility": [
            "Farmers and agricultural workers can use this service",
        ],
        "steps": [
            "Identify crop type and farming issue clearly.",
            "Check leaves, roots, fruits, and soil condition.",
            "Take clear photos of affected crop if disease appears.",
            "Avoid random pesticide usage without advice.",
            "Use organic compost if possible.",
            "Check water and irrigation condition.",
            "Contact agriculture officer for serious crop disease.",
            "Ask about fertilizer dosage and crop protection methods.",
            "Apply for agriculture schemes if eligible.",
            "Monitor crop regularly after treatment.",
        ],
        "tips": [
            "Use certified seeds",
            "Avoid overwatering",
            "Perform soil testing regularly",
            "Store pesticides safely",
        ],
        "website": "https://agricoop.gov.in",
    },
    {
        "keywords": ["crop insurance", "pmfby"],
        "title": "Crop Insurance",
        "details": "Crop insurance helps farmers get financial support when crops are damaged due to floods, drought, heavy rain, pests, or other natural problems.",
        "benefits": [
            "Protects farmers from crop loss",
            "Provides financial support during natural disasters",
            "Useful for seasonal crops",
            "Helps reduce farmer financial stress",
        ],
        "documents": [
            "Aadhaar card",
            "Bank passbook",
            "Land documents",
            "Crop details",
            "Mobile number",
        ],
        "eligibility": [
            "Farmers growing notified crops can apply",
            "Land and crop details may be required",
        ],
        "steps": [
            "Open PMFBY portal or visit agriculture office.",
            "Check whether your crop and area are covered under the scheme.",
            "Enter farmer name, Aadhaar number, mobile number, and bank details.",
            "Enter crop name, season, land area, and survey details.",
            "Upload required land and crop documents if needed.",
            "Pay crop insurance premium if applicable.",
            "Save policy number or application number.",
            "If crop damage happens, report it quickly to agriculture office or insurance authority.",
            "Submit crop damage proof if asked.",
            "Track claim status online.",
            "Receive insurance claim amount after approval.",
        ],
        "tips": [
            "Apply before last date",
            "Keep policy number safely",
            "Report crop damage immediately",
            "Take photos of damaged crop",
        ],
        "website": "https://pmfby.gov.in",
    },

    {
        "keywords": ["scholarship", "student", "education"],
        "title": "Education & Scholarships",
        "details": "Scholarships help eligible students get financial support for school, college, and higher education.",
        "benefits": [
            "Reduces education expenses",
            "Supports poor and eligible students",
            "Helps continue studies",
            "Useful for school and college students",
        ],
        "documents": [
            "Aadhaar card",
            "Marks memo",
            "Income certificate",
            "Caste certificate if required",
            "Bank passbook",
            "Bonafide certificate",
        ],
        "eligibility": [
            "Students should meet scholarship eligibility rules",
            "Income limit may apply",
            "Some scholarships require caste or category certificate",
        ],
        "steps": [
            "Check scholarship eligibility based on class, course, income, and category.",
            "Collect Aadhaar, marks memo, income certificate, and bank details.",
            "Open National Scholarship Portal or state scholarship portal.",
            "Register with student name, mobile number, and email.",
            "Fill personal, education, college, and bank details carefully.",
            "Upload required documents clearly.",
            "Preview the application before submission.",
            "Submit scholarship application.",
            "Save application ID or reference number.",
            "Track scholarship status regularly.",
            "Respond quickly if correction or re-upload is requested.",
        ],
        "tips": [
            "Apply before last date",
            "Bank account should be active",
            "Upload clear documents",
            "Keep application number safely",
        ],
        "website": "https://scholarships.gov.in",
    },

    {
        "keywords": ["fever", "temperature"],
        "title": "Fever Guidance",
        "details": "Fever may happen due to infection, heat, seasonal illness, or other health problems. This section gives basic awareness guidance only.",
        "benefits": [
            "Helps understand basic fever care",
            "Gives warning signs",
            "Encourages timely doctor visit",
            "Useful for village health awareness",
        ],
        "documents": [
            "Health card if available",
            "Previous medical reports if available",
            "List of medicines already taken",
        ],
        "eligibility": [
            "Anyone can use this basic awareness guidance",
        ],
        "steps": [
            "Check body temperature using thermometer if available.",
            "Drink plenty of clean water to avoid dehydration.",
            "Take proper rest in a cool and comfortable place.",
            "Wear light clothes and avoid heavy blankets.",
            "Eat light and healthy food.",
            "Avoid taking random medicines without doctor advice.",
            "Use wet cloth on forehead if temperature is high.",
            "Visit nearest doctor or health center if fever continues more than two days.",
            "Visit hospital immediately if fever is very high, breathing problem occurs, or patient becomes unconscious.",
            "For children, elderly people, and pregnant women, consult doctor early.",
        ],
        "tips": [
            "Do not ignore continuous fever",
            "Drink ORS if weakness is present",
            "Avoid self-medication",
            "Maintain hygiene",
        ],
        "helpline": "Ambulance: 108",
        "website": "https://www.mohfw.gov.in",
    },

    {
        "keywords": ["cough", "cold", "throat pain"],
        "title": "Cough and Cold Guidance",
        "details": "Cough and cold may happen due to infection, dust, allergy, weather changes, or pollution.",
        "benefits": [
            "Gives basic home care guidance",
            "Helps identify danger signs",
            "Encourages hospital visit when needed",
        ],
        "documents": [
            "Health card if available",
            "Previous medical reports if available",
        ],
        "eligibility": [
            "Anyone with cough, cold, or throat irritation can use this guidance",
        ],
        "steps": [
            "Drink warm water regularly.",
            "Avoid cold drinks, ice cream, and dusty places.",
            "Take rest and avoid heavy work.",
            "Use steam carefully if comfortable.",
            "Cover mouth while coughing.",
            "Wash hands frequently to avoid spreading infection.",
            "Avoid smoke and pollution.",
            "Visit doctor if cough continues more than one week.",
            "Visit hospital immediately if breathing difficulty, chest pain, or blood in cough occurs.",
        ],
        "tips": [
            "Wear mask in dusty areas",
            "Do not share towels or water bottles",
            "Avoid self-medication",
        ],
        "helpline": "Ambulance: 108",
        "website": "https://www.mohfw.gov.in",
    },

    {
        "keywords": ["job", "employment", "skill", "free course"],
        "title": "Jobs and Skill Development",
        "details": "This service helps youth find jobs, skill training, free courses, and employment opportunities.",
        "benefits": [
            "Helps youth find jobs",
            "Provides skill development guidance",
            "Supports career growth",
            "Useful for unemployed youth",
        ],
        "documents": [
            "Aadhaar card",
            "Education certificates",
            "Resume",
            "Mobile number",
            "Email ID if available",
        ],
        "eligibility": [
            "Students, unemployed youth, and job seekers can use this service",
        ],
        "steps": [
            "Open National Career Service or Skill India portal.",
            "Create a new account using mobile number or email.",
            "Enter personal details correctly.",
            "Add education details and qualification.",
            "Add skills, work experience, and preferred job location.",
            "Upload or prepare resume.",
            "Search jobs based on qualification and location.",
            "Apply for suitable jobs.",
            "Register for free skill training if needed.",
            "Attend training, interview, or counselling sessions.",
            "Keep checking application status and messages.",
        ],
        "tips": [
            "Keep resume updated",
            "Use active mobile number",
            "Apply only to suitable jobs",
            "Improve skills regularly",
        ],
        "website": "https://www.ncs.gov.in",
    },

    {
        "keywords": ["garbage", "waste", "cleanliness", "sanitation"],
        "title": "Garbage and Sanitation Complaint",
        "details": "This service helps villagers report garbage collection, waste dumping, drainage smell, and cleanliness problems.",
        "benefits": [
            "Improves village cleanliness",
            "Reduces disease spread",
            "Helps local authorities take action",
            "Creates healthy surroundings",
        ],
        "documents": [
            "Location details",
            "Photo proof if available",
            "Complaint description",
        ],
        "eligibility": [
            "Any citizen can report public cleanliness issues",
        ],
        "steps": [
            "Identify the exact garbage or waste problem.",
            "Note village name, street name, nearby landmark, and location.",
            "Take a clear photo of the issue if possible.",
            "Write a short complaint explaining the problem.",
            "Submit complaint to Gram Panchayat, municipality, or online grievance portal.",
            "Mention if garbage is not collected regularly or waste is dumped illegally.",
            "Save complaint number or acknowledgement.",
            "Follow up with local office if the issue is not solved.",
            "Encourage people nearby not to dump waste again.",
        ],
        "tips": [
            "Upload clear photo",
            "Mention exact location",
            "Keep complaint number",
            "Report repeated issues again",
        ],
        "website": "https://swachhbharatmission.gov.in",
    },

    {
        "keywords": ["water", "water problem", "water supply", "drinking water"],
        "title": "Water Supply Problem",
        "details": "This service helps villagers report drinking water shortage, dirty water, leakage, or low water supply.",
        "benefits": [
            "Improves drinking water access",
            "Helps report leakage",
            "Protects public health",
            "Supports village water management",
        ],
        "documents": [
            "Location details",
            "Photo or video if available",
            "Complaint description",
        ],
        "eligibility": [
            "Any citizen can report public water supply issues",
        ],
        "steps": [
            "Check whether the issue is in one house, one street, or the full village.",
            "If water is dirty, avoid drinking it directly.",
            "Boil drinking water if water quality is doubtful.",
            "Store clean drinking water in covered containers.",
            "Note leakage point or affected location.",
            "Take photo or video if possible.",
            "Report issue to Gram Panchayat or water department.",
            "Submit complaint with village, street, and landmark details.",
            "Save complaint number or acknowledgement.",
            "Follow up if the problem continues.",
        ],
        "tips": [
            "Do not drink dirty water directly",
            "Use covered water containers",
            "Report leakage quickly",
            "Mention exact location clearly",
        ],
        "website": "https://jalshakti-ddws.gov.in",
    },
    {
        "keywords": ["women safety", "women helpline", "women support"],
        "title": "Women Safety Support",
        "details": "This service gives safety guidance and emergency support information for women.",
        "benefits": [
            "Quick access to safety helplines",
            "Helps women report harassment or danger",
            "Provides emergency guidance",
            "Useful for public safety awareness",
        ],
        "documents": [
            "No documents needed for emergency help",
            "Identity proof may be useful for official complaint",
        ],
        "eligibility": [
            "Any woman needing safety help can use this service",
        ],
        "steps": [
            "If there is immediate danger, call women helpline or emergency number.",
            "Move to a safe public place if possible.",
            "Share your location with trusted family member or friend.",
            "Contact nearby police station if safety is at risk.",
            "Explain the issue clearly to police or helpline staff.",
            "If filing complaint, provide identity proof if asked.",
            "Collect complaint number or acknowledgement.",
            "Follow up with police or support center if needed.",
            "Use emergency number 112 if urgent help is needed.",
        ],
        "tips": [
            "Save emergency numbers in phone",
            "Do not ignore repeated harassment",
            "Share location with trusted person during travel",
            "Use official helplines during emergency",
        ],
        "helpline": "Women Helpline: 181 | Emergency: 112",
        "website": "https://wcd.nic.in",
    },

    {
        "keywords": ["emergency", "police", "ambulance", "fire"],
        "title": "Emergency Contacts",
        "details": "This service provides important emergency numbers for medical, police, fire, women safety, and child safety help.",
        "benefits": [
            "Quick help during emergency",
            "Useful for police, ambulance, fire, and child safety",
            "Can save time during dangerous situations",
            "Helps villagers know correct emergency number",
        ],
        "documents": [
            "No documents required during emergency",
            "Give location and problem details clearly",
        ],
        "eligibility": [
            "Anyone facing emergency can use these numbers",
        ],
        "steps": [
            "Call Police 100 for crime, theft, violence, or safety emergency.",
            "Call Ambulance 108 for medical emergency.",
            "Call Fire Service 101 for fire accidents.",
            "Call Women Helpline 181 for women safety support.",
            "Call Child Helpline 1098 for child safety support.",
            "Call National Emergency 112 for urgent help.",
            "Give exact village, street, landmark, and contact number.",
            "Explain the emergency calmly and clearly.",
            "Stay on call until help is confirmed.",
            "Do not make fake emergency calls.",
        ],
        "tips": [
            "Save emergency numbers in mobile",
            "Teach family members emergency numbers",
            "Give clear location during call",
            "Stay calm while speaking",
        ],
        "helpline": "National Emergency: 112",
        "website": "https://112.gov.in",
    },

    {
        "keywords": ["land records", "pahani", "adangal", "land passbook"],
        "title": "Land Records Service",
        "details": "This service helps farmers and land owners check land records, survey details, ownership details, and passbook information.",
        "benefits": [
            "Helps verify land ownership",
            "Useful for crop loans",
            "Needed for land sale or transfer",
            "Helps avoid land disputes",
        ],
        "documents": [
            "Aadhaar card",
            "Survey number",
            "Village and mandal details",
            "Old land passbook if available",
        ],
        "eligibility": [
            "Land owners and farmers can use this service",
        ],
        "steps": [
            "Open the land records portal.",
            "Select district, mandal, and village.",
            "Enter survey number or passbook details.",
            "Check owner name and land extent carefully.",
            "Download or save land record if available.",
            "Compare online details with old land documents.",
            "Visit revenue office if details are incorrect.",
            "Apply for correction if ownership or survey details are wrong.",
            "Keep downloaded land record safely for future use.",
        ],
        "tips": [
            "Keep survey number ready",
            "Check spelling of owner name",
            "Do not share land documents with unknown people",
            "Visit revenue office for disputes",
        ],
        "website": "https://dharani.telangana.gov.in",
    },

    {
        "keywords": ["mgnrega", "job card", "employment card"],
        "title": "MGNREGA Job Card",
        "details": "MGNREGA provides rural employment support to eligible families through job cards and wage-based work.",
        "benefits": [
            "Provides rural employment support",
            "Helps families get wage work",
            "Supports village development works",
            "Useful for low-income rural households",
        ],
        "documents": [
            "Aadhaar card",
            "Ration card if available",
            "Address proof",
            "Bank passbook",
            "Passport size photo",
        ],
        "eligibility": [
            "Rural households willing to do unskilled work can apply",
            "Applicant should be adult and eligible under scheme rules",
        ],
        "steps": [
            "Visit Gram Panchayat office.",
            "Ask for MGNREGA job card application.",
            "Submit family details and Aadhaar details.",
            "Attach bank account details and address proof.",
            "Submit passport size photos if required.",
            "Collect acknowledgement after application.",
            "After job card approval, request work when needed.",
            "Attend assigned work as per schedule.",
            "Check wage payment status regularly.",
            "Report delay in wage payment to Panchayat office.",
        ],
        "tips": [
            "Keep job card safely",
            "Check wage payment regularly",
            "Use bank account linked with correct details",
            "Ask Panchayat office for available work",
        ],
        "website": "https://nrega.nic.in",
    },

    {
        "keywords": ["bus pass", "student bus pass"],
        "title": "Bus Pass Service",
        "details": "This service helps students and citizens apply for bus passes for travel support.",
        "benefits": [
            "Reduces travel cost",
            "Helpful for students",
            "Useful for daily travel",
            "Supports education access",
        ],
        "documents": [
            "Student ID card if student",
            "Bonafide certificate if required",
            "Aadhaar card",
            "Passport size photo",
            "Mobile number",
        ],
        "eligibility": [
            "Students and eligible citizens can apply",
            "Student pass may require school or college proof",
        ],
        "steps": [
            "Open transport bus pass portal or visit bus pass counter.",
            "Choose student pass or general pass option.",
            "Fill name, route, institution, and travel details.",
            "Upload student ID or bonafide certificate if required.",
            "Upload photo and Aadhaar details.",
            "Check all details carefully.",
            "Submit application.",
            "Pay fee if required.",
            "Download pass or collect from counter after approval.",
            "Carry pass while travelling.",
        ],
        "tips": [
            "Use correct route details",
            "Renew pass before expiry",
            "Carry student ID while travelling",
            "Keep digital copy if available",
        ],
        "website": "https://online.tsrtcpass.in",
    },

    {
        "keywords": ["electricity", "current bill", "power bill"],
        "title": "Electricity Bill Payment",
        "details": "This service helps citizens check and pay electricity bills online.",
        "benefits": [
            "Saves time",
            "Avoids late payment fine",
            "Can download receipt",
            "Useful for monthly bill tracking",
        ],
        "documents": [
            "Electricity service number",
            "Mobile number",
            "Payment method",
        ],
        "eligibility": [
            "Any electricity consumer can use this service",
        ],
        "steps": [
            "Open electricity department website.",
            "Find bill payment option.",
            "Enter service number or consumer number.",
            "Check customer name and bill amount.",
            "Verify billing month and due date.",
            "Choose payment method.",
            "Pay bill online.",
            "Download or save receipt.",
            "Keep receipt until next bill is generated.",
        ],
        "tips": [
            "Pay before due date",
            "Check service number carefully",
            "Save payment receipt",
            "Use official electricity website only",
        ],
        "website": "https://www.tssouthernpower.com",
    },

    {
        "keywords": ["gas", "lpg", "gas connection"],
        "title": "LPG Gas Connection",
        "details": "This service helps citizens apply for new LPG gas connection, refill booking, and subsidy support.",
        "benefits": [
            "Helps get cooking gas connection",
            "Supports safe cooking",
            "Allows online refill booking",
            "Useful for subsidy benefits if eligible",
        ],
        "documents": [
            "Aadhaar card",
            "Address proof",
            "Bank passbook",
            "Passport size photo",
            "Mobile number",
        ],
        "eligibility": [
            "Eligible households can apply for LPG connection",
            "Applicant should provide address proof",
        ],
        "steps": [
            "Visit nearest gas agency or official LPG website.",
            "Choose new connection or refill booking option.",
            "Submit Aadhaar and address proof.",
            "Enter mobile number and bank details if required.",
            "Complete KYC verification.",
            "Pay connection charges if applicable.",
            "Collect gas book and safety information.",
            "Book cylinder refill online or through agency.",
            "Follow safety rules while using LPG cylinder.",
        ],
        "tips": [
            "Check gas pipe regularly",
            "Do not keep cylinder near fire",
            "Use authorized gas agency",
            "Keep emergency gas agency number",
        ],
        "website": "https://www.mylpg.in",
    },

    {
        "keywords": ["bank", "bank account", "loan"],
        "title": "Bank Account and Loan Guidance",
        "details": "This service guides citizens for opening bank accounts and understanding basic loan application process.",
        "benefits": [
            "Helps save money safely",
            "Useful for receiving scheme benefits",
            "Needed for scholarships and pensions",
            "Supports loan and financial services",
        ],
        "documents": [
            "Aadhaar card",
            "PAN card if available",
            "Passport size photo",
            "Address proof",
            "Mobile number",
        ],
        "eligibility": [
            "Any eligible citizen can open bank account",
            "Loan eligibility depends on bank rules and income",
        ],
        "steps": [
            "Visit nearest bank branch.",
            "Ask for savings account or loan application form.",
            "Fill personal details carefully.",
            "Submit Aadhaar, photo, and address proof.",
            "Give mobile number for SMS alerts.",
            "Complete KYC verification.",
            "Collect passbook, account number, and debit card if given.",
            "For loan, ask about eligibility and interest rate.",
            "Submit income or land documents if applying for loan.",
            "Track loan approval status with bank.",
        ],
        "tips": [
            "Keep passbook safely",
            "Do not share ATM PIN",
            "Use active mobile number",
            "Understand loan interest before applying",
        ],
        "website": "https://www.india.gov.in",
    },

    {
        "keywords": ["toilet", "toilet scheme", "swachh bharat"],
        "title": "Toilet Scheme",
        "details": "This service provides guidance for toilet construction support under sanitation schemes.",
        "benefits": [
            "Improves hygiene",
            "Supports household toilet construction",
            "Reduces open defecation",
            "Protects public health",
        ],
        "documents": [
            "Aadhaar card",
            "Address proof",
            "Bank passbook",
            "House details",
        ],
        "eligibility": [
            "Eligible rural households without toilet can apply",
        ],
        "steps": [
            "Visit village secretariat or Gram Panchayat office.",
            "Ask about toilet construction scheme.",
            "Check eligibility with local officer.",
            "Submit Aadhaar, address proof, and bank details.",
            "Fill application form.",
            "Wait for verification of household condition.",
            "After approval, construct toilet as per guidelines.",
            "Submit proof if required.",
            "Track payment or support status.",
        ],
        "tips": [
            "Use toilet regularly",
            "Keep toilet clean",
            "Do not submit fake details",
            "Ask local officer for scheme updates",
        ],
        "website": "https://swachhbharatmission.gov.in",
    },
    {
    "keywords": ["headache", "head pain", "migraine"],
    "title": "Headache Guidance",
    "details": "Headache may happen due to stress, dehydration, lack of sleep, eye strain, or illness.",
    "benefits": ["Basic headache care", "Helps identify warning signs", "Encourages timely doctor visit"],
    "documents": ["Health card if available", "Previous medical reports if available"],
    "eligibility": ["Anyone with headache can use this guidance"],
    "steps": [
        "Drink enough clean water.",
        "Rest in a quiet and comfortable place.",
        "Avoid bright light and loud noise.",
        "Reduce mobile or computer screen time.",
        "Eat food on time and avoid skipping meals.",
        "Check if headache is due to fever, stress, or lack of sleep.",
        "Visit doctor if headache is severe or repeated."
    ],
    "tips": ["Sleep properly", "Avoid stress", "Do not take random tablets"],
    "helpline": "Ambulance: 108",
    "website": "https://www.mohfw.gov.in",
},
{
    "keywords": ["stomach pain", "vomiting", "diarrhea", "loose motion"],
    "title": "Stomach Problem Guidance",
    "details": "Stomach problems may happen due to unsafe food, infection, indigestion, or dehydration.",
    "benefits": ["Basic stomach care", "Helps prevent dehydration", "Encourages doctor visit when needed"],
    "documents": ["Health card if available"],
    "eligibility": ["Anyone with stomach pain or vomiting can use this guidance"],
    "steps": [
        "Drink clean water.",
        "Eat light food like rice, curd, or soft food.",
        "Avoid oily and spicy food.",
        "Use ORS if loose motions or dehydration occur.",
        "Wash hands before eating.",
        "Avoid outside or unsafe food.",
        "Visit doctor if pain is severe or vomiting continues."
    ],
    "tips": ["Drink boiled water", "Maintain hygiene", "Do not ignore dehydration"],
    "helpline": "Ambulance: 108",
    "website": "https://www.mohfw.gov.in",
},
{
    "keywords": ["bp", "blood pressure", "high bp", "low bp"],
    "title": "Blood Pressure Guidance",
    "details": "Blood pressure problems need regular monitoring and medical advice.",
    "benefits": ["Health awareness", "Supports regular monitoring", "Encourages medical care"],
    "documents": ["BP readings if available", "Health card", "Previous medical reports"],
    "eligibility": ["People with high BP, low BP, dizziness, or weakness can use this guidance"],
    "steps": [
        "Check blood pressure using BP machine if available.",
        "Take rest in a calm place.",
        "Avoid too much salt if BP is high.",
        "Drink water and sit safely if feeling dizzy.",
        "Do not stop BP medicine without doctor advice.",
        "Maintain regular sleep and walking routine.",
        "Visit doctor for repeated high or low BP readings."
    ],
    "tips": ["Check BP regularly", "Avoid stress", "Follow doctor medicine schedule"],
    "helpline": "Ambulance: 108",
    "website": "https://www.mohfw.gov.in",
},
{
    "keywords": ["diabetes", "sugar", "blood sugar"],
    "title": "Diabetes Guidance",
    "details": "Diabetes needs food control, regular sugar checking, exercise, and doctor guidance.",
    "benefits": ["Diabetes awareness", "Helps manage sugar levels", "Encourages regular checkups"],
    "documents": ["Sugar test reports", "Health card", "Medicine details"],
    "eligibility": ["People with diabetes or high sugar symptoms can use this guidance"],
    "steps": [
        "Check blood sugar regularly.",
        "Avoid too much sweets and sugary drinks.",
        "Eat balanced food with vegetables and fiber.",
        "Walk or exercise regularly if doctor allows.",
        "Take medicines only as prescribed.",
        "Do not skip meals suddenly.",
        "Visit doctor regularly for checkups."
    ],
    "tips": ["Keep sugar reports safely", "Avoid self-medication", "Follow diet advice"],
    "helpline": "Ambulance: 108",
    "website": "https://www.mohfw.gov.in",
},
{
    "keywords": ["dengue", "malaria", "mosquito fever"],
    "title": "Mosquito-Borne Disease Guidance",
    "details": "Dengue and malaria can spread through mosquitoes and need quick medical attention.",
    "benefits": ["Prevention awareness", "Helps reduce mosquito breeding", "Encourages testing"],
    "documents": ["Fever records", "Blood test reports if available"],
    "eligibility": ["Anyone with fever, body pains, or mosquito-borne disease symptoms can use this guidance"],
    "steps": [
        "Avoid mosquito bites by using nets or repellents.",
        "Remove stagnant water near house.",
        "Keep water containers covered.",
        "Visit doctor if fever and body pains occur.",
        "Do blood test if doctor suggests.",
        "Drink enough fluids.",
        "Do not take random painkillers without doctor advice."
    ],
    "tips": ["Keep surroundings clean", "Use mosquito nets", "Report stagnant water"],
    "helpline": "Ambulance: 108",
    "website": "https://www.mohfw.gov.in",
},
    ]

if user_input.strip() == "":
    st.header(translate_text("Welcome to AI Village Help Portal", language))
    st.write(translate_text("Type your issue or service name in the sidebar search box.", language))

    st.write(translate_text("Examples:", language))
    examples = [
        "Aadhaar",
        "PAN Card",
        "Ration Card",
        "Income Certificate",
        "Farmer",
        "Crop Insurance",
        "Scholarship",
        "Fever",
        "Garbage",
        "Water Problem",
        "Women Safety",
        "Emergency",
        "Land Records",
        "MGNREGA",
        "Bus Pass",
    ]

    for example in examples:
        st.write("- " + translate_text(example, language))

    col1, col2, col3 = st.columns(3)
    col1.metric(translate_text("Services", language), "80+")
    col2.metric(translate_text("Government Support", language), translate_text("Available", language))
    col3.metric(translate_text("Village Help", language), "24/7")

else:
    query = user_input.lower().strip()
    found = False

    if ai_mode == "Local AI - Ollama":
        st.subheader("🤖 Local AI Response")
        answer = ask_ollama(user_input)
        st.write(translate_text(answer, language))
        st.stop()

    if ai_mode == "Online AI - BYOK":
        st.subheader("🤖 BYOK AI Response")
        answer = ask_byok_ai(user_input, api_key)
        st.write(translate_text(answer, language))
        st.stop()

    if ai_mode == "Google ADK Agent":
        st.subheader("🤖 Google ADK Agent Response")
        answer = ask_google_agent(user_input, api_key)
        st.write(translate_text(answer, language))
        st.stop()

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        for service in services:
            if any(keyword in query for keyword in service["keywords"]):
                found = True

                st.success(translate_text("Service Found Successfully", language))
                st.header(translate_text(service["title"], language))
                st.info(translate_text(service["details"], language))

                st.subheader(translate_text("🎯 Benefits", language))
                for benefit in service["benefits"]:
                    st.write("✅ " + translate_text(benefit, language))

                st.subheader(translate_text("📄 Required Documents", language))
                for document in service["documents"]:
                    st.write("📌 " + translate_text(document, language))

                st.subheader(translate_text("👨‍👩‍👧 Eligibility", language))
                for item in service["eligibility"]:
                    st.write("✔️ " + translate_text(item, language))

                st.subheader(translate_text("🪜 Detailed Step-by-Step Process", language))
                for index, step in enumerate(service["steps"], start=1):
                    st.write(f"{index}. " + translate_text(step, language))

                st.subheader(translate_text("💡 Important Tips", language))
                for tip in service["tips"]:
                    st.write("🔹 " + translate_text(tip, language))

                if "helpline" in service:
                    st.subheader(translate_text("📞 Helpline", language))
                    st.success(translate_text(service["helpline"], language))

                st.subheader(translate_text("🌐 Official Website", language))
                st.markdown(service["website"])

                break

        if not found:
            st.error(translate_text("Service not found.", language))
            st.write(
                translate_text(
                    "Try Aadhaar, PAN card, ration card, income certificate, farmer, crop insurance, scholarship, fever, garbage, water problem, women safety, land records, MGNREGA, bus pass, or emergency.",
                    language,
                )
            )
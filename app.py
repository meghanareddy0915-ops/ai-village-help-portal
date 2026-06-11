import streamlit as st
import pandas as pd
from datetime import datetime
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Village Help Portal", page_icon="🏡", layout="wide")

language_codes = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Odia": "or",
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

st.sidebar.title(translate_text("Services", language))
user_input = st.sidebar.text_input(
    translate_text("Type your problem or service", language),
    placeholder=translate_text(
        "Aadhaar, fever, crop insurance",
        language
    )
)

st.title("🏡 " + translate_text("AI Village Help Portal", language))
st.write(translate_text("A smart public service portal for village people.", language))

services = {
    "aadhaar": {
        "title": "Aadhaar Card",
        "details": "Aadhaar is used for identity verification, bank linking, SIM verification, and government schemes.",
        "steps": ["Visit nearest Aadhaar Seva Kendra or MeeSeva center.", "Carry identity proof and address proof.", "Apply for new Aadhaar or update details.", "Collect acknowledgement slip.", "Track Aadhaar status online."],
        "website": "https://uidai.gov.in"
    },
    "pan": {
        "title": "PAN Card",
        "details": "PAN is used for banking, tax filing, and financial services.",
        "steps": ["Open PAN application website.", "Fill personal details.", "Upload documents.", "Pay fee if required.", "Track PAN status online."],
        "website": "https://www.onlineservices.nsdl.com"
    },
    "ration": {
        "title": "Ration Card / Rice Card",
        "details": "Ration card helps families receive food grains and welfare benefits.",
        "steps": ["Visit MeeSeva or village secretariat.", "Submit family details.", "Attach Aadhaar, address proof, and income proof.", "Track application status."],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "income": {
        "title": "Income Certificate",
        "details": "Income certificate is useful for scholarships, schemes, and fee reimbursement.",
        "steps": ["Visit MeeSeva center.", "Fill application form.", "Upload required documents.", "Pay fee if required.", "Download certificate after approval."],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "caste": {
        "title": "Caste Certificate",
        "details": "Caste certificate is useful for education, scholarships, jobs, and reservations.",
        "steps": ["Visit MeeSeva center.", "Fill caste certificate application.", "Upload required documents.", "Submit application.", "Download certificate after approval."],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "pension": {
        "title": "Pension Services",
        "details": "Pension schemes support senior citizens, widows, and disabled persons.",
        "steps": ["Check eligibility.", "Collect Aadhaar, bank passbook, income certificate, and photo.", "Apply through MeeSeva or village secretariat.", "Track pension approval status."],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "voter": {
        "title": "Voter ID",
        "details": "Voter ID is used for voting and identity proof.",
        "steps": ["Visit voter service portal.", "Apply for new voter ID or correction.", "Upload age and address proof.", "Submit application.", "Track status online."],
        "website": "https://voters.eci.gov.in"
    },
    "farmer": {
        "title": "Farmer Support",
        "details": "Farmer support gives crop, fertilizer, pest, and farming guidance.",
        "steps": ["Check crop problem.", "Use organic compost.", "Avoid overwatering.", "Take crop photo if disease appears.", "Contact agriculture officer if issue continues."],
        "website": "https://agricoop.gov.in"
    },
    "crop insurance": {
        "title": "Crop Insurance",
        "details": "Crop insurance helps farmers during crop loss due to natural problems.",
        "steps": ["Open PMFBY website.", "Submit farmer details.", "Enter crop and land details.", "Track claim status online."],
        "website": "https://pmfby.gov.in"
    },
    "pm kisan": {
        "title": "PM-KISAN Scheme",
        "details": "PM-KISAN provides financial support to eligible farmers.",
        "steps": ["Open PM-KISAN website.", "Check eligibility.", "Enter Aadhaar and land details.", "Submit bank account details.", "Track beneficiary status."],
        "website": "https://pmkisan.gov.in"
    },
    "fever": {
        "title": "Fever Guidance",
        "details": "Fever may happen due to infection, heat, or seasonal illness.",
        "steps": ["Drink plenty of water.", "Take rest.", "Wear light clothes.", "Check temperature.", "Visit doctor if fever continues."],
        "website": "https://www.mohfw.gov.in"
    },
    "cough": {
        "title": "Cough Guidance",
        "details": "Cough may happen due to cold, dust, allergy, or infection.",
        "steps": ["Drink warm water.", "Avoid cold drinks.", "Avoid dust and smoke.", "Use steam carefully.", "Visit doctor if cough continues."],
        "website": "https://www.mohfw.gov.in"
    },
    "headache": {
        "title": "Headache Guidance",
        "details": "Headache may happen due to stress, dehydration, lack of sleep, or screen usage.",
        "steps": ["Drink water.", "Rest in a quiet place.", "Reduce screen time.", "Sleep properly.", "Visit doctor if severe."],
        "website": "https://www.mohfw.gov.in"
    },
    "stomach pain": {
        "title": "Stomach Pain Guidance",
        "details": "Stomach pain may happen due to gas, indigestion, unsafe food, or infection.",
        "steps": ["Drink clean water.", "Eat light food.", "Avoid oily food.", "Take rest.", "Visit doctor if pain is severe."],
        "website": "https://www.mohfw.gov.in"
    },
    "scholarship": {
        "title": "Education & Scholarships",
        "details": "Scholarships help students get financial support for education.",
        "steps": ["Check eligibility.", "Collect Aadhaar, income certificate, marks memo, and bank details.", "Register online.", "Submit application.", "Track status."],
        "website": "https://scholarships.gov.in"
    },
    "job": {
        "title": "Jobs & Skills",
        "details": "This helps youth find jobs and skill development programs.",
        "steps": ["Register on job portal.", "Create profile.", "Add education and skills.", "Search jobs or training.", "Apply for opportunities."],
        "website": "https://www.ncs.gov.in"
    },
    "electricity": {
        "title": "Electricity Bill Payment",
        "details": "Citizens can check and pay electricity bills online.",
        "steps": ["Open electricity website.", "Enter service number.", "Check bill amount.", "Pay online.", "Save receipt."],
        "website": "https://www.tssouthernpower.com"
    },
    "passport": {
        "title": "Passport Service",
        "details": "Citizens can apply for passport or passport renewal.",
        "steps": ["Open Passport Seva website.", "Register or login.", "Fill application form.", "Book appointment.", "Visit passport office with documents."],
        "website": "https://www.passportindia.gov.in"
    },
    "driving licence": {
        "title": "Driving Licence",
        "details": "Citizens can apply for learner licence or driving licence.",
        "steps": ["Open Parivahan portal.", "Fill application form.", "Upload documents.", "Book test slot.", "Attend test."],
        "website": "https://parivahan.gov.in"
    },
    "complaint": {
        "title": "Public Complaint",
        "details": "Citizens can report garbage, road, water, drainage, and streetlight problems.",
        "steps": ["Enter name and village.", "Select complaint type.", "Upload photo if available.", "Submit complaint.", "Track complaint status."],
        "website": "https://pgportal.gov.in"
    },
    "garbage": {
        "title": "Garbage Complaint",
        "details": "Citizens can report garbage collection or cleanliness problems.",
        "steps": ["Note exact location.", "Take photo if available.", "Submit complaint.", "Follow up with local office."],
        "website": "https://pgportal.gov.in"
    },
    "emergency": {
        "title": "Emergency Contacts",
        "details": "Important emergency numbers for public safety.",
        "steps": ["Police: 100", "Ambulance: 108", "Fire Service: 101", "Women Helpline: 181", "Child Helpline: 1098"],
        "website": "https://112.gov.in"
    },
}

if user_input == "":
    st.header(translate_text("Welcome to AI Village Help Portal", language))
    st.write(translate_text("Type your issue or service name in the sidebar search box.", language))

    examples = [
    "Aadhaar",
    "Fever",
    "Farmer",
    "Crop Insurance",
    "Scholarship",
    "Complaint",
    "Passport"
]

st.write(translate_text("Examples:", language))

for example in examples:
    st.write("- " + translate_text(example, language))

    col1, col2, col3 = st.columns(3)
    col1.metric(translate_text("Services", language), "45+")
    col2.metric(translate_text("Government Support", language), translate_text("Available", language))
    col3.metric(translate_text("Village Help", language), "24/7")

else:
    query = user_input.lower().strip()
    found = False

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        for key, value in services.items():
            if query == key:
                found = True

                st.success(translate_text("Service Found Successfully", language))
                st.header(translate_text(value["title"], language))
                st.info(translate_text(value["details"], language))

                st.subheader(translate_text("✅ Steps", language))
                for step in value["steps"]:
                    st.write("• " + translate_text(step, language))

                st.subheader(translate_text("🌐 Website", language))
                st.markdown(value["website"])

                break

        if not found:
            st.error(translate_text("Service not found.", language))
            st.write(
                translate_text(
                    "Please type exact service name like aadhaar, pan, fever, farmer, complaint, passport, or job.",
                    language
                )
            )

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        for key, value in services.items():
            if query in key:
                found = True
                st.success(translate_text("Service Found Successfully", language))
                st.header(translate_text(value["title"], language))
                st.info(translate_text(value["details"], language))

                st.subheader(translate_text("✅ Steps", language))
                for step in value["steps"]:
                    st.write("• " + translate_text(step, language))

                st.subheader(translate_text("🌐 Website", language))
                st.markdown(value["website"])

        if not found:
            st.error(translate_text("Service not found.", language))
            st.write(translate_text("Try Aadhaar, fever, farmer, crop insurance, scholarship, complaint, passport, or job.", language))
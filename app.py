import streamlit as st

st.set_page_config(page_title="AI Village Help Portal", layout="wide")

# =========================
# PAGE TITLE
# =========================

st.title("🏡 AI Village Help Portal")
st.write("A smart public service portal for village people.")

# =========================
# SERVICES DATA
# =========================

all_services = {

    "aadhaar card": {
        "title": "Aadhaar Card",
        "details": "Aadhaar is used for identity verification, bank linking, SIM verification, and government schemes.",
        "steps": [
            "Visit nearest Aadhaar Seva Kendra or MeeSeva center.",
            "Carry identity proof and address proof.",
            "Apply for new Aadhaar or update details.",
            "Give biometrics if required.",
            "Collect acknowledgement slip.",
            "Track Aadhaar status online."
        ],
        "website": "https://uidai.gov.in"
    },

    "pan card": {
        "title": "PAN Card",
        "details": "PAN card is used for banking, tax filing, and financial services.",
        "steps": [
            "Visit PAN card official website.",
            "Fill PAN application form.",
            "Upload Aadhaar and photo.",
            "Pay application fee.",
            "Submit application.",
            "Track PAN status online."
        ],
        "website": "https://www.onlineservices.nsdl.com"
    },

    "ration card": {
        "title": "Ration Card",
        "details": "Ration card helps families get subsidized food items.",
        "steps": [
            "Visit MeeSeva or ration office.",
            "Carry Aadhaar and income proof.",
            "Submit family details.",
            "Apply for new ration card.",
            "Track application status."
        ],
        "website": "https://epds.telangana.gov.in"
    },

    "income certificate": {
        "title": "Income Certificate",
        "details": "Income certificate is required for scholarships and welfare schemes.",
        "steps": [
            "Visit MeeSeva center.",
            "Submit Aadhaar and income proof.",
            "Fill certificate application form.",
            "Pay required fee.",
            "Collect certificate after approval."
        ],
        "website": "https://tg.meeseva.gov.in"
    },

    "caste certificate": {
        "title": "Caste Certificate",
        "details": "Caste certificate is used for reservations and government benefits.",
        "steps": [
            "Visit MeeSeva center.",
            "Submit Aadhaar and family documents.",
            "Fill caste certificate application.",
            "Submit required proofs.",
            "Collect certificate after approval."
        ],
        "website": "https://tg.meeseva.gov.in"
    },

    "birth certificate": {
        "title": "Birth Certificate",
        "details": "Birth certificate is an official proof of birth.",
        "steps": [
            "Visit municipality office or MeeSeva.",
            "Submit hospital details.",
            "Fill birth registration form.",
            "Verify parent details.",
            "Download or collect certificate."
        ],
        "website": "https://crsorgi.gov.in"
    },

    "farmer support": {
        "title": "Farmer Support",
        "details": "Guidance for crops, fertilizers, and farming support.",
        "steps": [
            "Select crop type.",
            "Check fertilizer suggestions.",
            "Read seasonal farming advice.",
            "Use crop disease guidance.",
            "Contact agriculture officer if needed."
        ],
        "website": "https://farmer.gov.in"
    },

    "crop insurance": {
        "title": "Crop Insurance",
        "details": "Insurance support for crop damage due to natural disasters.",
        "steps": [
            "Open PMFBY website.",
            "Register farmer details.",
            "Enter crop and land details.",
            "Submit bank account information.",
            "Track claim status online."
        ],
        "website": "https://pmfby.gov.in"
    },

    "pm kisan": {
        "title": "PM Kisan Scheme",
        "details": "Financial support scheme for eligible farmers.",
        "steps": [
            "Visit PM Kisan website.",
            "Check eligibility.",
            "Enter Aadhaar details.",
            "Submit land details.",
            "Track beneficiary status."
        ],
        "website": "https://pmkisan.gov.in"
    },

    "health guidance": {
        "title": "Health Guidance",
        "details": "Basic health support and awareness for common problems.",
        "steps": [
            "Type health issue in search.",
            "Read prevention methods.",
            "Check home care tips.",
            "Visit nearest hospital if symptoms continue.",
            "Call emergency services if needed."
        ],
        "website": "https://www.nhp.gov.in"
    },

    "fever": {
        "title": "Fever Guidance",
        "details": "Guidance for fever reduction and care.",
        "steps": [
            "Drink plenty of water.",
            "Take proper rest.",
            "Eat light food.",
            "Check temperature regularly.",
            "Visit doctor if fever continues."
        ],
        "website": "https://www.nhp.gov.in"
    },

    "cough": {
        "title": "Cough Guidance",
        "details": "Guidance for reducing cough problems.",
        "steps": [
            "Drink warm water.",
            "Avoid cold food.",
            "Take steam inhalation.",
            "Use doctor prescribed medicine.",
            "Visit hospital if cough continues."
        ],
        "website": "https://www.nhp.gov.in"
    },

    "headache": {
        "title": "Headache Guidance",
        "details": "Guidance for headache relief.",
        "steps": [
            "Take proper rest.",
            "Drink enough water.",
            "Avoid stress.",
            "Sleep properly.",
            "Visit doctor if pain continues."
        ],
        "website": "https://www.nhp.gov.in"
    },

    "stomach pain": {
        "title": "Stomach Pain Guidance",
        "details": "Guidance for stomach pain reduction.",
        "steps": [
            "Drink clean water.",
            "Avoid oily food.",
            "Eat light meals.",
            "Take rest.",
            "Visit doctor if pain becomes severe."
        ],
        "website": "https://www.nhp.gov.in"
    },

    "complaint": {
        "title": "Public Complaint",
        "details": "Citizens can report garbage, water, roads, and streetlight problems.",
        "steps": [
            "Select complaint type.",
            "Enter village/location details.",
            "Upload photo if available.",
            "Submit complaint.",
            "Track complaint status."
        ],
        "website": "https://pgportal.gov.in"
    },

    "streetlight": {
        "title": "Streetlight Complaint",
        "details": "Report damaged or non-working streetlights.",
        "steps": [
            "Enter streetlight location.",
            "Upload image if possible.",
            "Submit complaint.",
            "Track complaint online."
        ],
        "website": "https://pgportal.gov.in"
    },

    "water problem": {
        "title": "Water Supply Complaint",
        "details": "Report drinking water or water supply problems.",
        "steps": [
            "Enter village details.",
            "Describe water issue.",
            "Submit complaint.",
            "Track complaint status."
        ],
        "website": "https://pgportal.gov.in"
    },

    "road issue": {
        "title": "Road Issue Complaint",
        "details": "Citizens can report damaged roads and potholes.",
        "steps": [
            "Take photo of damaged road.",
            "Enter location details.",
            "Submit complaint.",
            "Track complaint online."
        ],
        "website": "https://pgportal.gov.in"
    },

    "electricity bill": {
        "title": "Electricity Bill Payment",
        "details": "Citizens can check and pay electricity bills online.",
        "steps": [
            "Open electricity department website.",
            "Enter service number.",
            "Check bill amount.",
            "Pay online.",
            "Download receipt."
        ],
        "website": "https://www.tssouthernpower.com"
    },

    "gas connection": {
        "title": "Gas Connection",
        "details": "Apply for new LPG gas connection or refill booking.",
        "steps": [
            "Visit LPG website or gas agency.",
            "Submit Aadhaar and address proof.",
            "Apply for connection.",
            "Complete verification.",
            "Receive gas connection."
        ],
        "website": "https://www.mylpg.in"
    },

    "passport": {
        "title": "Passport Service",
        "details": "Apply for new passport or passport renewal.",
        "steps": [
            "Visit Passport Seva website.",
            "Register account.",
            "Fill passport application.",
            "Book appointment.",
            "Visit passport office."
        ],
        "website": "https://www.passportindia.gov.in"
    },

    "driving licence": {
        "title": "Driving Licence",
        "details": "Apply for learner or driving licence.",
        "steps": [
            "Visit Parivahan website.",
            "Fill driving licence form.",
            "Upload documents.",
            "Book test slot.",
            "Attend driving test."
        ],
        "website": "https://parivahan.gov.in"
    },

    "jobs": {
        "title": "Jobs and Skill Training",
        "details": "Information about jobs and skill development programs.",
        "steps": [
            "Visit employment portal.",
            "Search available jobs.",
            "Apply for skill training.",
            "Attend training program.",
            "Apply for jobs."
        ],
        "website": "https://www.ncs.gov.in"
    },

    "education": {
        "title": "Scholarships and Education",
        "details": "Students can apply for scholarships and educational schemes.",
        "steps": [
            "Visit scholarship portal.",
            "Check eligibility.",
            "Upload student documents.",
            "Submit application.",
            "Track scholarship status."
        ],
        "website": "https://scholarships.gov.in"
    },

    "emergency": {
        "title": "Emergency Contacts",
        "details": "Emergency contact numbers for public safety.",
        "steps": [
            "Police: 100",
            "Ambulance: 108",
            "Fire Service: 101",
            "Women Helpline: 181"
        ],
        "website": "https://www.india.gov.in"
    }
}

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Services")

user_input = st.sidebar.text_input(
    "Type your problem or service",
    placeholder="Example: Aadhaar, fever, crop insurance"
)

# =========================
# HOME PAGE
# =========================

if user_input == "":

    st.header("Welcome to AI Village Help Portal")

    st.write("""
This project helps villagers access important services easily.
Type your issue or service name in the sidebar search box.

Examples:
- Aadhaar Card
- PAN Card
- Fever
- Farmer Support
- Complaint
- Crop Insurance
- Jobs
- Education
""")

    col1, col2, col3 = st.columns(3)

    col1.metric("Services", "45+")
    col2.metric("Government Support", "Available")
    col3.metric("Village Help", "24/7")

# =========================
# SEARCH SERVICE
# =========================

# =========================
# SEARCH SERVICE
# =========================

else:

    query = user_input.lower().strip()

    found = False

    st.markdown("---")

    col1, col2, col3 = st.columns([1,4,1])

    with col2:

        for key, value in all_services.items():

            if query in key:

                found = True

                st.success("Service Found Successfully")

                st.header(f"📌 {value['title']}")

                st.info(value["details"])

                st.subheader("✅ Steps To Follow")

                step_no = 1

                for step in value["steps"]:
                    st.write(f"{step_no}. {step}")
                    step_no += 1

                st.subheader("🌐 Official Website")

                st.markdown(
                    f"""
                    <a href="{value['website']}" target="_blank">
                        Open Website
                    </a>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("---")

        if not found:

            st.error("❌ Service Not Found")

            st.subheader("Try Searching Like:")

            st.write("• Aadhaar")
            st.write("• PAN Card")
            st.write("• Fever")
            st.write("• Farmer Support")
            st.write("• Crop Insurance")
            st.write("• Complaint")
            st.write("• Jobs")
            st.write("• Passport")
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AI Village Help Portal",
    page_icon="🏡",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(90deg, #2E8B57, #1E90FF);
    padding: 30px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.card {
    background-color: #f7f9fc;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #2E8B57;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 18px;
    min-height: 150px;
}
.small-card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e6e6e6;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.06);
    margin-bottom: 15px;
}
.footer {
    text-align: center;
    padding: 18px;
    color: gray;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>🏡 AI Village Help Portal</h1>
    <p>Smart Digital Public Service Support for Rural Citizens</p>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Choose Service",
    [
        "Home",
        "Ask Any Service",
        "Complaint Reporting",
        "Emergency Contacts"
    ]
)

# ---------------- DATA ----------------
all_services = {
    "aadhaar": {
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
    "aadhar": {
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
    "pan": {
        "title": "PAN Card",
        "details": "PAN is useful for bank accounts, tax services, scholarships, and financial work.",
        "steps": [
            "Open PAN application website.",
            "Fill personal details.",
            "Upload documents.",
            "Pay fee if required.",
            "Submit application.",
            "Track PAN status online."
        ],
        "website": "https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html"
    },
    "ration": {
        "title": "Ration Card / Rice Card",
        "details": "Ration card helps families receive food grains and welfare benefits.",
        "steps": [
            "Visit MeeSeva or village secretariat.",
            "Submit family details.",
            "Attach Aadhaar, address proof, and income proof.",
            "Submit application.",
            "Track application status."
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "rice card": {
        "title": "Ration Card / Rice Card",
        "details": "Rice card helps eligible families receive food grains and welfare benefits.",
        "steps": [
            "Visit MeeSeva or village secretariat.",
            "Submit family details.",
            "Attach Aadhaar, address proof, and income proof.",
            "Submit application.",
            "Track application status."
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "income": {
        "title": "Income Certificate",
        "details": "Income certificate is useful for scholarships, schemes, and fee reimbursement.",
        "steps": [
            "Visit MeeSeva portal or MeeSeva center.",
            "Select income certificate service.",
            "Fill application form.",
            "Upload required documents.",
            "Pay fee if required.",
            "Download certificate after approval."
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "caste": {
        "title": "Caste Certificate",
        "details": "Caste certificate is useful for education, scholarships, jobs, and reservations.",
        "steps": [
            "Visit MeeSeva portal or MeeSeva center.",
            "Select caste certificate service.",
            "Fill application form.",
            "Upload required documents.",
            "Submit application.",
            "Download certificate after approval."
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "residence": {
        "title": "Residence Certificate",
        "details": "Residence certificate is used as proof of address.",
        "steps": [
            "Visit MeeSeva portal.",
            "Select residence certificate.",
            "Fill address details.",
            "Upload address proof.",
            "Submit application.",
            "Track status online."
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "birth": {
        "title": "Birth Certificate",
        "details": "Birth certificate is official proof of date and place of birth.",
        "steps": [
            "Visit municipal office or MeeSeva.",
            "Fill birth certificate application.",
            "Upload hospital record if available.",
            "Submit parent details.",
            "Download certificate after approval."
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "pension": {
        "title": "Pension Services",
        "details": "Pension schemes support senior citizens, widows, and disabled persons.",
        "steps": [
            "Check eligibility.",
            "Collect Aadhaar, bank passbook, income certificate, and photo.",
            "Apply through MeeSeva or village secretariat.",
            "Submit documents.",
            "Track pension approval status."
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/"
    },
    "voter": {
        "title": "Voter ID",
        "details": "Voter ID is used for voting and identity proof.",
        "steps": [
            "Visit voter service portal.",
            "Apply for new voter ID or correction.",
            "Upload age and address proof.",
            "Submit application.",
            "Track status online."
        ],
        "website": "https://voters.eci.gov.in"
    },
    "scheme": {
        "title": "Government Schemes",
        "details": "Citizens can search schemes based on age, income, occupation, and category.",
        "steps": [
            "Search suitable scheme.",
            "Check eligibility.",
            "Collect required documents.",
            "Apply online or through MeeSeva or village office.",
            "Track application status."
        ],
        "website": "https://www.india.gov.in"
    },
    "yellow leaves": {
        "title": "Farmer Help - Yellow Leaves",
        "details": "Yellow leaves may happen due to nutrient deficiency, overwatering, poor soil, or disease.",
        "steps": [
            "Check whether soil is too dry or too wet.",
            "Use organic compost.",
            "Avoid overwatering.",
            "Do soil testing if possible.",
            "Contact agriculture officer if yellowing spreads."
        ],
        "website": "https://agricoop.gov.in"
    },
    "pest": {
        "title": "Farmer Help - Pest Attack",
        "details": "Pests may damage leaves, stems, flowers, or fruits.",
        "steps": [
            "Check plant leaves and stems carefully.",
            "Take a clear photo of affected crop.",
            "Remove heavily affected leaves if possible.",
            "Do not use random pesticide without advice.",
            "Contact agriculture officer."
        ],
        "website": "https://agricoop.gov.in"
    },
    "leaf spot": {
        "title": "Farmer Help - Leaf Spot",
        "details": "Leaf spots may happen due to fungal or bacterial infection.",
        "steps": [
            "Avoid watering directly on leaves.",
            "Remove infected leaves carefully.",
            "Keep spacing between plants.",
            "Avoid overcrowding.",
            "Consult agriculture officer if spots increase."
        ],
        "website": "https://agricoop.gov.in"
    },
    "fertilizer": {
        "title": "Farmer Help - Fertilizer Guidance",
        "details": "Wrong fertilizer usage can damage crop growth.",
        "steps": [
            "Use fertilizer based on crop stage.",
            "Do soil testing before applying fertilizer.",
            "Avoid too much chemical fertilizer.",
            "Use compost.",
            "Ask agriculture officer for crop-specific dosage."
        ],
        "website": "https://agricoop.gov.in"
    },
    "crop disease": {
        "title": "Farmer Help - Crop Disease",
        "details": "Crop disease may happen due to fungus, bacteria, virus, pests, or weather conditions.",
        "steps": [
            "Take a clear photo of affected crop.",
            "Separate affected plants if possible.",
            "Avoid using random medicines.",
            "Check whether leaves, stem, or fruits are affected.",
            "Contact agriculture department for exact disease identification."
        ],
        "website": "https://agricoop.gov.in"
    },
    "fever": {
        "title": "Health Support - Fever",
        "details": "Fever may happen due to infection, heat, or seasonal illness.",
        "steps": [
            "Drink plenty of water.",
            "Take proper rest.",
            "Wear light clothes.",
            "Use wet cloth on forehead if temperature is high.",
            "Visit doctor if fever continues more than 2 days."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "headache": {
        "title": "Health Support - Headache",
        "details": "Headache may happen due to stress, dehydration, lack of sleep, or screen usage.",
        "steps": [
            "Drink enough water.",
            "Rest in a quiet place.",
            "Reduce mobile or laptop screen time.",
            "Sleep properly.",
            "Visit doctor if severe."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "cough": {
        "title": "Health Support - Cough",
        "details": "Cough may happen due to cold, dust, allergy, or infection.",
        "steps": [
            "Drink warm water.",
            "Avoid cold drinks.",
            "Avoid dust and smoke.",
            "Use steam carefully.",
            "Visit doctor if cough continues more than one week."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "cold": {
        "title": "Health Support - Cold",
        "details": "Cold usually improves with rest and fluids.",
        "steps": [
            "Drink warm water.",
            "Take rest.",
            "Avoid cold food and drinks.",
            "Keep yourself warm.",
            "Maintain hygiene."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "stomach pain": {
        "title": "Health Support - Stomach Pain",
        "details": "Stomach pain may happen due to gas, indigestion, unsafe food, or infection.",
        "steps": [
            "Drink clean water.",
            "Eat light food.",
            "Avoid oily and outside food.",
            "Take rest.",
            "Visit doctor if pain is severe."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "vomiting": {
        "title": "Health Support - Vomiting",
        "details": "Vomiting can cause dehydration.",
        "steps": [
            "Drink small sips of water or ORS.",
            "Avoid spicy and oily food.",
            "Take rest.",
            "Eat light food after vomiting reduces.",
            "Visit doctor if vomiting continues."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "diarrhea": {
        "title": "Health Support - Diarrhea",
        "details": "Loose motions can cause dehydration.",
        "steps": [
            "Drink ORS or clean water.",
            "Eat simple food.",
            "Avoid outside food.",
            "Maintain hygiene.",
            "Visit doctor if weakness or blood in stool appears."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "tooth pain": {
        "title": "Health Support - Tooth Pain",
        "details": "Tooth pain may happen due to cavity, gum problem, or infection.",
        "steps": [
            "Rinse mouth with clean warm water.",
            "Avoid very cold or very hot foods.",
            "Keep mouth clean.",
            "Do not put unknown powders or chemicals.",
            "Visit dentist if pain continues."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "burn": {
        "title": "Health Support - Burn First Aid",
        "details": "Burns need careful first aid.",
        "steps": [
            "Keep burned area under cool running water for some time.",
            "Do not apply toothpaste, oil, or unknown creams.",
            "Cover with clean cloth.",
            "Visit doctor if burn is large or severe."
        ],
        "website": "https://www.mohfw.gov.in"
    },
    "scholarship": {
        "title": "Education & Scholarships",
        "details": "Scholarships help students get financial support for education.",
        "steps": [
            "Check scholarship eligibility.",
            "Collect Aadhaar, income certificate, marks memo, and bank details.",
            "Register online.",
            "Fill scholarship application.",
            "Upload documents.",
            "Submit and track status."
        ],
        "website": "https://scholarships.gov.in"
    },
    "job": {
        "title": "Jobs & Skills",
        "details": "This helps youth find job and skill development information.",
        "steps": [
            "Register on job portal.",
            "Create profile.",
            "Add education and skills.",
            "Search jobs or training.",
            "Apply for suitable opportunities."
        ],
        "website": "https://www.ncs.gov.in"
    },
    "skill": {
        "title": "Skill Development",
        "details": "Skill training helps youth improve employability.",
        "steps": [
            "Open Skill India portal.",
            "Choose training course.",
            "Register with basic details.",
            "Attend training.",
            "Apply for jobs after completion."
        ],
        "website": "https://www.skillindiadigital.gov.in"
    },
    "garbage": {
        "title": "Complaint - Garbage Issue",
        "details": "Citizens can report garbage issues in their area.",
        "steps": [
            "Go to Complaint Reporting section.",
            "Enter name and village.",
            "Select Garbage Issue.",
            "Upload photo if available.",
            "Submit complaint."
        ],
        "website": "https://pgportal.gov.in"
    },
    "road": {
        "title": "Complaint - Road Damage",
        "details": "Citizens can report road damage or potholes.",
        "steps": [
            "Go to Complaint Reporting section.",
            "Enter location details.",
            "Select Road Damage.",
            "Upload road photo.",
            "Submit complaint."
        ],
        "website": "https://pgportal.gov.in"
    },
    "water": {
        "title": "Complaint - Water Problem",
        "details": "Citizens can report water leakage or drinking water issues.",
        "steps": [
            "Go to Complaint Reporting section.",
            "Enter village and issue details.",
            "Select Water Problem.",
            "Upload photo if available.",
            "Submit complaint."
        ],
        "website": "https://pgportal.gov.in"
    },
    "emergency": {
        "title": "Emergency Contacts",
        "details": "Important emergency numbers for quick help.",
        "steps": [
            "Police: 100",
            "Ambulance: 108",
            "Fire Service: 101",
            "Women Helpline: 1091",
            "Child Helpline: 1098",
            "Disaster Management: 1078"
        ],
        "website": "https://112.gov.in"
    }
}

# ---------------- HOME ----------------
if menu == "Home":
    st.markdown("## 🌍 Welcome to AI Village Help Portal")
    st.write(
        "A one-stop digital platform that helps villagers access government services, "
        "health guidance, farmer support, education help, jobs, complaints, and emergency contacts."
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Services", "30+")
    col2.metric("Complaint Types", "7")
    col3.metric("Guidance Areas", "25+")
    col4.metric("Emergency Contacts", "6")

    st.markdown("### 🚀 Main Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>🤖 Ask Any Service</h3>
        <p>Type questions about Aadhaar, PAN, certificates, health, farming, jobs, complaints and more.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>🌾 Farmer Help</h3>
        <p>Get crop guidance for pests, yellow leaves, fertilizer, leaf spots and crop diseases.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h3>🏥 Health Support</h3>
        <p>Basic awareness for fever, cough, headache, stomach pain, burns and tooth pain.</p>
        </div>
        """, unsafe_allow_html=True)

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown("""
        <div class="card">
        <h3>📝 Complaint Reporting</h3>
        <p>Report garbage, road, water, streetlight, drainage and electricity problems.</p>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class="card">
        <h3>🎓 Education Help</h3>
        <p>Scholarship guidance and education support for rural students.</p>
        </div>
        """, unsafe_allow_html=True)

    with c6:
        st.markdown("""
        <div class="card">
        <h3>💼 Jobs & Skills</h3>
        <p>Skill training and job portal guidance for rural youth.</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("Use the Ask Any Service section to type your question and get guidance.")


# ---------------- ASK ANY SERVICE ----------------
elif menu == "Ask Any Service":
    st.header("🤖 Ask Any Village Service")

    st.write("Type any question about government services, farming, health, education, jobs, complaints, or emergency help.")

    query = st.text_input(
        "Type your question",
        placeholder="Example: I want Aadhaar / fever / yellow leaves / scholarship / garbage complaint"
    )

    if st.button("Get Answer"):
        q = query.lower().strip()
        found = False

        for keyword, data in all_services.items():
            if keyword in q:
                st.subheader(data["title"])
                st.info(data["details"])

                st.markdown("### ✅ Steps / Guidance")
                for step in data["steps"]:
                    st.write(f"- {step}")

                st.markdown("### 🌐 Website")
                st.write(data["website"])

                found = True
                break

        if not found:
            st.warning("I could not find exact guidance for this question.")
            st.write(
                "Try asking about Aadhaar, PAN, ration card, income certificate, farmer crop problem, "
                "fever, cough, scholarship, job, garbage, road, water, or emergency."
            )


# ---------------- COMPLAINT REPORTING ----------------
elif menu == "Complaint Reporting":
    st.header("📝 Public Complaint Reporting")

    name = st.text_input("Citizen Name")
    village = st.text_input("Village Name")
    complaint_type = st.selectbox(
        "Complaint Type",
        [
            "Garbage Issue",
            "Road Damage",
            "Water Problem",
            "Streetlight Issue",
            "Drainage Problem",
            "Electricity Problem",
            "Other"
        ]
    )
    details = st.text_area("Complaint Details")
    image = st.file_uploader("Upload Complaint Image", type=["jpg", "jpeg", "png"])

    if image:
        st.image(image, caption="Uploaded Complaint Image", use_container_width=True)

    if st.button("Submit Complaint"):
        if name and village and details:
            data = {
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Village": village,
                "Complaint Type": complaint_type,
                "Details": details,
                "Status": "Submitted"
            }

            df = pd.DataFrame([data])

            try:
                old = pd.read_csv("complaints.csv")
                final = pd.concat([old, df], ignore_index=True)
                final.to_csv("complaints.csv", index=False)
            except FileNotFoundError:
                df.to_csv("complaints.csv", index=False)

            st.success("Complaint submitted successfully.")
            st.info("Website for public grievance: https://pgportal.gov.in")
        else:
            st.error("Please fill all required details.")

    st.subheader("Submitted Complaints")

    try:
        complaints = pd.read_csv("complaints.csv")
        st.dataframe(complaints)

        status_counts = complaints["Status"].value_counts()
        st.bar_chart(status_counts)
    except FileNotFoundError:
        st.write("No complaints submitted yet.")


# ---------------- EMERGENCY ----------------
elif menu == "Emergency Contacts":
    st.header("🚨 Emergency Contacts")

    contacts = {
        "Police": "100",
        "Ambulance": "108",
        "Fire Service": "101",
        "Women Helpline": "1091",
        "Child Helpline": "1098",
        "Disaster Management": "1078"
    }

    for service_name, number in contacts.items():
        st.markdown(
            f"""
            <div class="small-card">
            <h4>{service_name}</h4>
            <p><b>{number}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<div class="footer">
    <p>AI Village Help Portal | Built using Python & Streamlit | Public Service Project</p>
</div>
""", unsafe_allow_html=True)
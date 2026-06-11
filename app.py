import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AI Village Help Portal",
    page_icon="🏡",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .hero {
        background: linear-gradient(90deg, #2E8B57, #1E90FF);
        padding: 30px;
        border-radius: 18px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .hero p {
        font-size: 18px;
    }

    .card {
        background-color: #f7f9fc;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #2E8B57;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
        margin-bottom: 18px;
        min-height: 160px;
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
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <div class="hero">
        <h1>🏡 AI Village Help Portal</h1>
        <p>Smart Digital Public Service Support for Rural Citizens</p>
    </div>
    """,
    unsafe_allow_html=True
)

menu = st.sidebar.selectbox(
    "Choose Service",
    [
        "Home",
        "Government Services",
        "Farmer Help",
        "Health Support",
        "Complaint Reporting",
        "Education & Scholarships",
        "Jobs & Skills",
        "Emergency Contacts",
        "AI Help Assistant"
    ]
)


# ---------------- HOME ----------------
if menu == "Home":
    st.markdown("## 🌍 Welcome to AI Village Help Portal")
    st.write(
        "A one-stop digital platform that helps villagers access government services, "
        "health guidance, farmer support, education help, jobs, complaints, and emergency contacts."
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Services", "8+")
    col2.metric("Complaint Types", "7")
    col3.metric("Guidance Areas", "25+")
    col4.metric("Emergency Contacts", "6")

    st.markdown("### 🚀 Main Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="card">
            <h3>🏛️ Government Services</h3>
            <p>Aadhaar, PAN, ration card, certificates, pension, voter ID and schemes.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="card">
            <h3>🌾 Farmer Help</h3>
            <p>Crop guidance, pest help, fertilizer advice, water issues and crop disease tips.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="card">
            <h3>🏥 Health Support</h3>
            <p>Basic awareness for fever, cough, headache, stomach pain, injuries and pregnancy care.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown(
            """
            <div class="card">
            <h3>📝 Complaint Reporting</h3>
            <p>Report garbage, road, water, streetlight, drainage and electricity problems.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c5:
        st.markdown(
            """
            <div class="card">
            <h3>🎓 Education Help</h3>
            <p>Scholarship guidance and education support for rural students.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c6:
        st.markdown(
            """
            <div class="card">
            <h3>💼 Jobs & Skills</h3>
            <p>Skill training and job portal guidance for rural youth.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success("This portal saves time and helps villagers get correct service guidance.")


# ---------------- GOVERNMENT SERVICES ----------------
elif menu == "Government Services":
    st.header("🏛️ Government Services")

    service = st.selectbox(
        "Select Service",
        [
            "Aadhaar Card",
            "PAN Card",
            "Ration Card / Rice Card",
            "Income Certificate",
            "Caste Certificate",
            "Residence Certificate",
            "Birth Certificate",
            "Old Age / Widow / Disability Pension",
            "Voter ID",
            "Government Schemes"
        ]
    )

    service_info = {
        "Aadhaar Card": {
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
        "PAN Card": {
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
        "Ration Card / Rice Card": {
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
        "Income Certificate": {
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
        "Caste Certificate": {
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
        "Residence Certificate": {
            "details": "Residence certificate is used as proof of address for education, jobs, and schemes.",
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
        "Birth Certificate": {
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
        "Old Age / Widow / Disability Pension": {
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
        "Voter ID": {
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
        "Government Schemes": {
            "details": "Citizens can search schemes based on age, income, occupation, and category.",
            "steps": [
                "Search suitable scheme.",
                "Check eligibility.",
                "Collect required documents.",
                "Apply online or through MeeSeva or village office.",
                "Track application status."
            ],
            "website": "https://www.india.gov.in"
        }
    }

    selected = service_info[service]

    st.markdown(f"### {service}")
    st.info(selected["details"])

    st.markdown("### ✅ Steps")
    for step in selected["steps"]:
        st.write(f"- {step}")

    st.markdown("### 🌐 Website")
    st.write(selected["website"])


# ---------------- FARMER HELP ----------------
elif menu == "Farmer Help":
    st.header("🌾 Farmer Crop Help")

    crop = st.selectbox(
        "Select Crop",
        ["Rice", "Cotton", "Maize", "Tomato", "Chilli", "Groundnut", "Potato", "Onion", "Other"]
    )

    problem = st.text_input(
        "Type crop problem",
        placeholder="Example: yellow leaves, pests, leaf spots, less growth, water problem"
    )

    farmer_guidance = {
        "yellow leaves": {
            "reason": "Possible reasons are nutrient deficiency, overwatering, poor soil health, or disease.",
            "solution": [
                "Check whether the soil is too dry or too wet.",
                "Use organic compost or farmyard manure.",
                "Avoid overwatering.",
                "Do soil testing if possible.",
                "Contact agriculture officer if yellowing spreads quickly."
            ]
        },
        "pest": {
            "reason": "Pests may damage leaves, stems, flowers, or fruits.",
            "solution": [
                "Check the plant leaves and stems carefully.",
                "Take a clear photo of affected crop.",
                "Remove heavily affected leaves if possible.",
                "Do not use random pesticide without advice.",
                "Contact agriculture officer for correct pesticide recommendation."
            ]
        },
        "leaf spot": {
            "reason": "Leaf spots may happen due to fungal or bacterial infection.",
            "solution": [
                "Avoid watering directly on leaves.",
                "Remove infected leaves carefully.",
                "Keep enough spacing between plants.",
                "Avoid overcrowding.",
                "Consult agriculture officer if spots increase."
            ]
        },
        "less growth": {
            "reason": "Less growth may happen due to poor soil nutrients, less sunlight, weeds, or water stress.",
            "solution": [
                "Remove weeds around the crop.",
                "Use organic manure.",
                "Check irrigation properly.",
                "Ensure plants get enough sunlight.",
                "Do soil testing for better fertilizer usage."
            ]
        },
        "water": {
            "reason": "Too much or too little water can damage crops.",
            "solution": [
                "Do not overwater the crop.",
                "Water early morning or evening.",
                "Improve drainage if water is standing.",
                "Use drip irrigation if available.",
                "Check soil moisture before watering."
            ]
        },
        "fertilizer": {
            "reason": "Wrong fertilizer usage can damage crop growth.",
            "solution": [
                "Use fertilizer based on crop stage.",
                "Do soil testing before applying fertilizer.",
                "Avoid applying too much chemical fertilizer.",
                "Use compost to improve soil health.",
                "Ask agriculture officer for crop-specific fertilizer dosage."
            ]
        },
        "disease": {
            "reason": "Crop disease can happen due to fungus, bacteria, virus, pests, or weather conditions.",
            "solution": [
                "Take a clear photo of affected crop.",
                "Separate affected plants if possible.",
                "Avoid using random medicines.",
                "Check if leaves, stem, or fruits are affected.",
                "Contact agriculture department for exact disease identification."
            ]
        },
        "dry leaves": {
            "reason": "Dry leaves may happen due to water shortage, heat, fertilizer burn, or root damage.",
            "solution": [
                "Check soil moisture.",
                "Water the crop properly.",
                "Add mulch around plants.",
                "Avoid too much fertilizer.",
                "Check roots and soil condition."
            ]
        },
        "fruit rot": {
            "reason": "Fruit rot may happen due to fungal infection, excess moisture, or poor air circulation.",
            "solution": [
                "Remove rotten fruits.",
                "Avoid waterlogging.",
                "Keep proper spacing between plants.",
                "Do not let fruits touch wet soil.",
                "Consult agriculture officer if rot spreads."
            ]
        },
        "flower drop": {
            "reason": "Flower drop may happen due to heat, water stress, poor pollination, or nutrient deficiency.",
            "solution": [
                "Maintain proper watering.",
                "Avoid water stress.",
                "Use compost.",
                "Protect crop from extreme heat if possible.",
                "Consult agriculture officer if problem continues."
            ]
        }
    }

    if st.button("Get Farmer Advice"):
        q = problem.lower().strip()
        found = False

        st.subheader(f"Guidance for {crop}")

        for key, data in farmer_guidance.items():
            if key in q:
                st.success("Possible Reason")
                st.write(data["reason"])

                st.markdown("### How to reduce the problem")
                for step in data["solution"]:
                    st.write(f"- {step}")

                st.info("Agriculture Website: https://agricoop.gov.in")
                found = True
                break

        if not found:
            st.warning("This crop problem is not in the current list.")
            st.write(
                """
                Basic farmer guidance:
                - Check soil moisture.
                - Remove weeds.
                - Use organic compost.
                - Avoid overwatering.
                - Take a clear crop photo.
                - Visit nearest agriculture office if the problem continues.
                """
            )
            st.info("Agriculture Website: https://agricoop.gov.in")


# ---------------- HEALTH SUPPORT ----------------
elif menu == "Health Support":
    st.header("🏥 Health Support")

    st.write("Type your health issue and get basic awareness guidance.")

    issue = st.text_input(
        "Enter health issue",
        placeholder="Example: fever, headache, cough, stomach pain, vomiting"
    )

    health_guidance = {
        "fever": {
            "guidance": "Fever may happen due to infection, heat, or seasonal illness.",
            "reduce": [
                "Drink plenty of water.",
                "Take proper rest.",
                "Wear light clothes.",
                "Use a wet cloth on forehead if temperature is high.",
                "Visit doctor if fever continues more than 2 days."
            ],
            "danger": "High fever, breathing problem, continuous vomiting, fits, or unconsciousness."
        },
        "headache": {
            "guidance": "Headache may happen due to stress, dehydration, lack of sleep, or screen usage.",
            "reduce": [
                "Drink enough water.",
                "Rest in a quiet place.",
                "Reduce mobile or laptop screen time.",
                "Sleep properly.",
                "Avoid loud noise."
            ],
            "danger": "Severe headache, fainting, blurred vision, vomiting, or headache after injury."
        },
        "cough": {
            "guidance": "Cough may happen due to cold, dust, allergy, or infection.",
            "reduce": [
                "Drink warm water.",
                "Avoid cold drinks.",
                "Avoid dust and smoke.",
                "Use steam carefully.",
                "Visit doctor if cough continues more than one week."
            ],
            "danger": "Breathing difficulty, chest pain, blood in cough, or high fever."
        },
        "cold": {
            "guidance": "Cold usually improves with rest and fluids.",
            "reduce": [
                "Drink warm water.",
                "Take rest.",
                "Avoid cold food and drinks.",
                "Keep yourself warm.",
                "Maintain hygiene."
            ],
            "danger": "High fever, breathing problem, chest pain, or symptoms continuing many days."
        },
        "stomach pain": {
            "guidance": "Stomach pain may happen due to gas, indigestion, unsafe food, or infection.",
            "reduce": [
                "Drink clean water.",
                "Eat light food.",
                "Avoid oily and outside food.",
                "Take rest.",
                "Visit doctor if pain is severe."
            ],
            "danger": "Severe pain, vomiting, blood in stool, continuous pain, or swelling."
        },
        "vomiting": {
            "guidance": "Vomiting can cause dehydration.",
            "reduce": [
                "Drink small sips of water or ORS.",
                "Avoid spicy and oily food.",
                "Take rest.",
                "Eat light food after vomiting reduces.",
                "Visit doctor if vomiting continues."
            ],
            "danger": "Continuous vomiting, severe weakness, dehydration, or blood in vomit."
        },
        "diarrhea": {
            "guidance": "Loose motions can cause dehydration.",
            "reduce": [
                "Drink ORS or clean water.",
                "Eat simple food.",
                "Avoid outside food.",
                "Maintain hygiene.",
                "Wash hands before eating."
            ],
            "danger": "Blood in stool, dehydration, high fever, or severe weakness."
        },
        "weakness": {
            "guidance": "Weakness may happen due to less food, dehydration, fever, or low nutrition.",
            "reduce": [
                "Eat healthy food.",
                "Drink enough water.",
                "Take proper rest.",
                "Eat fruits and vegetables.",
                "Visit doctor if weakness continues."
            ],
            "danger": "Fainting, chest pain, breathing problem, or severe tiredness."
        },
        "body pain": {
            "guidance": "Body pain may happen due to fever, tiredness, heavy work, or infection.",
            "reduce": [
                "Take rest.",
                "Drink water.",
                "Avoid heavy work for some time.",
                "Sleep properly.",
                "Visit doctor if pain is severe."
            ],
            "danger": "Severe pain, swelling, injury, chest pain, or fever with body pains."
        },
        "tooth pain": {
            "guidance": "Tooth pain may happen due to cavity, gum problem, or infection.",
            "reduce": [
                "Rinse mouth with clean warm water.",
                "Avoid very cold or very hot foods.",
                "Keep mouth clean.",
                "Do not put unknown powders or chemicals.",
                "Visit dentist if pain continues."
            ],
            "danger": "Face swelling, fever, severe pain, or difficulty opening mouth."
        },
        "burn": {
            "guidance": "Burns need careful first aid.",
            "reduce": [
                "Keep the burned area under cool running water for some time.",
                "Do not apply toothpaste, oil, or unknown creams.",
                "Cover with clean cloth.",
                "Visit doctor if burn is large or severe."
            ],
            "danger": "Large burn, face burn, electric burn, severe pain, or breathing difficulty."
        }
    }

    if st.button("Get Health Guidance"):
        q = issue.lower().strip()
        found = False

        for problem, data in health_guidance.items():
            if problem in q:
                st.success(f"Guidance for {problem.title()}")
                st.write(data["guidance"])

                st.markdown("### How to reduce it")
                for step in data["reduce"]:
                    st.write(f"- {step}")

                st.markdown("### Visit doctor immediately if")
                st.error(data["danger"])

                st.warning("This is basic awareness only. For serious health problems, consult a doctor.")
                st.info("Health Website: https://www.mohfw.gov.in")

                found = True
                break

        if not found:
            st.warning("This issue is not in the current list.")
            st.write(
                """
                Basic guidance:
                - Take rest.
                - Drink clean water.
                - Eat light and healthy food.
                - Maintain hygiene.
                - Visit nearest PHC, clinic, or hospital if symptoms continue.
                """
            )
            st.error("For emergency, call ambulance 108.")
            st.info("Health Website: https://www.mohfw.gov.in")


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


# ---------------- EDUCATION ----------------
elif menu == "Education & Scholarships":
    st.header("🎓 Education & Scholarships")

    st.markdown(
        """
        <div class="small-card">
        <h4>Scholarship Guidance</h4>
        <p>This section helps students find scholarship and education support.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        """
        Steps:
        1. Check scholarship eligibility.
        2. Collect Aadhaar, income certificate, caste certificate if needed, marks memo, and bank details.
        3. Register online.
        4. Fill scholarship application.
        5. Upload documents.
        6. Submit and track status.
        """
    )

    st.info("National Scholarship Portal: https://scholarships.gov.in")
    st.info("Telangana MeeSeva: https://ts.meeseva.telangana.gov.in/meeseva/")


# ---------------- JOBS ----------------
elif menu == "Jobs & Skills":
    st.header("💼 Jobs & Skills")

    st.markdown(
        """
        <div class="small-card">
        <h4>Job and Skill Support</h4>
        <p>This section helps youth find job and skill development information.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        """
        Steps:
        1. Register on job portal.
        2. Create profile.
        3. Add education and skills.
        4. Search jobs or training.
        5. Apply for suitable opportunities.
        """
    )

    st.info("National Career Service: https://www.ncs.gov.in")
    st.info("Skill India: https://www.skillindiadigital.gov.in")


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


# ---------------- AI ASSISTANT ----------------
elif menu == "AI Help Assistant":
    st.header("🤖 AI Help Assistant")

    question = st.text_input("Ask your question")

    if st.button("Ask"):
        q = question.lower()

        if "aadhaar" in q or "aadhar" in q:
            st.success("Go to Government Services → Aadhaar Card.")
            st.write("Website: https://uidai.gov.in")

        elif "pan" in q:
            st.success("Go to Government Services → PAN Card.")

        elif "ration" in q or "rice card" in q:
            st.success("Go to Government Services → Ration Card / Rice Card.")

        elif "income" in q or "caste" in q or "residence" in q or "birth" in q:
            st.success("Go to Government Services → Certificate Services.")

        elif "pension" in q:
            st.success("Go to Government Services → Pension Services.")

        elif "voter" in q:
            st.success("Go to Government Services → Voter ID.")

        elif "farmer" in q or "crop" in q or "agriculture" in q:
            st.success("Go to Farmer Help section.")

        elif "health" in q or "doctor" in q or "hospital" in q:
            st.success("Go to Health Support section.")

        elif "complaint" in q or "garbage" in q or "road" in q or "water" in q or "streetlight" in q:
            st.success("Go to Complaint Reporting section.")

        elif "scholarship" in q or "student" in q or "education" in q:
            st.success("Go to Education & Scholarships section.")

        elif "job" in q or "skill" in q or "employment" in q:
            st.success("Go to Jobs & Skills section.")

        elif "emergency" in q:
            st.success("Go to Emergency Contacts section.")

        else:
            st.info(
                "Ask about Aadhaar, PAN, ration card, certificates, pension, schemes, "
                "farming, health, complaints, education, jobs, or emergency."
            )


# ---------------- FOOTER ----------------
st.markdown(
    """
    <hr>
    <div class="footer">
        <p>AI Village Help Portal | Built using Python & Streamlit | Public Service Project</p>
    </div>
    """,
    unsafe_allow_html=True
)
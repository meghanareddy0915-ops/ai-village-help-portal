import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AI Village Help Portal", page_icon="🏡", layout="wide")

st.title("🏡 AI Village Help Portal")
st.write("A smart public service portal for village people.")

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
    st.header("Welcome to AI Village Help Portal")

    st.write("""
    This project helps villagers access important public services in one place.
    It gives information about government documents, schemes, farming, health,
    complaints, education, jobs, and emergency services.
    """)

    st.subheader("Main Services")
    st.write("""
    - Aadhaar and PAN services
    - Ration card / Rice card
    - Income, caste, residence, and birth certificates
    - Pension and welfare schemes
    - Farmer crop support
    - Health guidance
    - Public complaint reporting
    - Scholarships and education help
    - Jobs and skill training
    - Emergency contacts
    """)

    st.success("This project is useful for rural people because it saves time and gives correct service guidance.")


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

    if service == "Aadhaar Card":
        st.subheader("Aadhaar Card Service")
        st.write("""
        Aadhaar is used for identity verification, bank linking, SIM verification,
        government schemes, and other public services.
        """)
        st.write("""
        Steps:
        1. Visit nearest Aadhaar Seva Kendra or MeeSeva center.
        2. Carry identity proof and address proof.
        3. Apply for new Aadhaar or update details.
        4. Give biometrics if required.
        5. Collect acknowledgement slip.
        6. Track Aadhaar status online.
        """)
        st.info("Website: https://uidai.gov.in")

    elif service == "PAN Card":
        st.subheader("PAN Card Service")
        st.write("PAN is useful for bank accounts, tax services, scholarships, and financial work.")
        st.write("""
        Steps:
        1. Open PAN application website.
        2. Fill personal details.
        3. Upload documents.
        4. Pay fee if required.
        5. Submit application.
        6. Track PAN status online.
        """)
        st.info("Website: https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html")

    elif service == "Ration Card / Rice Card":
        st.subheader("Ration Card / Rice Card")
        st.write("Ration card helps families receive food grains and other welfare benefits.")
        st.write("""
        Steps:
        1. Visit MeeSeva or village secretariat.
        2. Submit family details.
        3. Attach Aadhaar, address proof, and income proof.
        4. Submit application.
        5. Track application status.
        """)
        st.info("Website: https://ts.meeseva.telangana.gov.in/meeseva/")

    elif service in ["Income Certificate", "Caste Certificate", "Residence Certificate", "Birth Certificate"]:
        st.subheader(service)
        st.write("This certificate is useful for education, scholarships, jobs, and government schemes.")
        st.write("""
        Steps:
        1. Visit MeeSeva portal or MeeSeva center.
        2. Select certificate service.
        3. Fill application form.
        4. Upload required documents.
        5. Pay fee if required.
        6. Download certificate after approval.
        """)
        st.info("Website: https://ts.meeseva.telangana.gov.in/meeseva/")

    elif service == "Old Age / Widow / Disability Pension":
        st.subheader("Pension Services")
        st.write("Pension schemes support senior citizens, widows, and disabled persons.")
        st.write("""
        Steps:
        1. Check eligibility.
        2. Collect Aadhaar, bank passbook, income certificate, and photo.
        3. Apply through MeeSeva or village secretariat.
        4. Submit documents.
        5. Track pension approval status.
        """)
        st.info("Website: https://ts.meeseva.telangana.gov.in/meeseva/")

    elif service == "Voter ID":
        st.subheader("Voter ID Service")
        st.write("Voter ID is used for voting and identity proof.")
        st.write("""
        Steps:
        1. Visit voter service portal.
        2. Apply for new voter ID or correction.
        3. Upload age and address proof.
        4. Submit application.
        5. Track status online.
        """)
        st.info("Website: https://voters.eci.gov.in")

    elif service == "Government Schemes":
        st.subheader("Government Schemes")
        st.write("Citizens can search schemes based on age, income, occupation, and category.")
        st.write("""
        Steps:
        1. Search suitable scheme.
        2. Check eligibility.
        3. Collect required documents.
        4. Apply online or through MeeSeva/village office.
        5. Track application status.
        """)
        st.info("Website: https://www.india.gov.in")


# ---------------- FARMER HELP ----------------
elif menu == "Farmer Help":
    st.header("🌾 Farmer Crop Help")

    crop = st.selectbox(
        "Select Crop",
        [
            "Rice",
            "Cotton",
            "Maize",
            "Tomato",
            "Chilli",
            "Groundnut",
            "Potato",
            "Onion",
            "Other"
        ]
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
        "insect": {
            "reason": "Insects can reduce crop growth and damage yield.",
            "solution": [
                "Observe which part of the plant is affected.",
                "Use natural pest control methods if possible.",
                "Keep field clean.",
                "Consult agriculture officer before spraying pesticide."
            ]
        },
        "root rot": {
            "reason": "Root rot may happen due to excess water or fungal infection.",
            "solution": [
                "Improve soil drainage.",
                "Avoid overwatering.",
                "Remove affected plants carefully.",
                "Consult agriculture officer if spread increases."
            ]

        },

        "low yield": {
            "reason": "Low yield may happen due to poor soil nutrition or crop disease.",
            "solution": [
                "Use organic manure.",
                "Check irrigation properly.",
                "Do soil testing.",
                "Use proper fertilizer dosage."
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
        "weeds": {
            "reason": "Weeds take nutrients, water, and sunlight from crops.",
            "solution": [
                "Remove weeds regularly.",
                "Use mulching.",
                "Maintain proper spacing.",
                "Remove weeds before flowering.",
                "Keep field clean."
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
            st.write("""
            Basic farmer guidance:
            - Check soil moisture.
            - Remove weeds.
            - Use organic compost.
            - Avoid overwatering.
            - Take a clear crop photo.
            - Visit nearest agriculture office if the problem continues.
            """)
            st.info("Agriculture Website: https://agricoop.gov.in")


# ---------------- HEALTH SUPPORT ----------------
elif menu == "Health Support":
    st.header("🏥 Health Support")

    st.write("Type your health issue and get basic guidance.")

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
        "loose motion": {
            "guidance": "Loose motions can happen due to unsafe food, infection, or contaminated water.",
            "reduce": [
                "Drink ORS.",
                "Drink clean water.",
                "Avoid spicy food.",
                "Eat rice, curd, or simple food.",
                "Visit doctor if it continues."
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
        "skin rash": {
            "guidance": "Skin rash may happen due to allergy, infection, heat, or insect bite.",
            "reduce": [
                "Keep skin clean.",
                "Do not scratch.",
                "Avoid unknown creams.",
                "Wear clean clothes.",
                "Visit doctor if rash spreads."
            ],
            "danger": "Swelling, breathing problem, fever, or rash spreading fast."
        },
        "eye pain": {
            "guidance": "Eye pain may happen due to dust, infection, dryness, or screen strain.",
            "reduce": [
                "Wash eyes with clean water.",
                "Avoid rubbing eyes.",
                "Reduce screen time.",
                "Use clean towel.",
                "Visit eye doctor if pain continues."
            ],
            "danger": "Vision loss, severe pain, injury, redness with swelling, or eye discharge."
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
        "ear pain": {
             "guidance": "Ear pain may happen due to infection, cold, or injury.",
             "reduce": [
                 "Keep ear clean and dry.",
                 "Avoid inserting objects into ear.",
                 "Visit doctor if pain continues."
            ],
            "danger": "Severe pain, swelling, pus, or hearing problem."
        },

        "dehydration": {
             "guidance": "Dehydration happens when body loses too much water.",
             "reduce": [
                "Drink ORS or water regularly.",
                "Avoid too much sun exposure.",
                "Eat fruits and healthy food."
            ],
            "danger": "Severe weakness, dizziness, or unconsciousness."
        },
        "back pain": {
            "guidance": "Back pain may happen due to posture, heavy lifting, or muscle strain.",
            "reduce": [
                "Take rest.",
                "Avoid lifting heavy items.",
                "Sit with proper posture.",
                "Do gentle stretching.",
                "Visit doctor if pain continues."
            ],
            "danger": "Pain after injury, leg weakness, numbness, or severe pain."
        },
        "pregnancy": {
            "guidance": "Pregnant women should take regular checkups and follow doctor advice.",
            "reduce": [
                "Visit nearest health center regularly.",
                "Eat nutritious food.",
                "Take iron and calcium tablets only as advised by doctor.",
                "Avoid heavy work.",
                "Call ambulance during emergency."
            ],
            "danger": "Heavy bleeding, severe stomach pain, fits, severe headache, or reduced baby movement."
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
        },
        "injury": {
            "guidance": "Injury may need cleaning and medical care.",
            "reduce": [
                "Wash small wound with clean water.",
                "Cover with clean cloth.",
                "Avoid touching wound with dirty hands.",
                "Visit doctor for deep cuts or serious injury."
            ],
            "danger": "Heavy bleeding, deep wound, fracture, head injury, or unconsciousness."
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
            st.write("""
            Basic guidance:
            - Take rest.
            - Drink clean water.
            - Eat light and healthy food.
            - Maintain hygiene.
            - Visit nearest PHC, clinic, or hospital if symptoms continue.
            """)
            st.error("For emergency, call ambulance 108.")
            st.info("Health Website: https://www.mohfw.gov.in")


# ---------------- COMPLAINT REPORTING ----------------
elif menu == "Complaint Reporting":
    st.header("📝 Public Complaint Reporting")

    name = st.text_input("Citizen Name")
    village = st.text_input("Village Name")
    complaint_type = st.selectbox(
        "Complaint Type",
        ["Garbage Issue", "Road Damage", "Water Problem", "Streetlight Issue", "Drainage Problem", "Electricity Problem", "Other"]
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
        st.dataframe(pd.read_csv("complaints.csv"))
    except FileNotFoundError:
        st.write("No complaints submitted yet.")


# ---------------- EDUCATION ----------------
elif menu == "Education & Scholarships":
    st.header("🎓 Education & Scholarships")

    st.write("""
    This section helps students find scholarship and education support.
    """)

    st.write("""
    Steps:
    1. Check scholarship eligibility.
    2. Collect Aadhaar, income certificate, caste certificate if needed, marks memo, and bank details.
    3. Register online.
    4. Fill scholarship application.
    5. Upload documents.
    6. Submit and track status.
    """)

    st.info("National Scholarship Portal: https://scholarships.gov.in")
    st.info("Telangana MeeSeva: https://ts.meeseva.telangana.gov.in/meeseva/")


# ---------------- JOBS ----------------
elif menu == "Jobs & Skills":
    st.header("💼 Jobs & Skills")

    st.write("""
    This section helps youth find job and skill development information.
    """)

    st.write("""
    Steps:
    1. Register on job portal.
    2. Create profile.
    3. Add education and skills.
    4. Search jobs or training.
    5. Apply for suitable opportunities.
    """)

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
        ("Women Safety Helpline: 181")
        ("Mental Health Helpline: 14416")
    }

    for service, number in contacts.items():
        st.write(f"**{service}:** {number}")


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
            st.info("Ask about Aadhaar, PAN, ration card, certificates, pension, schemes, farming, health, complaints, education, jobs, or emergency.")
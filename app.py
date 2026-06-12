import streamlit as st
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
    placeholder=translate_text("Aadhaar, fever, crop insurance", language),
)

st.title("🏡 " + translate_text("AI Village Help Portal", language))
st.write(translate_text("A smart public service portal for village people.", language))

services = [
    {
        "keywords": ["aadhaar", "aadhar", "uidai"],
        "title": "Aadhaar Card",
        "details": "Aadhaar is used for identity verification, bank linking, SIM verification, and government schemes.",
        "steps": [
            "Visit nearest Aadhaar Seva Kendra or MeeSeva center.",
            "Carry identity proof and address proof.",
            "Apply for new Aadhaar or update details.",
            "Collect acknowledgement slip.",
            "Track Aadhaar status online.",
        ],
        "website": "https://uidai.gov.in",
    },
    {
        "keywords": ["pan", "pan card"],
        "title": "PAN Card",
        "details": "PAN is used for banking, tax filing, and financial services.",
        "steps": [
            "Open PAN application website.",
            "Fill personal details.",
            "Upload documents.",
            "Pay fee if required.",
            "Track PAN status online.",
        ],
        "website": "https://www.onlineservices.nsdl.com",
    },
    {
        "keywords": ["ration", "rice card", "ration card"],
        "title": "Ration Card / Rice Card",
        "details": "Ration card helps families receive food grains and welfare benefits.",
        "steps": [
            "Visit MeeSeva or village secretariat.",
            "Submit family details.",
            "Attach Aadhaar, address proof, and income proof.",
            "Track application status.",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["income", "income certificate"],
        "title": "Income Certificate",
        "details": "Income certificate is useful for scholarships, schemes, and fee reimbursement.",
        "steps": [
            "Visit MeeSeva center.",
            "Fill application form.",
            "Upload required documents.",
            "Pay fee if required.",
            "Download certificate after approval.",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["caste", "caste certificate"],
        "title": "Caste Certificate",
        "details": "Caste certificate is useful for education, scholarships, jobs, and reservations.",
        "steps": [
            "Visit MeeSeva center.",
            "Fill caste certificate application.",
            "Upload required documents.",
            "Submit application.",
            "Download certificate after approval.",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["residence", "residence certificate"],
        "title": "Residence Certificate",
        "details": "Residence certificate is used as proof of address.",
        "steps": [
            "Visit MeeSeva center.",
            "Fill residence certificate form.",
            "Upload address proof.",
            "Submit application.",
            "Track status online.",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["birth", "birth certificate"],
        "title": "Birth Certificate",
        "details": "Birth certificate is official proof of birth.",
        "steps": [
            "Visit municipality or MeeSeva.",
            "Submit hospital record if available.",
            "Fill birth certificate form.",
            "Submit parent details.",
            "Download certificate after approval.",
        ],
        "website": "https://crsorgi.gov.in",
    },
    {
        "keywords": ["death", "death certificate"],
        "title": "Death Certificate",
        "details": "Death certificate is required for legal and family benefit purposes.",
        "steps": [
            "Visit municipality or MeeSeva.",
            "Submit death proof.",
            "Fill application form.",
            "Upload required documents.",
            "Download certificate after approval.",
        ],
        "website": "https://ts.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["marriage", "marriage certificate", "marriage registration"],
        "title": "Marriage Certificate",
        "details": "Marriage certificate is useful for legal proof, passport, bank, and family benefits.",
        "steps": [
            "Collect marriage proof and photos.",
            "Carry Aadhaar of both persons.",
            "Apply through registration office or online portal.",
            "Submit witness details.",
            "Download certificate after approval.",
        ],
        "website": "https://tg.meeseva.telangana.gov.in/meeseva/",
    },
    {
        "keywords": ["pension", "old age pension", "widow pension", "disability pension"],
        "title": "Pension Services",
        "details": "Pension schemes support senior citizens, widows, and disabled persons.",
        "steps": [
            "Check eligibility.",
            "Collect Aadhaar, bank passbook, income certificate, and photo.",
            "Apply through MeeSeva or village secretariat.",
            "Track pension approval status.",
        ],
        "website": "https://nsap.nic.in",
    },
    {
        "keywords": ["voter", "voter id", "election card"],
        "title": "Voter ID",
        "details": "Voter ID is used for voting and identity proof.",
        "steps": [
            "Visit voter service portal.",
            "Apply for new voter ID or correction.",
            "Upload age and address proof.",
            "Submit application.",
            "Track status online.",
        ],
        "website": "https://voters.eci.gov.in",
    },
    {
        "keywords": ["lost document", "lost aadhaar", "lost pan", "lost certificate"],
        "title": "Lost Document Help",
        "details": "Guidance for recovering lost Aadhaar, PAN, certificates, or other documents.",
        "steps": [
            "Check if digital copy is available.",
            "File police complaint if required.",
            "Visit official website for duplicate copy.",
            "Submit identity proof.",
            "Download or reapply for document.",
        ],
        "website": "https://www.india.gov.in",
    },
    {
        "keywords": ["police complaint", "fir", "lost phone", "theft"],
        "title": "Police Complaint / FIR Guidance",
        "details": "Citizens can report theft, lost documents, or safety problems to police.",
        "steps": [
            "Visit nearest police station or online portal.",
            "Explain issue clearly.",
            "Provide identity proof.",
            "Collect complaint acknowledgement.",
            "Follow up using complaint number.",
        ],
        "website": "https://www.tspolice.gov.in",
    },
    {
        "keywords": ["digital seva", "csc", "online service center", "meeseva"],
        "title": "Digital Seva / CSC Services",
        "details": "Common Service Centers help villagers access online government services.",
        "steps": [
            "Visit nearest CSC or MeeSeva center.",
            "Carry required documents.",
            "Ask for the needed online service.",
            "Pay service fee if required.",
            "Collect receipt or acknowledgement.",
        ],
        "website": "https://csc.gov.in",
    },
    {
        "keywords": ["farmer", "crop", "agriculture"],
        "title": "Farmer Support",
        "details": "Farmer support gives crop, fertilizer, pest, and farming guidance.",
        "steps": [
            "Check crop problem.",
            "Use organic compost.",
            "Avoid overwatering.",
            "Take crop photo if disease appears.",
            "Contact agriculture officer if issue continues.",
        ],
        "website": "https://agricoop.gov.in",
    },
    {
        "keywords": ["crop insurance", "pmfby"],
        "title": "Crop Insurance",
        "details": "Crop insurance helps farmers during crop loss due to natural problems.",
        "steps": [
            "Open PMFBY website.",
            "Submit farmer details.",
            "Enter crop and land details.",
            "Track claim status online.",
        ],
        "website": "https://pmfby.gov.in",
    },
    {
        "keywords": ["pm kisan", "kisan"],
        "title": "PM-KISAN Scheme",
        "details": "PM-KISAN provides financial support to eligible farmers.",
        "steps": [
            "Open PM-KISAN website.",
            "Check eligibility.",
            "Enter Aadhaar and land details.",
            "Submit bank account details.",
            "Track beneficiary status.",
        ],
        "website": "https://pmkisan.gov.in",
    },
    {
        "keywords": ["soil testing", "soil test", "soil health"],
        "title": "Soil Testing",
        "details": "Soil testing helps farmers know soil nutrients and fertilizer needs.",
        "steps": [
            "Collect soil sample.",
            "Visit agriculture office.",
            "Submit sample.",
            "Receive soil health report.",
            "Use fertilizer based on report.",
        ],
        "website": "https://soilhealth.dac.gov.in",
    },
    {
        "keywords": ["fertilizer", "urea", "compost"],
        "title": "Fertilizer Guidance",
        "details": "Proper fertilizer use improves crop growth and soil health.",
        "steps": [
            "Identify crop stage.",
            "Use fertilizer based on soil test.",
            "Avoid excessive fertilizer.",
            "Use organic compost.",
            "Contact agriculture officer for dosage.",
        ],
        "website": "https://agricoop.gov.in",
    },
    {
        "keywords": ["pest", "pest attack", "insects"],
        "title": "Pest Attack Guidance",
        "details": "Pests can damage leaves, stems, flowers, and fruits.",
        "steps": [
            "Check affected parts.",
            "Take crop photo.",
            "Remove affected leaves if possible.",
            "Avoid random pesticide.",
            "Consult agriculture officer.",
        ],
        "website": "https://agricoop.gov.in",
    },
    {
        "keywords": ["crop loan", "farmer loan"],
        "title": "Crop Loan Guidance",
        "details": "Farmers can apply for crop loans through banks for seasonal farming needs.",
        "steps": [
            "Visit nearest bank branch.",
            "Carry Aadhaar, land documents, and bank passbook.",
            "Fill crop loan application.",
            "Submit crop and land details.",
            "Track loan approval.",
        ],
        "website": "https://www.india.gov.in",
    },
    {
        "keywords": ["market price", "crop price", "mandi price"],
        "title": "Crop Market Price",
        "details": "Farmers can check market prices before selling crops.",
        "steps": [
            "Open agriculture market price portal.",
            "Select crop name.",
            "Select state and market.",
            "Check latest price.",
            "Compare prices before selling.",
        ],
        "website": "https://agmarknet.gov.in",
    },
    {
        "keywords": ["seed", "seeds", "seed subsidy"],
        "title": "Seed Support",
        "details": "Farmers can get information about quality seeds and seed subsidy support.",
        "steps": [
            "Visit agriculture office.",
            "Ask about available certified seeds.",
            "Check seed subsidy eligibility.",
            "Purchase seeds from approved center.",
            "Keep receipt safely.",
        ],
        "website": "https://agricoop.gov.in",
    },
    {
        "keywords": ["irrigation", "drip irrigation", "sprinkler"],
        "title": "Irrigation Support",
        "details": "Farmers can get guidance for drip irrigation, sprinkler systems, and water-saving methods.",
        "steps": [
            "Check water availability in farm.",
            "Consult agriculture officer.",
            "Choose drip or sprinkler system.",
            "Apply for subsidy if available.",
            "Maintain irrigation system regularly.",
        ],
        "website": "https://pmksy.gov.in",
    },
    {
        "keywords": ["animal care", "cattle", "veterinary", "cow", "buffalo"],
        "title": "Animal Care",
        "details": "Animal care helps maintain cattle and farm animal health.",
        "steps": [
            "Vaccinate animals regularly.",
            "Provide clean water and food.",
            "Keep shelter clean.",
            "Contact veterinary doctor if sick.",
        ],
        "website": "https://dahd.nic.in",
    },
    {
        "keywords": ["fish farming", "fishery"],
        "title": "Fish Farming",
        "details": "Fish farming guidance helps with pond and fish management.",
        "steps": [
            "Maintain clean pond water.",
            "Use quality fish seeds.",
            "Provide proper feed.",
            "Monitor water quality.",
            "Contact fisheries officer if needed.",
        ],
        "website": "https://nfdb.gov.in",
    },
    {
        "keywords": ["land records", "pahani", "adangal", "land passbook"],
        "title": "Land Records Service",
        "details": "Farmers and land owners can check land records, survey details, and passbook information.",
        "steps": [
            "Open the land records portal.",
            "Enter district, mandal, village, and survey number.",
            "Check owner and land details.",
            "Download or save record if available.",
            "Visit revenue office if correction is needed.",
        ],
        "website": "https://dharani.telangana.gov.in",
    },
    {
        "keywords": ["mutation", "land mutation"],
        "title": "Land Mutation Service",
        "details": "Land mutation updates ownership details after sale, inheritance, or transfer.",
        "steps": [
            "Collect sale deed or ownership proof.",
            "Visit revenue office or online portal.",
            "Submit mutation application.",
            "Upload required documents.",
            "Track approval status.",
        ],
        "website": "https://dharani.telangana.gov.in",
    },
    {
        "keywords": ["fever", "temperature"],
        "title": "Fever Guidance",
        "details": "Fever may happen due to infection, heat, or seasonal illness.",
        "steps": [
            "Drink plenty of water.",
            "Take rest.",
            "Wear light clothes.",
            "Check temperature.",
            "Visit doctor if fever continues.",
        ],
        "website": "https://www.mohfw.gov.in",
    },
    {
        "keywords": ["cough", "cold"],
        "title": "Cough and Cold Guidance",
        "details": "Cough and cold may happen due to infection, dust, allergy, or weather changes.",
        "steps": [
            "Drink warm water.",
            "Avoid cold drinks.",
            "Avoid dust and smoke.",
            "Use steam carefully.",
            "Visit doctor if symptoms continue.",
        ],
        "website": "https://www.mohfw.gov.in",
    },
    {
        "keywords": ["headache", "head pain"],
        "title": "Headache Guidance",
        "details": "Headache may happen due to stress, dehydration, lack of sleep, or screen usage.",
        "steps": [
            "Drink water.",
            "Rest in a quiet place.",
            "Reduce screen time.",
            "Sleep properly.",
            "Visit doctor if severe.",
        ],
        "website": "https://www.mohfw.gov.in",
    },
    {
        "keywords": ["stomach pain", "vomiting", "diarrhea", "loose motion"],
        "title": "Stomach Problem Guidance",
        "details": "Stomach issues may happen due to unsafe food, infection, or dehydration.",
        "steps": [
            "Drink clean water.",
            "Eat light food.",
            "Avoid oily food.",
            "Use ORS for dehydration.",
            "Visit doctor if severe.",
        ],
        "website": "https://www.mohfw.gov.in",
    },
    {
        "keywords": ["pregnancy", "pregnant", "mother care"],
        "title": "Pregnancy Support",
        "details": "Pregnant women should take regular checkups and nutrition support.",
        "steps": [
            "Visit nearest health center.",
            "Attend regular checkups.",
            "Take nutritious food.",
            "Follow doctor advice.",
            "Call ambulance during emergency.",
        ],
        "website": "https://nhm.gov.in",
    },
    {
        "keywords": ["ayushman", "health insurance"],
        "title": "Ayushman Bharat Health Scheme",
        "details": "Ayushman Bharat provides health coverage for eligible families.",
        "steps": [
            "Check eligibility online.",
            "Visit empanelled hospital.",
            "Verify Aadhaar or ration details.",
            "Use card for eligible treatment.",
        ],
        "website": "https://beneficiary.nha.gov.in",
    },
    {
        "keywords": ["vaccination", "vaccine", "immunization"],
        "title": "Vaccination Support",
        "details": "Vaccination helps children and adults prevent diseases.",
        "steps": [
            "Visit nearest PHC or government hospital.",
            "Carry health card if available.",
            "Check vaccination schedule.",
            "Take vaccine as advised.",
            "Keep vaccination record safely.",
        ],
        "website": "https://www.mohfw.gov.in",
    },
    {
        "keywords": ["blood donation", "blood bank"],
        "title": "Blood Bank / Blood Donation",
        "details": "Citizens can find blood banks or donate blood safely.",
        "steps": [
            "Open blood bank portal.",
            "Search nearest blood bank.",
            "Check blood availability.",
            "Contact hospital or blood bank.",
            "Donate blood only if medically fit.",
        ],
        "website": "https://www.eraktkosh.in",
    },
    {
        "keywords": ["ambulance", "108 service"],
        "title": "Ambulance Service",
        "details": "Ambulance service provides emergency medical transport.",
        "steps": [
            "Call 108 during medical emergency.",
            "Give exact location.",
            "Explain patient condition.",
            "Stay near patient until ambulance arrives.",
            "Follow medical staff instructions.",
        ],
        "website": "https://112.gov.in",
    },
    {
        "keywords": ["mental health", "stress", "depression", "anxiety"],
        "title": "Mental Health Support",
        "details": "Mental health support helps people facing stress, anxiety, or emotional problems.",
        "steps": [
            "Talk to a trusted person.",
            "Visit nearest health center or counselor.",
            "Avoid isolation.",
            "Call mental health helpline if needed.",
            "Seek emergency support if there is immediate danger.",
        ],
        "website": "https://telemanas.mohfw.gov.in",
    },
    {
        "keywords": ["snake bite", "dog bite", "animal bite"],
        "title": "Animal Bite Emergency",
        "details": "Snake bite or dog bite needs urgent medical care.",
        "steps": [
            "Stay calm and avoid home remedies.",
            "Wash dog bite wound with clean water.",
            "Do not cut or suck snake bite area.",
            "Go to nearest hospital immediately.",
            "Call ambulance if needed.",
        ],
        "website": "https://www.mohfw.gov.in",
    },
    {
        "keywords": ["heat stroke", "sun stroke", "heat wave"],
        "title": "Heat Stroke Guidance",
        "details": "Heat stroke can happen during high temperature and needs quick care.",
        "steps": [
            "Move person to cool place.",
            "Give water if conscious.",
            "Use wet cloth to cool body.",
            "Avoid direct sunlight.",
            "Visit hospital if symptoms are severe.",
        ],
        "website": "https://ndma.gov.in",
    },
    {
        "keywords": ["scholarship", "student", "education"],
        "title": "Education & Scholarships",
        "details": "Scholarships help students get financial support for education.",
        "steps": [
            "Check eligibility.",
            "Collect Aadhaar, income certificate, marks memo, and bank details.",
            "Register online.",
            "Submit application.",
            "Track status.",
        ],
        "website": "https://scholarships.gov.in",
    },
    {
        "keywords": ["fee reimbursement", "fees"],
        "title": "Fee Reimbursement",
        "details": "Fee reimbursement helps eligible students pay education fees.",
        "steps": [
            "Check eligibility.",
            "Collect income and caste certificates.",
            "Submit college details.",
            "Apply through official portal.",
            "Track status.",
        ],
        "website": "https://scholarships.gov.in",
    },
    {
        "keywords": ["job", "employment", "ncs"],
        "title": "Jobs & Employment",
        "details": "This helps youth find jobs and employment opportunities.",
        "steps": [
            "Register on job portal.",
            "Create profile.",
            "Add education and skills.",
            "Search jobs.",
            "Apply for opportunities.",
        ],
        "website": "https://www.ncs.gov.in",
    },
    {
        "keywords": ["skill", "skill training", "free course"],
        "title": "Skill Development",
        "details": "Skill training helps youth improve employability.",
        "steps": [
            "Open Skill India portal.",
            "Choose training course.",
            "Register with basic details.",
            "Attend training.",
            "Apply for jobs after training.",
        ],
        "website": "https://www.skillindiadigital.gov.in",
    },
    {
        "keywords": ["employment card", "mgnrega", "job card"],
        "title": "MGNREGA Job Card",
        "details": "MGNREGA provides rural employment support to eligible families.",
        "steps": [
            "Visit Gram Panchayat office.",
            "Submit family and Aadhaar details.",
            "Apply for job card.",
            "Request work when needed.",
            "Track wages and work details.",
        ],
        "website": "https://nrega.nic.in",
    },
    {
        "keywords": ["electricity", "current bill", "power bill"],
        "title": "Electricity Bill Payment",
        "details": "Citizens can check and pay electricity bills online.",
        "steps": [
            "Open electricity website.",
            "Enter service number.",
            "Check bill amount.",
            "Pay online.",
            "Save receipt.",
        ],
        "website": "https://www.tssouthernpower.com",
    },
    {
        "keywords": ["water", "water problem", "water supply"],
        "title": "Water Supply Problem",
        "details": "Villagers can get guidance for drinking water and water supply issues.",
        "steps": [
            "Use clean water storage containers.",
            "Boil drinking water if needed.",
            "Report leakage to local office.",
            "Submit complaint if issue continues.",
        ],
        "website": "https://jalshakti-ddws.gov.in",
    },
    {
        "keywords": ["drainage", "sewage"],
        "title": "Drainage Problem",
        "details": "Guidance for drainage blockage and sewage issues.",
        "steps": [
            "Avoid dumping waste into drains.",
            "Report blocked drainage.",
            "Take photo if possible.",
            "Submit complaint.",
            "Follow up with local office.",
        ],
        "website": "https://pgportal.gov.in",
    },
    {
        "keywords": ["streetlight", "street light"],
        "title": "Streetlight Complaint",
        "details": "Citizens can report damaged or non-working streetlights.",
        "steps": [
            "Note streetlight location.",
            "Take photo if possible.",
            "Submit complaint to municipality.",
            "Track complaint status.",
        ],
        "website": "https://pgportal.gov.in",
    },
    {
        "keywords": ["garbage", "waste", "cleanliness", "sanitation"],
        "title": "Garbage and Sanitation Complaint",
        "details": "Citizens can report garbage collection or cleanliness problems.",
        "steps": [
            "Note exact location.",
            "Take photo if available.",
            "Submit complaint.",
            "Follow up with local office.",
        ],
        "website": "https://swachhbharatmission.gov.in",
    },
    {
        "keywords": ["passport"],
        "title": "Passport Service",
        "details": "Citizens can apply for passport or passport renewal.",
        "steps": [
            "Open Passport Seva website.",
            "Register or login.",
            "Fill application form.",
            "Book appointment.",
            "Visit passport office with documents.",
        ],
        "website": "https://www.passportindia.gov.in",
    },
    {
        "keywords": ["driving licence", "driving license", "license"],
        "title": "Driving Licence",
        "details": "Citizens can apply for learner licence or driving licence.",
        "steps": [
            "Open Parivahan portal.",
            "Fill application form.",
            "Upload documents.",
            "Book test slot.",
            "Attend test.",
        ],
        "website": "https://parivahan.gov.in",
    },
    {
        "keywords": ["bus pass", "student bus pass"],
        "title": "Bus Pass Service",
        "details": "Students and citizens can apply for bus passes.",
        "steps": [
            "Visit transport portal.",
            "Upload student or identity proof.",
            "Submit application.",
            "Download or collect bus pass.",
        ],
        "website": "https://online.tsrtcpass.in",
    },
    {
        "keywords": ["railway", "train ticket", "railway ticket"],
        "title": "Railway Ticket Booking",
        "details": "Citizens can book railway tickets online.",
        "steps": [
            "Open IRCTC website.",
            "Login or register.",
            "Search trains.",
            "Book ticket online.",
        ],
        "website": "https://www.irctc.co.in",
    },
    {
        "keywords": ["gas", "lpg", "gas connection"],
        "title": "LPG Gas Connection",
        "details": "Citizens can apply for new LPG gas connection or refill booking.",
        "steps": [
            "Visit gas agency or LPG website.",
            "Submit Aadhaar and address proof.",
            "Apply for connection or refill.",
            "Complete verification.",
        ],
        "website": "https://www.mylpg.in",
    },
    {
        "keywords": ["bank", "bank account", "loan"],
        "title": "Bank Account and Loan Guidance",
        "details": "Citizens can open bank accounts or get basic loan guidance.",
        "steps": [
            "Visit nearest bank.",
            "Carry Aadhaar, PAN, and photo.",
            "Fill application form.",
            "Submit documents.",
            "Collect passbook or account details.",
        ],
        "website": "https://www.india.gov.in",
    },
    {
        "keywords": ["small business", "mudra loan", "business loan"],
        "title": "Small Business Loan",
        "details": "Citizens can apply for small business support through Mudra loan and other schemes.",
        "steps": [
            "Prepare business idea.",
            "Visit bank or Mudra portal.",
            "Submit Aadhaar, PAN, and business details.",
            "Apply for suitable loan category.",
            "Track application status.",
        ],
        "website": "https://www.mudra.org.in",
    },
    {
        "keywords": ["self help group", "shg", "dwcra"],
        "title": "Self Help Group Support",
        "details": "Women and village groups can form SHGs for savings, loans, and small business support.",
        "steps": [
            "Form a group with eligible members.",
            "Open group bank account.",
            "Maintain savings records.",
            "Apply for bank linkage or scheme support.",
            "Start small income activity.",
        ],
        "website": "https://nrlm.gov.in",
    },
    {
        "keywords": ["housing", "pm awas", "house"],
        "title": "Housing Scheme",
        "details": "Government housing schemes support eligible families.",
        "steps": [
            "Check PM Awas eligibility.",
            "Collect Aadhaar, income proof, and address proof.",
            "Apply through portal or local office.",
            "Track application status.",
        ],
        "website": "https://pmaymis.gov.in",
    },
    {
        "keywords": ["toilet", "toilet scheme", "swachh bharat"],
        "title": "Toilet Scheme",
        "details": "Government toilet construction support for rural families.",
        "steps": [
            "Visit village secretariat.",
            "Check eligibility.",
            "Submit Aadhaar and address proof.",
            "Apply for toilet scheme.",
        ],
        "website": "https://swachhbharatmission.gov.in",
    },
    {
        "keywords": ["women safety", "women helpline", "women support"],
        "title": "Women Safety Support",
        "details": "Emergency and safety support for women.",
        "steps": [
            "Call women helpline 181.",
            "Contact nearby police station.",
            "Use emergency support services.",
            "Report harassment immediately.",
        ],
        "website": "https://wcd.nic.in",
    },
    {
        "keywords": ["child", "child helpline", "anganwadi"],
        "title": "Child and Anganwadi Services",
        "details": "Anganwadi services support children, pregnant women, and mothers.",
        "steps": [
            "Visit nearest Anganwadi center.",
            "Register child or pregnant woman.",
            "Receive nutrition and health support.",
            "Follow regular visit schedule.",
        ],
        "website": "https://wcd.nic.in",
    },
    {
        "keywords": ["weather", "rain", "climate"],
        "title": "Weather Information",
        "details": "Weather updates are useful for farmers and villagers.",
        "steps": [
            "Check daily weather updates.",
            "Avoid farming during heavy rain.",
            "Protect crops during storms.",
            "Follow weather alerts.",
        ],
        "website": "https://mausam.imd.gov.in",
    },
    {
        "keywords": ["disaster", "flood", "cyclone", "earthquake"],
        "title": "Disaster Safety",
        "details": "Disaster safety guidance helps during floods, cyclones, and emergencies.",
        "steps": [
            "Follow official alerts.",
            "Keep emergency kit ready.",
            "Move to safe place if advised.",
            "Avoid flood water.",
            "Call emergency services if trapped.",
        ],
        "website": "https://ndma.gov.in",
    },
    {
        "keywords": ["property tax", "house tax"],
        "title": "Property Tax Payment",
        "details": "Citizens can pay property or house tax online or at local office.",
        "steps": [
            "Open municipal tax portal.",
            "Enter property number.",
            "Check tax amount.",
            "Pay online or at office.",
            "Save receipt.",
        ],
        "website": "https://www.india.gov.in",
    },
    {
        "keywords": ["application status", "pension status", "scheme status"],
        "title": "Application Status Tracking",
        "details": "Citizens can track government service applications using acknowledgement number.",
        "steps": [
            "Open related service portal.",
            "Click application status.",
            "Enter application or acknowledgement number.",
            "Check current status.",
            "Visit local office if delayed.",
        ],
        "website": "https://www.india.gov.in",
    },
    {
        "keywords": ["internet", "network", "mobile network"],
        "title": "Internet and Mobile Network Problem",
        "details": "Guidance for internet and mobile network issues.",
        "steps": [
            "Restart mobile device.",
            "Check signal availability.",
            "Contact service provider.",
            "Use nearby digital service center if needed.",
        ],
        "website": "https://dot.gov.in",
    },
    {
        "keywords": ["emergency", "police", "ambulance", "fire"],
        "title": "Emergency Contacts",
        "details": "Important emergency numbers for public safety.",
        "steps": [
            "Police: 100",
            "Ambulance: 108",
            "Fire Service: 101",
            "Women Helpline: 181",
            "Child Helpline: 1098",
            "National Emergency: 112",
        ],
        "website": "https://112.gov.in",
    },
]

if user_input.strip() == "":
    st.header(translate_text("Welcome to AI Village Help Portal", language))
    st.write(translate_text("Type your issue or service name in the sidebar search box.", language))

    st.write(translate_text("Examples:", language))
    examples = [
        "Aadhaar",
        "Fever",
        "Farmer",
        "Crop Insurance",
        "Scholarship",
        "Garbage",
        "Passport",
        "Water Problem",
        "Land Records",
        "MGNREGA",
        "Women Safety",
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

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        for service in services:
            if any(keyword in query for keyword in service["keywords"]):
                found = True
                st.success(translate_text("Service Found Successfully", language))
                st.header(translate_text(service["title"], language))
                st.info(translate_text(service["details"], language))

                st.subheader(translate_text("🎯 Benefits", language))

                benefits = service.get(
                    "benefits",
                    [
                        "Saves time for villagers",
                        "Provides easy service guidance",
                        "Helps people access public services",
                        "Useful for rural citizens",
                    ],
                )

                for benefit in benefits:
                    st.write("✅ " + translate_text(benefit, language))

                st.subheader(translate_text("📄 Required Documents", language))

                documents = service.get(
                    "documents",
                    [
                        "Aadhaar Card if required",
                        "Mobile Number",
                        "Address Proof if required",
                        "Passport Size Photo if needed",
                    ],
                )

                for document in documents:
                    st.write("📌 " + translate_text(document, language))

                st.subheader(translate_text("👨‍👩‍👧 Eligibility", language))

                eligibility = service.get(
                    "eligibility",
                    [
                        "Indian citizens can use this service",
                        "Valid documents may be required",
                    ],
                )

                for item in eligibility:
                    st.write("✔️ " + translate_text(item, language))

                st.subheader(translate_text("🪜 Detailed Step-by-Step Process", language))

                detailed_steps = []

                for step in service["steps"]:
                    detailed_steps.append(step)
                    detailed_steps.append("Check all details carefully before submission.")
                    detailed_steps.append("Keep acknowledgement receipts safely for future tracking.")
                    detailed_steps.append("Use official government portals or authorized centers only.")

                for index, step in enumerate(detailed_steps, start=1):
                    st.write(f"{index}. " + translate_text(step, language))

                st.subheader(translate_text("💡 Important Tips", language))

                tips = service.get(
                    "tips",
                    [
                        "Use correct mobile number",
                        "Keep application number safely",
                        "Avoid sharing OTP with unknown persons",
                        "Visit nearest office if online process is difficult",
                    ],
                )

                for tip in tips:
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
                    "Try Aadhaar, fever, farmer, crop insurance, scholarship, complaint, passport, water, job, land records, MGNREGA, or emergency.",
                    language,
                )
            )
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Convert image to base64 string
def image_to_base64(path, width=140):
    img = Image.open(path)
    img = img.resize((width, int(width * img.height / img.width)))
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

# Load and convert images
logo_base64 = image_to_base64("99845A80-DBCD-4356-B37A-6F5EE36DFCD7.jpg", width=140)
poster1_base64 = image_to_base64("C38636C4-7A44-4208-9C3E-3BE0CCB9E111.PNG", width=400)
poster2_base64 = image_to_base64("962E8984-7EFB-48B5-9932-07899C9D16D6.PNG", width=400)

# Page config
st.set_page_config(page_title="Open Hearts Summer Night", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #f9d9b0, #ffe4c3);
            color: #000 !important;
        }
        .header {
            text-align: center;
            padding-bottom: 0.5rem;
        }
        .header img {
            width: 140px;
            margin-bottom: 0.3rem;
        }
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: #000 !important;
        }
        .poster-row {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 10px;
        }
        .poster-img {
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Header: logo, title, verse
st.markdown(f"""
    <div class="header">
        <img src="data:image/png;base64,{logo_base64}" />
        <h1>🌟 OPEN HEARTS SUMMER NIGHT</h1>
        <h3>“Sharing the Love of God, Sharing the Gifts of God”</h3>
        <p><strong>📖 1 John 4:19</strong> – “We love because He first loved us.”</p>
    </div>
""", unsafe_allow_html=True)

# Guaranteed-working native video
st.video("youth_open_hearts.mp4")

# Poster image row (collapsible)
with st.expander("🖼️ View Event Posters"):
    st.markdown(f"""
        <div class="poster-row">
            <img class="poster-img" src="data:image/png;base64,{poster2_base64}" width="400">
            <img class="poster-img" src="data:image/png;base64,{poster1_base64}" width="400">
        </div>
    """, unsafe_allow_html=True)

# Event Details
st.markdown("### 📅 Event Details")
st.write("**Date:** Friday, July 11")
st.write("**Time:** 6:00 PM – 12:00 AM")
st.write("**Location:** International Christian Church")

# Program Overview
with st.expander("🗓 Click to View Full Program"):
    program = {
        "6:00 PM": "Doors Open & Registration\n• Name tag • Light refreshments",
        "6:30 PM": "Welcome & Intro\n• Emcee • Theme & verse",
        "6:50 PM": "Ice Breaker 🤝\n• Group game • Led by youth • Small prizes",
        "7:10 PM": "Opening Worship 🎶\n• Worship team • Opening prayer",
        "7:40 PM": "Word 💬\n• Pastor Michael Rhoad • Center on Christ",
        "8:15 PM": "Breakout Sessions 🧩\n• Reflect & pray • Small groups",
        "8:45 PM": "Musical Performances 🎵\n• Youth band • Solo/group numbers",
        "9:25 PM": "Spoken Word & Poetry 🎤\n• Creative faith expressions",
        "9:55 PM": "Testimonies 🙌\n• Transformation stories",
        "10:25 PM": "Worship Finale 🔥\n• Extended worship • Corporate prayer",
        "10:40 PM": "Games 🎉\n• High-energy group games • Team fun",
        "12:00 AM": "Group Photo 📸 & Dismissal\n• Final photo • Thank you & send-off"
    }
    for time, details in program.items():
        st.subheader(time)
        st.markdown(details)

# Why This Night Matters
st.subheader("💛 Why This Night Matters")
st.markdown("""
Let’s go beyond the fun — and reflect on the greatest love of all: the love of Christ.
Let's gather, worship, share, and grow — together!
""")

# Sign-Up and Guidelines
col1, col2 = st.columns(2)
with col1:
    st.subheader("📋 Sign-Up")
    st.markdown("[👉 Fill out the Participation Form](https://docs.google.com/forms/d/e/1FAIpQLSeBfgRe9LTsKQjJ9XwYOGBFwUHQWF3NKoE2LooaeMcn0LCqsQ/viewform?usp=sharing)")

with col2:
    st.subheader("🎤 Performance Guidelines")
    st.markdown("""
    - **Groups:** 2 songs or 10–12 minutes  
    - **Solo:** 5–7 minutes  
    Let's honor each other’s time and showcase our gifts for Christ!
    """)

#save changes
# # Volunteer Section
# with st.expander("🙌 Click to View Volunteer Team"):
#     st.subheader("Volunteer Assignments")
#     volunteers = {
#         "Food & Refreshments": "Jen, Bing, Joy, Lee",
#         "Security": "Ron, Garnet, Jeremy, John",
#         "Registration": "Carmina, Nina",
#         "Music & Sound": "Mark Kalagayan",
#         "Coordinators": "James & Janelle",
#         "Speaker": "Pastor Michael Rhoad",
#         "Worship Team": "KC, Ariel, Sam, Zech, Kayla, Kamie, Jon",
#         "Facilitators": "[]",
#         "Games": "Gomer, Nina",
#         "Photographer": "Ian",
#         "Youth Leads": "Z & Mac",
#         "Social Media": "KC, Ariel",
#         "Video": "Andria, Ariel",
#         "Event Lead": "Mar Esplana"
#     }
#     for role, names in volunteers.items():
#         st.markdown(f"**{role}:** {names}")

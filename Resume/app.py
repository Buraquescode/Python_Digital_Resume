
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Buraque Syed"
PAGE_ICON = ":wave:"
NAME = "Buraque Syed"
DESCRIPTION = """
full-stack developer having grip in html css and javascript where as also working as an android and a python developer.
"""
EMAIL = "buraquescode@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codefixlab",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 I have done an e-commerce website which is fully functional and working nowadays" :"https://youtu.be/Sb0A9i6d320",
    "🏆 I have done an e-commerce website which is fully functional and working nowadays" :"https://youtu.be/Sb0A9i6d320",
    "🏆 I have done an e-commerce website which is fully functional and working nowadays" :"https://youtu.be/Sb0A9i6d320",
    "🏆 I have done an e-commerce website which is fully functional and working nowadays" :"https://youtu.be/Sb0A9i6d320",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ---profile coloum and download button for resume
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 years of exprience in doing internships in diffrent companies of pakistan and india digitally
- ✔️ 2 years of exprience in doing internships in diffrent companies of pakistan and india digitally
- ✔️ 2 years of exprience in doing internships in diffrent companies of pakistan and india digitally
- ✔️ 2 years of exprience in doing internships in diffrent companies of pakistan and india digitally
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
----------------------------------------------
----------------------------------------------
----------------------------------------------
----------------------------------------------
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Web Developer | Softwy Solution**")
st.write("02/2022 - Present")
st.write(
    """
- ► I have wroked in this company as a web developer and love to do the web developement
- ► I have wroked in this company as a web developer and love to do the web developement
- ► I have wroked in this company as a web developer and love to do the web developement
"""
)

# --- JOB 2


# --- JOB 3

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")





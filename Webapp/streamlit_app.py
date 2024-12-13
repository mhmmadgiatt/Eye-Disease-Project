import streamlit as st

# Fungsi untuk memuat CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call Fungsi load_css
load_css("style/style.css")

# Setup Page
home_page = st.Page(
    "views/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
model_1_page = st.Page(
    "views/test_resnet50.py",
    title="Test using ResNet50",
    icon=":material/mystery:",
)
model_2_page = st.Page(
    "views/test_vgg16.py",
    title="Test using VGG16",
    icon=":material/symptoms:",
)
info_resnet50 = st.Page(
    "views/about_resnet50.py",
    title="About Model Resnet50",
    icon=":material/info:",
)
info_vgg16 = st.Page(
    "views/about_vgg16.py",
    title="About Model VGG16",
    icon=":material/info:",
)

# Navigasi Pages
pg = st.navigation(
    {
        "Home Page": [home_page],
        "Model Using": [model_1_page, model_2_page],
        "Information": [info_resnet50, info_vgg16],
    }
)

# Logo EyeCheck.AI
st.logo("assets/eye_check.png")

# Run Page
pg.run()

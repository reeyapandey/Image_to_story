css_code = """
<style>

/* FORCE ALL TEXT TO BLACK */
html, body, [class*="css"] {
    color: black !important;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #ffc0cb, #ffe4ec);
}

/* Headings */
h1 {
    color: #8b004f !important;
    text-align: center;
    font-size: 36px;
}

h2, h3 {
    color: black !important;
    text-align: center;
}

/* Upload box */
[data-testid="stFileUploader"] {
    border: 2px dashed #ff69b4;
    padding: 20px;
    border-radius: 15px;
    background-color: #fff0f5;
}

/* Buttons */
.stButton>button {
    background-color: #ff69b4;
    color: white !important;
    border-radius: 10px;
    padding: 10px 20px;
}

/* CUSTOM BOX */
.custom-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-top: 20px;
}

/* TITLE INSIDE BOX */
.custom-box h3 {
    color: black !important;
    font-size: 24px;
    font-weight: bold;
}

/* TEXT INSIDE BOX */
.custom-box p {
    color: black !important;
    font-size: 15px;
    font-weight: bold;
}

/* ALSO FIX STREAMLIT TEXT ELEMENTS */
.stMarkdown, .stText, .stWrite {
    color: black !important;
    font-weight: bold !important;
}

</style>
"""
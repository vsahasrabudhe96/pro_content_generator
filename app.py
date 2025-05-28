import streamlit as st
from email_writer import generate_email
from document_writer import generate_technical_doc
from summarizer import summarize_content
from file_reader import read_file
from web_summarizer import summarize_website

if "email_output" not in st.session_state: st.session_state.email_output = ""
if "doc_output" not in st.session_state: st.session_state.doc_output = ""
if "summary_output" not in st.session_state: st.session_state.summary_output = ""
if "url_output" not in st.session_state: st.session_state.url_output = ""

if "email_input" not in st.session_state: st.session_state.email_input = ""
if "doc_input" not in st.session_state: st.session_state.doc_input = ""
if "summary_input" not in st.session_state: st.session_state.summary_input = ""
if "url_input" not in st.session_state: st.session_state.url_input = ""


st.set_page_config(page_title="🤖 AI Content Assistant", layout="centered")
st.title("🤖 AI Content Assistant")
tab1, tab2, tab3, tab4 = st.tabs([
    "✉️ Email Generator",
    "📄 Technical Doc Writer",
    "🧠 Summarizer",
    "🌐 Summarize from URL"
])

def get_text_or_file(tab_key):
    # st.markdown("**Upload a .txt, .pdf, or .docx file (Max 20MB)**", unsafe_allow_html=True)

    # Hide Streamlit's default file size message via CSS
    st.markdown(
        """
        <style>
        .stFileUploader > div > div > span {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Optional: Upload a .txt, .pdf, or .docx file",
        type=["txt", "pdf", "docx"],
        key=f"file_{tab_key}"
    )

    if uploaded_file:
        max_size_mb = 20
        if uploaded_file.size > max_size_mb * 1024 * 1024:
            st.error(f"File too large. Limit is {max_size_mb}MB.")
            return ""
        return read_file(uploaded_file)
    else:
        return st.text_area("Or paste content below:", key=f"text_{tab_key}")



# --- Email Tab ---
with tab1:
    st.subheader("✉️ Generate a Professional Email")
    email_input = get_text_or_file("email")
    st.session_state.email_input = email_input

    col1, col2 = st.columns([1, 1])
    if col1.button("Generate Email", key="gen_email"):
        if not email_input.strip():
            st.warning("Please provide input.")
        else:
            with st.spinner("Generating email..."):
                st.session_state.email_output = generate_email(email_input)

    if col2.button("Generate Another Email", key="regen_email"):
        if not st.session_state.email_input.strip():
            st.warning("No previous input found.")
        else:
            with st.spinner("Regenerating..."):
                st.session_state.email_output = generate_email(st.session_state.email_input)

    if st.session_state.email_output:
        st.text_area("Generated Email", st.session_state.email_output, height=300)


# --- Tech Doc Tab ---
with tab2:
    st.subheader("📄 Generate Technical Documentation")
    doc_input = get_text_or_file("doc")
    st.session_state.doc_input = doc_input

    col1, col2 = st.columns([1, 1])
    if col1.button("Generate Documentation", key="gen_doc"):
        if not doc_input.strip():
            st.warning("Please provide input.")
        else:
            with st.spinner("Generating documentation..."):
                st.session_state.doc_output = generate_technical_doc(doc_input)

    if col2.button("Generate Another Document", key="regen_doc"):
        if not st.session_state.doc_input.strip():
            st.warning("No previous input found.")
        else:
            with st.spinner("Regenerating..."):
                st.session_state.doc_output = generate_technical_doc(st.session_state.doc_input)

    if st.session_state.doc_output:
        st.text_area("Generated Documentation", st.session_state.doc_output, height=300)


# --- Summarizer Tab ---
with tab3:
    st.subheader("🧠 Summarize Notes or Documents")
    summary_input = get_text_or_file("summary")
    st.session_state.summary_input = summary_input

    col1, col2 = st.columns([1, 1])
    if col1.button("Generate Summary", key="gen_summary"):
        if not summary_input.strip():
            st.warning("Please provide input.")
        else:
            with st.spinner("Generating summary..."):
                st.session_state.summary_output = summarize_content(summary_input)

    if col2.button("Generate Another Summary", key="regen_summary"):
        if not st.session_state.summary_input.strip():
            st.warning("No previous input found.")
        else:
            with st.spinner("Regenerating..."):
                st.session_state.summary_output = summarize_content(st.session_state.summary_input)

    if st.session_state.summary_output:
        st.text_area("Summary", st.session_state.summary_output, height=300)


with tab4:
    st.subheader("🌐 Summarize Content from a URL")
    url = st.text_input("Enter a URL to summarize", key="url_input_field")
    st.session_state.url_input = url

    col1, col2 = st.columns([1, 1])
    if col1.button("Summarize Website", key="gen_web_summary"):
        if not url.strip():
            st.warning("Please enter a valid URL.")
        else:
            with st.spinner("Fetching and summarizing..."):
                st.session_state.url_output = summarize_website(url)

    if col2.button("Generate Another Summary", key="regen_web_summary"):
        if not st.session_state.url_input.strip():
            st.warning("No previous URL found.")
        else:
            with st.spinner("Regenerating..."):
                st.session_state.url_output = summarize_website(st.session_state.url_input)

    if st.session_state.url_output:
        st.text_area("Webpage Summary", st.session_state.url_output, height=300)


st.markdown("Created by Varun Sahasrabudhe")
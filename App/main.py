import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            st.info("🔄 Loading job description from URL...")
            data = clean_text(loader.load().pop().page_content)

            st.info("🧠 Loading portfolio...")
            portfolio.load_portfolio()

            st.info("📄 Extracting job details...")
            jobs = llm.extract_jobs(data)

            if not jobs:
                st.warning("⚠️ No jobs found in the given page.")
                return

            for i, job in enumerate(jobs):
                st.subheader(f"Job #{i+1}")
                skills = job.get('skills', [])

                st.write(f"🔍 Matching portfolio links for skills: `{skills}`")
                links = portfolio.query_links(skills)

                st.write("✉️ Generating cold email...")
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')

        except Exception as e:
            import traceback
            st.error(f"❌ An Error Occurred: {e}")
            st.text(traceback.format_exc())


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

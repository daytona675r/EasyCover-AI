import streamlit as st
from openai import AsyncOpenAI
from firecrawl import FirecrawlApp
import os
from dotenv import load_dotenv
import asyncio
from src.core import process_cover_letter_request


# Load environment variables
load_dotenv()

# Initialize API clients
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
firecrawl_client = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))



def main():
    st.set_page_config(
        page_title="EasyCover AI", page_icon="✨", layout="centered"
    )

    with st.sidebar:
        os.environ["OPENAI_API_KEY"] = st.text_input("OpenAI API Key", key="openai_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        os.environ["FIRECRAWL_API_KEY"] = st.text_input("Firecrawl API Key", key="firecrawl_api_key", type="password")
        "[Get an Firecrawl API key](https://docs.firecrawl.dev/introduction#api-key)"
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/5_Chat_with_user_feedback.py)"

        # Add helpful instructions
        with st.expander("ℹ️ How to use"):
            st.write(
                """
            1. Upload your resume in PDF format
            2. Paste the URL of the job posting you're interested in
            3. Click 'Create Cover Letter'
            4. View, copy, or download your customized cover letter
            """
            )

    st.title("✨ EasyCover AI")
    st.write(
        "Upload your resume and provide the URL for the job posting to generate your customized cover letter."
    )

    # Input section
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    with col2:
        job_url = st.text_input("Enter job posting URL")

    if st.button("Create Cover Letter", type="primary"):
        # Check if the OpenAI and FirecrawlAPI key is set
        if not os.environ["OPENAI_API_KEY"]:
                    st.info("Please add your OpenAI API key to continue.")
                    st.stop()

        if not os.environ["FIRECRAWL_API_KEY"]:
            st.info("Please add your Firecrawl API key to continue.")
            st.stop()

        if uploaded_file is not None and job_url:
            try:
                # Create a placeholder for the progress messages
                progress_placeholder = st.empty()

                async def process_with_status():
                    # Step 1: Processing PDF
                    progress_placeholder.info("📄 Processing your resume...")

                    # Step 2: Parallel Processing
                    progress_placeholder.info("🔍 Analyzing resume and job posting...")

                    cover_letter = await process_cover_letter_request(
                        uploaded_file, job_url, openai_client, firecrawl_client
                    )

                    # Step 3: Final Generation
                    progress_placeholder.info("✍️ Creating your cover letter...")

                    return cover_letter
                

                # Run the async function
                cover_letter = asyncio.run(process_with_status())

                if cover_letter:
                    # Clear the progress message
                    progress_placeholder.empty()

                    # Display success and results
                    st.success("✨ Your cover letter has been created!")

                    # Create tabs for different views
                    tab1, tab2 = st.tabs(["📄 View", "📋 Copy & Download"])

                    with tab1:
                        st.markdown("### Your Cover Letter")
                        st.markdown(cover_letter)

                    with tab2:
                        st.text_area(
                            "Copy your cover letter", value=cover_letter, height=400
                        )

                        # Single download button for TXT
                        st.download_button(
                            label="📥 Download as TXT",
                            data=cover_letter,
                            file_name="cover_letter.txt",
                            mime="text/plain",
                            help="Click to download your cover letter as a text file",
                        )

                else:
                    progress_placeholder.empty()
                    st.error("Failed to generate cover letter. Please try again.")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please upload a PDF resume and provide a job posting URL.")

    


if __name__ == "__main__":
    main()

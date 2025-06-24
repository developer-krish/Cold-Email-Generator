import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-8b-instant"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### INSTRUCTION:
            This text is from a career/job listing page.
            Extract job postings and return them in JSON format with keys:
            - `role`: Job title
            - `experience`: Years of experience or entry-level/etc.
            - `skills`: Look for phrases like "Qualifications", "Required skills", or "You should have"
            - `description`: Full description of the role

            If a section is not available, try to infer it or use "Not specified".
            ### RETURN VALID JSON ONLY (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm
        json_parser = JsonOutputParser()

        try:
            # ✅ Step 1: Get response from LLM
            response = chain_extract.invoke({"page_data": cleaned_text})

            # ✅ Step 2: Parse the content
            res = json_parser.parse(response.content)

        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")

        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Vaishnavi Gupta, a SWE intern at Microsoft. Microsoft specializes in AI and Software Engineering.
            Your task is to write a cold email to a potential client regarding the job mentioned above, focusing on how Microsoft can help them achieve goals and address their specific needs.
            Use the job description to tailor your message, and include relevant achievements or case studies from Microsoft to build credibility.
            Also add the most relevant ones from the following links to showcase Microsoft's portfolio: {link_list}

            Do not include a preamble.

            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))

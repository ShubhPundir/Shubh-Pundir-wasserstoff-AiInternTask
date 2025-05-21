from typing import List
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.core.llm import get_gemini_llm

def extract_themes_from_document(document_content: str) -> List[str]:

    # Initialize Gemini LLM
    llm = get_gemini_llm()

    # Prompt to extract multiple themes from a document
    THEME_PROMPT_TEMPLATE = """
    You are an AI assistant helping categorize documents.
    Given the following document content, identify and return 2 to 5 high-level themes that describe its content.
    Each theme should be 1 to 3 words long. Respond with a comma-separated list only.

    Document Content:
    {document_content}

    Themes:
    """

    prompt = PromptTemplate(
        input_variables=["document_content"],
        template=THEME_PROMPT_TEMPLATE
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    raw_output = chain.invoke({"document_content": document_content})
    themes = [theme.strip() for theme in raw_output.split(",") if theme.strip()]
    return themes
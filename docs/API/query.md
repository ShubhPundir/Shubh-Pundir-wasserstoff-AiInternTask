# 📄 API Documentation – `query.py`

This module provides an endpoint to submit a natural language query which is processed against uploaded documents. It returns a synthesized answer along with citations referencing the source documents and locations within them.

---

## ✅ `/query/`

- **HTTP Method**: `POST`
- **Description**: Accepts a query string, processes it using document semantic search and synthesis logic, and returns a detailed, cited answer.
- **Request Body**:
  - `query: str` — The user’s natural language query.

### 🔄 Workflow Details

1. Receives the query as JSON.
2. Uses the internal `query_documents` service to:
   - Search relevant documents in the vector store.
   - Extract and synthesize an answer.
   - Provide citations for referenced documents and text locations.
3. Returns the synthesized answer with citations in JSON format.
4. Handles exceptions with HTTP 500 status on failure.

### 📤 Sample Input

```json
{
  "query": "What tasks are to be completed in Wasserstoff"
}
```

### 📤 Sample Output
```json
{
  "answer": {
    "synthesized_answer": "Wasserstoff is offering a 6-month, full-time AI internship focused on Generative AI.  The intern will build a chatbot capable of researching and identifying themes across 75+ uploaded documents (PDFs, scanned images accepted).  The chatbot must provide cited answers to user queries.  Required skills include Python, experience with Transformers/LLMs, LangChain, OpenAI API, system design, and basic SQL/NoSQL database knowledge.  Divyansh Sharma (divyansh.sharma@thewasserstoff.com) is the contact person.  The chatbot will be deployed using one of the following platforms: Render, Railway, Replit, Hugging Face Spaces, or Vercel.",
    "citations": [
      {
        "Document ID": "682e1a3d0ab0f7a88736959a",
        "Extracted Answer": "Company: Wasserstoff \nRole: AI Intern (Generative AI) – Full-Time, 6 Month Internship \nFocus: Research-based implementation of Generative AI tools and applications (mix of \nresearch and real product development) \nRequired Skills: Python; Transformers and LLM architecture; LangChain framework; \nOpenAI API usage; system design fundamentals; basic database knowledge \n(SQL/NoSQL) \n \nInternship Task: Document Research & Theme Identification Chatbot \nObjective:",
        "Citation": "Page 1, Para 1"
      },
      {
        "Document ID": "682e1a3d0ab0f7a88736959a",
        "Extracted Answer": "●​ Render​\n \n●​ Railway​\n \n●​ Replit​\n \n●​ Hugging Face Spaces​\n \n●​ Vercel​\n \n \nContact \nFor any questions during the internship or to submit your deliverables, please reach out \nto: \nDivyansh Sharma – Wasserstoff​\n Email: divyansh.sharma@thewasserstoff.com",
        "Citation": "Page 5, Para 1"
      },
      {
        "Document ID": "682e1a3d0ab0f7a88736959a",
        "Extracted Answer": "AI Software Intern – Internship Task Document \nInternship Role Overview \nAs an AI Intern for 6 months (full-time), you will engage in research-driven development \nof Generative AI applications. The internship emphasizes both academic research and \nhands-on implementation, contributing to real product development, exploring research \npapers, and building internal tools. \nCompany: Wasserstoff \nRole: AI Intern (Generative AI) – Full-Time, 6 Month Internship",
        "Citation": "Page 1, Para 1"
      },
      {
        "Document ID": "682e1a3d0ab0f7a88736959a",
        "Extracted Answer": "(SQL/NoSQL) \n \nInternship Task: Document Research & Theme Identification Chatbot \nObjective: \nCreate an interactive chatbot that can perform research across a large set of documents \n(minimum 75 documents), identify common themes (multiple themes are possible), and \nprovide detailed, cited responses to user queries. \n \nTask Breakdown: \n1. Document Upload and Knowledge Base Creation: \n●​ Allow users to upload 75+ documents in various formats including PDF and \nscanned images.​",
        "Citation": "Page 1, Para 1"
      }
    ]
  }
}

```

### ❗ Error Responses
500 Internal Server Error: Query processing failure or unexpected errors.


### ⚙️ Implementation Notes
The endpoint expects a JSON payload with a single query string.

The query_documents service handles semantic search, answer synthesis, and citation extraction.

Returned citations include document IDs and text snippet locations (page, paragraph).

Exception handling ensures graceful failure reporting.
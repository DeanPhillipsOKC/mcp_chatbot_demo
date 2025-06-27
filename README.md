# MCP Chatbot Demo

This repository is a proof of concept for a payroll-related chatbot application built using Streamlit. The chatbot interacts with users to answer payroll-related questions and integrates with Azure OpenAI services.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd detroit_mcp_poc
   ```

3. Install the [UV Package Manager](https://docs.astral.sh/uv/getting-started/installation/)

2. Install dependencies:
   ```bash
   uv sync
   ```

## Running the Application

1. Start the application:
   ```bash
   uv run streamlit run app.py
   ```

2. Open the Streamlit app in your browser at `http://localhost:8501`.

## Environment Setup

1. Rename the file to `.env`:
   ```bash
   mv dot-env .env
   ```

   - Replace `<oracle database username>` with the Oracle database username / schema owner
   - Replace `<oracle database password>` with the Oracle database password

## License

Add your license information here.
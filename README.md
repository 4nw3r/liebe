# LIEBE

Welcome to the RAG Chatbot with powered by a self-hosted LLM project! This project leverages Streamlit for a user-friendly interface and various LangChain components to provide an intelligent document querying system.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This AI-powered assistant helps users search and articulate information from documents, focusing on PDF files. It uses advanced language models and text-processing techniques to provide accurate and contextually relevant answers.

## Features

- **User-Friendly Interface**: Interact with the assistant through a web-based Streamlit app.
- **Chat History**: Maintains a history of user queries and responses.
- **Document Upload**: Upload PDF files for querying.
- **Custom Prompts**: Uses a custom prompt template for generating accurate responses.
- **Scalable and Robust**: Designed to scale horizontally and handle various edge cases.

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/ai-powered-assistant.git
    cd ai-powered-assistant
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    streamlit run ollama_api.py
    ```

## Usage

### Starting the App

1. Run the Streamlit app:
    ```bash
    streamlit run ollama_api.py
    ```

2. Open your browser and navigate to `http://localhost:8501`.

### Uploading a PDF

1. Navigate to the **Upload PDF** section.
2. Choose a PDF file and upload it.
3. The file will be saved and processed for querying.

### Querying

- **General Queries**:
    - Enter your query in the input box and click "Submit Query".
    - The assistant will provide a response based on the available information.
- **PDF Queries**:
    - Enter your query specific to the uploaded PDF in the input box under "Ask PDF".
    - The assistant will retrieve relevant information from the PDF and display it along with the sources.

## API Endpoints

### General Query

- **Endpoint**: `/ai`
- **Method**: POST
- **Payload**: `{ "query": "<your_query>" }`
- **Response**:
    ```json
    {
        "answer": "<response>"
    }
    ```

### PDF Query

- **Endpoint**: `/ask_pdf`
- **Method**: POST
- **Payload**: `{ "query": "<your_query>" }`
- **Response**:
    ```json
    {
        "answer": "<response>",
        "sources": [
            {
                "source": "<source_name>",
                "page_content": "<content>"
            }
        ]
    }
    ```

## Troubleshooting

### Common Issues

1. **Server Not Starting**:
    - **Cause**: Dependencies not installed or incorrect Python version.
    - **Solution**: Ensure all dependencies are installed and you are using Python 3.7+.

2. **No Response from AI**:
    - **Cause**: Local server not running.
    - **Solution**: Verify that the local server is running and accessible.

3. **PDF Upload Issues**:
    - **Cause**: File not saved or processed correctly.
    - **Solution**: Check the file path and permissions. Ensure the server can read and write to the specified directory.

### Logs and Monitoring

- Use `streamlit logs` to view the application logs for debugging purposes.
- Implement real-time monitoring with tools like Prometheus and Grafana for better insights.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your fork.
4. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the AI-Powered Technical Assistant! If you have any questions or feedback, feel free to open an issue or reach out to us.

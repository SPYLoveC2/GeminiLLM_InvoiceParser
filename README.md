# GeminiLLM_InvoiceParser

## Overview
**GeminiLLM_InvoiceParser** is a Streamlit-based web application that leverages Google's Gemini LLM to extract and process information from invoice images. Users can upload an invoice image, input a query, and receive AI-generated responses based on the provided prompt and image content.

## Features
- Upload invoice images in **JPG, JPEG, or PNG** format
- Utilize Google's **Gemini LLM** models for intelligent processing
- Interactive query input for extracting specific details
- Real-time streaming responses for better user experience

## Prerequisites
Ensure you have the following installed before running the application:

- Python 3.8+
- Streamlit
- Google Generative AI SDK
- Pillow (PIL)
- Python dotenv

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/SPYLoveC2/GeminiLLM_InvoiceParser.git
   cd GeminiLLM_InvoiceParser
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up API Key:
   - Create a `.env` file in the root directory.
   - Add your **Google API Key**:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

2. Open the web application in your browser and:
   - Upload an invoice image.
   - Enter a query to extract specific information.
   - Click **Ask Me** to receive a response.

## File Structure
```
GeminiLLM_InvoiceParser/
│── app.py              # Main application script
│── template.py         # System prompt template file
│── .env                # API key storage (not committed)
│── requirements.txt    # Dependencies list
│── README.md           # Documentation
```

## Supported Models
The application supports the following Google Gemini models:
- `gemini-1.5-pro`
- `gemini-2.0-flash`
- `gemini-1.5-flash-latest`
- `gemini-2.0-pro-exp`

By default, **Gemini 1.5 Pro** is used for optimal performance.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and open a Pull Request.

## License
This project is licensed under the **MIT License**.

## Contact
For any queries, reach out via GitHub Issues or email **your-email@example.com**.


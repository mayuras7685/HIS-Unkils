# Food Complaint Resolution Application

The Food Complaint Resolution Application is an AI-based customer complaint system tailored to the food delivery industry. It aims to streamline the process of addressing customer complaints by leveraging state-of-the-art AI models and automation. Traditional complaint resolution processes often involve human intervention, which can be time-consuming and dependent on the availability of personnel. This application seeks to automate and expedite the complaint resolution process, thereby enhancing customer satisfaction and operational efficiency.

## Hosted Platforms

The Food Complaint Resolution Application is hosted on the following platforms:

### Clarifai [Clarifai - Customer Complaint Handler](https://clarifai.com/mayuras7685/Hack-it-Sapiens/installed_module_versions/customer-complaint-handler)

### Lightning AI [Lightning AI - Food Complaint Resolution](https://8501-01hr6mr9sh869vbn7jwhdffscm.cloudspaces.litng.ai)


## Features

- **AI-driven Complaint Processing**: Utilizes AI models for complaint processing, reducing human effort and time.
- **User-friendly Interface**: Allows users to select the item, write a description, and upload images of food for complaint submission.
- **Validation of Inputs**: Complaints are processed only when all required inputs are provided by the user.
- **Food Item Recognition**: Utilizes the Food Item Recognition model to identify food items in uploaded images.
- **GPT-4 Turbo Integration**: Validates selected categories and images using the GPT-4 Turbo language model.
- **GPT-4 Vision**: Analyzes complaint descriptions using the GPT-4 Vision model.
- **Automated Resolution**: Provides cashback or discounts based on company policies.
- **Maximum Try Limit**: Sets a limit on the number of attempts allowed for automated resolution.
- **Human Intervention**: Redirects complaints to human agents after exceeding the maximum try limit for personalized resolution.
- **Real-time Updates**: Provides real-time updates on the processing stage and response (% cashback) to users.

## Built with

- **Clarifai's Streamlit Module**: A template for creating a UI module with Clarifai using Streamlit.
- **Food Item Recognition**: AI model for recognizing a wide variety of food items in images.
- **GPT-4 Turbo**: Advanced language model (LLM) for validating inputs and categories.
- **GPT-4 Vision**: Extends GPT-4's capabilities to understand and answer questions about images.

## Installation

To install and run the Food Complaint Resolution Application locally, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/mayuras7685/HIS-Unkils
   ```

2. **Change Directory**:
   ```
   cd Streamlit-app
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```
   streamlit run app.py
   ```

Make sure to create or update the `.env` file with your `CLARIFAI_PAT` or provide the Personal Access Token (PAT) through the UI on the application.

## Usage

The Food Complaint Resolution Application simplifies the complaint process using the Streamlit library. Users can select their issue, provide details, and upload photos of the food items in question. The system swiftly processes complaints, providing real-time updates on the processing stage and response (percentage cashback). After reaching the maximum number of attempts, if the user remains unsatisfied, complaints are redirected to human intervention. The application offers an efficient and user-friendly interface, blending automated resolution with personalized human assistance for enhanced customer satisfaction.

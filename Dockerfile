# Use the official Streamlit image as a base
FROM streamlit/streamlit:latest

# Install wkhtmltopdf
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy everything to the working directory
COPY . /app

# Set the working directory
WORKDIR /app

# Install required Python packages
RUN pip install -r requirements.txt

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]


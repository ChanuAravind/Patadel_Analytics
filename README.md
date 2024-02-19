```
# Patadel_Analytics
Assignment for Machine Learning

Task : Develop a semantic search feature that retrieves documents by performing a query on the text content (all fields) within the documents.
Implementation steps:
      
      Step 1: Read and Analyze Data
              - Unzip 'patent_jsons_ML Assignment.zip' and analyze its content.
      Step 2: Data Processing
              - Extract English language data.
              - Perform text preprocessing using 'JSON_Preprocessing_ZIP.ipynb'.
              - Export the preprocessed data as a zip file ('cleaned_df.zip').
      Step 3: Flask app
              - Create a Flask app that reads 'cleaned_df.zip'.
              - Perform semantic search over the query and return relevant patents.
                Run Flask app           : flask run
      Step 4: Docker Containerization
             - Create a Docker container with scaling using 'nginx.conf' (scales up to 3 instances).
               Initialize containers    : docker-compose up -d --build --scale app=3
               Shut down containers     : docker-compose down
               Check running containers : docker ps
      ==================================================================================================================
      
      Accessing the Application:  1. Flask
                                  2. Streamlit

      1. Flask:
           --> Open terminal
           --> Run Flask : flask run
           --> Access the application : http://127.0.0.1:5000/search?query={replace with the query}
      2. Streamlit:
           --> Open terminal
           --> Run Streamlit : streamlit run streamlit_app.py
           --> Access the application   :   Local URL   : http://localhost:8501
                                            Network URL : http://192.168.0.119:8501
           --> Enter the query in the search box and hit search.

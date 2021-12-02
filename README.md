# flood-forecast
01219335 - Data Acquisition and Integration Flood problem project

Panitan Plengkham          6210545521  Software and knowledge engineering Kasetsart University
Sirapop Kunjiak            6210546447  Software and knowledge engineering Kasetsart University
Sarocha Sittipon           6210546439  Software and knowledge engineering Kasetsart University


## Installation
1. Clone the repo
   ```sh
   git clone https://github.com/bemyXmas/flood-forecast-api.git
   ```
2. Change directory
    ```sh
   cd flood-forecast-api
   ```
3. Install required libraries
   ```sh
   pip install -r requirements.txt
   ```
4. Install OpenAPI-to-GraphQL
   ```sh
   npm install -g openapi-to-graphql-cli@2.5.0
   ```
5. Edit `config.py` to access to a database
   ```
    OPENAPI_AUTOGEN_DIR = 'autogen'
    DB_HOST = "iot.cpe.ku.ac.th"
    DB_USER = "b6210546447"
    DB_PASSWD = "sirapop.ku@ku.th"
    DB_NAME = "b6210546447"
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
1. Start the REST API server
   ```sh
   python app.py
   ```
   - swagger tool on http://localhost:8080/speed/v1/ui
2. Start openapi-to-graphql in another terminal
   ```sh
   openapi-to-graphql --cors -u http://localhost:8080/flood-forecast-api openapi/flood-api.yaml
   ```
   -  GraphQL on http://localhost:3000/graphql
3. Open the index page in `html\index.html`

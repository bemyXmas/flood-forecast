# flood-forecast
01219335 - Data Acquisition and Integration Flood problem project

Panitan Plengkham          6210545521  Software and knowledge engineering Kasetsart University


Sirapop Kunjiak            6210546447  Software and knowledge engineering Kasetsart University


Sarocha Sittipon           6210546439  Software and knowledge engineering Kasetsart University


### Project Overview
There’s a big flood in Thailand before like year 2554.
And there’s also a frequent flood in Thai around this
Time of the year and even if Thai have a lot of flood
data collection but there’s a still a few API for our 
country

This API provides information about flood happening in Thailand:

- Water level in the dam data from EGAT.
- Flood forecast data from Department of Water Resource.
- Weather Forecasting from Openweather API.
- Rainfall data gathered by our group in Google form.


### API features
![unknown (1)](https://user-images.githubusercontent.com/59832742/145714681-dbd8add7-f0e8-4e6e-b861-f39a63d63d9c.png)
![unknown (2)](https://user-images.githubusercontent.com/59832742/145714693-fd73d1d3-9242-4cc9-b041-3eab7f1b0d54.png)





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

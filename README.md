# MLDS_sprint9

## Task 1. Basic Web Scraping and JSON Storage

Create a Python script that performs basic web scraping on a Wikipedia page to extract specific information and then saves this information in a JSON file.

**Tasks:**

1. **Fetch a Wikipedia Page:**
   - Write a Python function that retrieves the HTML content of the Wikipedia page for "Web scraping" using the `requests` library.

2. **Extract the Page Title:**
   - Write a Python function that parses the HTML content using `BeautifulSoup` and extracts the title of the page (`<h1>` element with `id="firstHeading"`).

3. **Extract the First Sentence of the First Paragraph:**
   - Write a Python function that extracts the first sentence from the first paragraph (`<p>` element) on the page.

4. **Store the Extracted Information in a JSON File:**
   - Write a Python function that saves the extracted title and first sentence into a JSON file.

**Expected JSON Output:**

The JSON file should contain the following structure:

```json
{
    "title": "Web scraping",
    "first_sentence": "Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites."
}
```

**Implementation Details:**

- **Libraries Used:** `requests`, `BeautifulSoup`, `json`, `pytest`
- **Testing:** Use `pytest` to implement unit tests for each function.
- **File Handling:** The extracted data should be saved to a JSON file named `extracted_wikipedia_data.json`.



## Task 2: Collecting Weather Data Using Open-Meteo API

Learn how to collect weather data using the Open-Meteo API and save the extracted data into a JSON file.

### Task Description:

1. **Fetch Weather Data:**
   - Write a Python script that sends a request to the Open-Meteo API using the provided endpoint:
     - URL: `https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&daily=temperature_2m_max&timezone=Asia/Tokyo`
   - This URL fetches the maximum temperature forecast for Tokyo (latitude 35.6895, longitude 139.6917).

2. **Extract the Maximum Temperature:**
   - Extract the `temperature_2m_max` value from the JSON response. This represents the maximum temperature for the next day in Tokyo.

3. **Save the Extracted Data:**
   - Save the extracted temperature data into a JSON file named `tokyo_weather.json`.

### JSON Output Example:

The JSON file might look like this:

```json
{
    "date": "2024-08-18",
    "max_temperature": 32.5
}
```

## Task 3: Advanced Parsing, Analyzing, and Reporting on Complex Weather Data

Create a Python script that loads, parses, and analyzes complex weather data stored in a JSON file. The script should perform multiple analyses over several days and generate detailed reports summarizing the findings.

### Task Description:

1. **Load the JSON Data:**
   - Write a Python script that loads weather data from a JSON file named `tokyo_weather_complex.json`.

2. **Parse the JSON Data:**
   - Extract relevant information from the JSON data, including:
     - City name, geographical coordinates (latitude, longitude), and timezone.
     - Daily weather data, including the date, maximum and minimum temperatures, precipitation, wind speed, humidity, and a short weather description.

3. **Perform Multiple Analyses:**
   - **Temperature Analysis:** For each day, check if the maximum temperature exceeds a specified threshold (e.g., 30°C) and determine if it’s a hot day.
   - **Temperature Swing Analysis:** Calculate the difference between the maximum and minimum temperatures for each day. Determine if there was a significant temperature swing (e.g., more than 10°C).
   - **Wind Analysis:** Check if the wind speed exceeded a specified threshold (e.g., 15 km/h) and determine if it was a windy day.
   - **Humidity and Comfort Analysis:** Assess the humidity level and determine if the day was likely to be uncomfortable (e.g., if humidity is over 70%).
   - **Precipitation Analysis:** Identify rainy days and determine the severity of the rain (e.g., light, moderate, or heavy rain based on precipitation levels).

4. **Generate Detailed Reports:**
   - For each day, generate a detailed report that summarizes the findings from the analyses. The report should include:
     - The date and weather description.
     - An assessment of whether it was a hot day, the significance of the temperature swing, whether it was windy, and whether the humidity made the day uncomfortable.
     - Information on whether it was a rainy day or if there was no precipitation.
   - Provide a summary report that highlights:
     - The hottest day.
     - The windiest day.
     - The most humid day.
     - The day with the most precipitation.

**The output**
```
Date: 2024-08-18
Weather: Clear sky
Temperature: Max 10.0°C
It was a hot day.
It was a windy day.
There was no precipitation.

Date: 2024-08-19
Weather: Light rain
Temperature: Max 9.0°C
It was a rainy day.

Date: 2024-08-20
Weather: Moderate rain
Temperature: Max 8.0°C
The humidity made the day uncomfortable.
It was a rainy day.

Date: 2024-08-21
Weather: Sunny
Temperature: Max 9.0°C
It was a hot day.
It was a windy day.
There was no precipitation.

Weather Summary:
Hottest day: 2024-08-18 with a maximum temperature of 10.0°C
Windiest day: 2024-08-18 with wind speeds of True km/h
Most humid day: 2024-08-20 with a humidity level of True%
Rainiest day: 2024-08-19 with True mm of precipitation
```






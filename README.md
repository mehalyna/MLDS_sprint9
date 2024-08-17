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

**Objective:**  
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




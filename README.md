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


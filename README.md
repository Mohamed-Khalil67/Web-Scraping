Here's a professionally rewritten version of your README.md with clear structure, corrected grammar, and improved technical clarity:

---

# Web Scraping Project: Amazon Price Tracker

## Project Objective
Develop a Python script to automatically extract and monitor pricing data for Raspberry Pi 4 devices from Amazon.fr.

## Technical Specifications

### Target Website
- **Amazon.fr**: [https://www.amazon.fr/](https://www.amazon.fr/)
- **Target Product**: Raspberry Pi 4 (Monitoring price fluctuations for embedded systems components)

### Scraping Tool Selection
**Selenium** was chosen because it enables:
- Interactive browser automation (button clicks, page scrolling)
- Multi-page navigation
- Robust element location strategies

### Implementation Approach

#### Data Collection
1. Search for "Raspberry Pi 4" products on Amazon
2. Extract the following product attributes:
   - Product name
   - ASIN (Amazon Standard Identification Number)
   - Current price
   - Customer rating
   - Rating count
   - Product URL

#### Technical Process
- HTML parsing using Selenium's `find_element`/`find_elements` methods
- Data storage in lists during iteration
- Persistent storage in `amazon_search.db` SQLite database

#### Performance Considerations
- Implemented 5-second implicit waits (`driver.implicitly_wait(5)`) between page interactions
- Randomized delay intervals to prevent bot detection

### Development Workflow
1. **Prototyping**: Initial testing in Jupyter Notebook (.ipynb)
2. **Modularization**: Refactored into functional components in `app.py`
   - `scrape_amazon()` main function with configurable:
     - Page count
     - Search keyword
3. **Containerization**:
   - Selenium Standalone Chrome container
   - Python script container (planned network bridge not implemented)

### Data Significance
Raspberry Pi 4 was selected due to:
- Notable price volatility in embedded systems market
- High demand creating interesting pricing patterns

### Future Improvements
- Implement inter-container communication
- Add price change visualization
- Develop Flask dashboard for data presentation

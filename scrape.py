import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL for Simplify ETFs
BASE_URL = "https://www.simplify.us/etfs"

# Directory to store downloaded PDFs
PDF_DIR = "simplify_portfolio/simplify_prospectuses"
os.makedirs(PDF_DIR, exist_ok=True)

def get_etf_links():
    """Scrape the main page and extract individual ETF links."""
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all ETF links from the main page
    etf_links = []
    for a_tag in soup.select("a[href^='/etfs/']"):
        etf_links.append(urljoin(BASE_URL, a_tag["href"]))
    
    return list(set(etf_links))  # Remove duplicates

def find_prospectus_link(etf_url):
    """Find and return the prospectus PDF link from an ETF page."""
    response = requests.get(etf_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Look for links containing '/prospectus/' and ending with '.pdf'
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if "/prospectus/" in href and href.endswith(".pdf"):
            return urljoin("https://www.simplify.us", href)  # Ensure full URL
    
    return None

def download_pdf(pdf_url, etf_name):
    """Download and save the prospectus PDF if it doesn't already exist."""
    pdf_path = os.path.join(PDF_DIR, f"{etf_name}.pdf")

    # Check if the PDF is already downloaded
    if os.path.exists(pdf_path):
        print(f"Skipping: {etf_name}.pdf (already downloaded)")
        return

    response = requests.get(pdf_url, stream=True)
    if response.status_code == 200:
        with open(pdf_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {etf_name}.pdf")
    else:
        print(f"Failed to download: {etf_name}")

def main():
    etf_links = get_etf_links()
    
    for etf_url in etf_links:
        etf_name = etf_url.split("/")[-1]  # Extract ETF name from URL
        pdf_url = find_prospectus_link(etf_url)
        
        if pdf_url:
            print(f"Found prospectus for {etf_name}: {pdf_url}")
            download_pdf(pdf_url, etf_name)
        else:
            print(f"Prospectus not found for {etf_name}")

if __name__ == "__main__":
    main()

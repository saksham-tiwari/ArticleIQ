import requests
from bs4 import BeautifulSoup

def fetch_article(url: str) -> str:
    """Fetch and return clean article text from a URL."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove noise
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
            tag.decompose()

        # Prefer article/main body; fallback to whole body
        body = soup.find("article") or soup.find("main") or soup.body
        text = body.get_text(separator="\n", strip=True) if body else soup.get_text(separator="\n", strip=True)
        return text
    except Exception as e:
        raise Exception(f"Failed to fetch `{url}`: {e}")

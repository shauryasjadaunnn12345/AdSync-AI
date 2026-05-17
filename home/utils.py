import requests
from bs4 import BeautifulSoup
from django.conf import settings
import re
import uuid
import os
from supabase import create_client


SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")
SUPABASE_BUCKET = os.environ.get("SUPABASE_BUCKET", "media")

supabase = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def upload_to_supabase(file):
    try:
        if not supabase:
            return None

        file_name = f"{uuid.uuid4()}_{file.name}"

        supabase.storage.from_(SUPABASE_BUCKET).upload(
            file_name,
            file.read(),
            {"content-type": file.content_type}
        )

        public_url = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(file_name)

        return public_url

    except Exception as e:
        print("Supabase Upload Error:", e)
        return None



def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, timeout=5, headers=headers)

        if response.status_code != 200:
            return "Generic landing page content"

        soup = BeautifulSoup(response.text, "html.parser")

        headings = " ".join([
            h.get_text(strip=True)
            for h in soup.find_all(['h1', 'h2', 'h3'])
        ])

        paragraphs = " ".join([
            p.get_text(strip=True)
            for p in soup.find_all('p')[:15]
        ])

        content = f"Headings: {headings}\nContent: {paragraphs}"

        return content if content.strip() else "Generic landing page content"

    except Exception as e:
        print("Scraping Error:", e)
        return "Generic landing page content"



def clean_markdown(text):
    if not text:
        return ""

    if "```" in text:
        match = re.search(r"```html(.*?)```", text, re.DOTALL)
        if match:
            return match.group(1).strip()

        match = re.search(r"```(.*?)```", text, re.DOTALL)
        if match:
            return match.group(1).strip()

    return text.strip()



def generate_personalized_page(ad_text, landing_content, logo_url=None):
    try:
        api_url = "https://api.mistral.ai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {settings.MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }

        # Default logo fallback
        if not logo_url:
            logo_url = "https://placehold.co/150x50/png?text=Logo"

        prompt = f"""
You are an expert frontend developer.

Ad Copy:
{ad_text}

Landing Page Content:
{landing_content}

TASK:
Create a FULL modern high-converting landing page.

STRICT RULES:
- Start with <!DOCTYPE html>
- Include <meta charset="UTF-8">
- Include <meta name="viewport" content="width=device-width, initial-scale=1.0">
- Use Tailwind CDN:
  <script src="https://cdn.tailwindcss.com"></script>

SECTIONS REQUIRED:
1. Navbar (MUST include logo)
2. Hero section (strong headline + CTA)
3. Features section
4. Testimonials
5. Footer

LOGO RULE (VERY IMPORTANT):
Use EXACTLY this tag:
<img src="{logo_url}" alt="Logo" class="h-10 w-auto">

Do NOT change the logo URL.

STYLE:
- Modern SaaS design
- Clean spacing
- Gradient hero section
- Rounded buttons
- Mobile responsive

IMPORTANT:
- Do NOT return markdown
- Do NOT wrap in ``` 
- Return ONLY full HTML
- Ensure page is COMPLETE (no cut-off)
"""

        data = {
            "model": "mistral-small-latest",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 4096
        }

        response = requests.post(api_url, headers=headers, json=data, timeout=45)

        print("API STATUS:", response.status_code)

        if response.status_code != 200:
            return f"""
            <div style='color:red;padding:20px;'>
                <h2>API Error</h2>
                <pre>{response.text}</pre>
            </div>
            """

        result = response.json()

        raw_content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        if not raw_content:
            return """
            <div style='color:red;padding:20px;'>
                <h2>No content generated</h2>
            </div>
            """

        cleaned_html = clean_markdown(raw_content)

        # Safety check for valid HTML
        soup_check = BeautifulSoup(cleaned_html, "html.parser")
        body = soup_check.find("body")

        if body is None or len(body.get_text(strip=True)) < 20:
            return """
            <div style='color:orange;padding:20px;'>
                <h2>Generation Incomplete</h2>
                <p>Try generating again.</p>
            </div>
            """

        return cleaned_html

    except Exception as e:
        return f"""
        <div style='color:red;padding:20px;'>
            <h2>Server Error</h2>
            <pre>{str(e)}</pre>
        </div>
        """

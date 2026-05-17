from django.shortcuts import render
from .utils import (
    scrape_website,
    generate_personalized_page,
    upload_to_supabase
)


def home(request):
    return render(request, "index.html")


def generate(request):
    if request.method == "POST":
        try:
            
            ad_text = request.POST.get("ad_text") or ""
            ad_link = request.POST.get("ad_link")
            ad_image = request.FILES.get("ad_image")
            logo_file = request.FILES.get("logo")
            url = request.POST.get("url")

           
            if not url:
                return render(request, "result.html", {
                    "html_code": "<h2 style='color:red;'>URL is required</h2>"
                })

           
            final_ad_text = ad_text.strip()

            if ad_link:
                final_ad_text += f"\nAd Link: {ad_link}"

           
            image_url = None
            if ad_image:
                image_url = upload_to_supabase(ad_image)
                if image_url:
                    final_ad_text += f"\nAd Image URL: {image_url}"

           
            logo_url = None
            if logo_file:
                logo_url = upload_to_supabase(logo_file)

           
            landing_content = scrape_website(url)

            # Fallback if scraping fails
            if not landing_content or "Error" in landing_content:
                landing_content = "Generic modern landing page content"

            # =========================
            # 6. GENERATE HTML
            # =========================
            html_code = generate_personalized_page(
                final_ad_text,
                landing_content,
                logo_url
            )

           
            return render(request, "result.html", {
                "html_code": html_code
            })

        except Exception as e:
            return render(request, "result.html", {
                "html_code": f"""
                <div style='color:red;padding:20px;font-family:sans-serif;'>
                    <h2>Server Error</h2>
                    <pre>{str(e)}</pre>
                </div>
                """
            })

    
    return render(request, "index.html")
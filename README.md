# AI Personalized Landing Page Generator

AI-powered system that generates personalized landing pages by aligning advertisement creatives with existing landing page content using Conversion Rate Optimization (CRO) principles.

---

## 🚀 Overview

This project enhances existing landing pages instead of generating completely new ones. It analyzes advertisement messaging and modifies landing page content to create a better message match, improve clarity, and increase conversion potential.

The system accepts ad creatives (text, link, or image) along with a landing page URL and produces an AI-generated optimized HTML landing page.

---

## ❌ Problem Statement

In digital marketing funnels, there is often a disconnect between:

- Advertisement messaging
- Landing page content

This mismatch creates:

- Poor user experience
- Reduced trust
- Lower conversion rates

---

## ✅ Solution

The system generates an improved landing page by:

- Matching landing page messaging with advertisement intent
- Improving content structure and readability
- Applying CRO principles
- Preserving core website context

Instead of rebuilding pages from scratch, the AI enhances existing content using scraped website data.

---

# ✨ Features

- Input ad creative as:
  - Text
  - Link
  - Image
- Upload brand logo
- Input landing page URL
- AI-generated personalized landing page
- Live preview using iframe
- Download generated HTML
- Image storage using Supabase

---

# 🛠️ Tech Stack

## Backend
- Python
- Django

## AI
- Mistral API

## Web Scraping
- Requests
- BeautifulSoup

## Storage
- Supabase

## Frontend
- HTML
- CSS
- JavaScript

## Deployment
- Render

---

# ⚙️ System Workflow

```text
User Input
   ↓
Ad Processing & Image Upload
   ↓
Website Scraping
   ↓
AI Prompt Generation
   ↓
HTML Generation
   ↓
Preview & Download

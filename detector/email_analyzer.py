import re

URGENT_PHRASES = [
    'your account will be', 'act immediately', 'click here now',
    'verify your identity', 'unusual sign-in', 'limited time',
    'account suspended', 'action required', 'dear customer'
]

def analyze_email(text):
    findings = []
    score = 0
    lower = text.lower()

    # Bahasa urgent
    found = [p for p in URGENT_PHRASES if p in lower]
    if found:
        findings.append((f'Bahasa urgent: {len(found)} frasa', 'high'))
        score += 15 * min(len(found), 4)

    # Link mencurigakan di dalam email
    urls = re.findall(r'https?://[^\s<>"]+', text)
    if len(urls) > 5:
        findings.append((f'Banyak link: {len(urls)} URL ditemukan', 'medium'))
        score += 20

    # Generic greeting
    if re.search(r'dear (customer|user|member|account holder)', lower):
        findings.append(('Sapaan generik (bukan nama)', 'low'))
        score += 10

    # Mismatch link text vs href
    mismatches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>', text)
    for href, display in mismatches:
        if display.startswith('http') and display not in href:
            findings.append(('Link text vs URL tidak cocok', 'critical'))
            score += 35
            break

    return {'score': min(score, 100), 'findings': findings}
import re
import tldextract

SUSPICIOUS_TLDS = {'.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.click'}
BRAND_TYPOS = {
    'paypa1': 'paypal', 'g00gle': 'google',
    'amaz0n': 'amazon', 'micros0ft': 'microsoft',
    'app1e': 'apple', 'facebo0k': 'facebook'
}
URGENT_WORDS = ['verify', 'suspended', 'confirm', 'update', 'login',
                'secure', 'validate', 'billing', 'unusual', 'activity']

def analyze_url(url):
    findings = []
    score = 0
    ext = tldextract.extract(url)
    domain = ext.domain
    suffix = '.' + ext.suffix

    # IP address langsung
    if re.match(r'\d{1,3}(\.\d{1,3}){3}', url):
        findings.append(('IP address langsung', 'high'))
        score += 30

    # TLD mencurigakan
    if suffix in SUSPICIOUS_TLDS:
        findings.append((f'TLD mencurigakan: {suffix}', 'high'))
        score += 25

    # Typosquatting
    for typo, brand in BRAND_TYPOS.items():
        if typo in domain:
            findings.append((f'Imitasi brand: {typo} → {brand}', 'critical'))
            score += 40

    # URL panjang
    if len(url) > 100:
        findings.append(('URL sangat panjang', 'medium'))
        score += 15

    # Banyak subdomain
    if ext.subdomain.count('.') >= 2:
        findings.append(('Subdomain berlapis', 'medium'))
        score += 20

    # Kata kunci mencurigakan
    found = [w for w in URGENT_WORDS if w in url.lower()]
    if found:
        findings.append((f'Kata sensitif: {", ".join(found)}', 'medium'))
        score += 10 * min(len(found), 3)

    return {'score': min(score, 100), 'findings': findings}
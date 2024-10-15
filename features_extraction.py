# Purpose - This file is used to extract features from web pages.

import requests
from bs4 import BeautifulSoup
import re
import socket
import whois
import urllib
from urllib.parse import urlparse
from urllib.parse import urlsplit
from urllib.parse import urlunparse
import ipaddress
import dns.resolver
import dns.reversename
import tldextract
import joblib
from sklearn.preprocessing import StandardScaler

# Load the classifier from the .pkl file
clf = joblib.load('classifier.pkl')

def having_ip_address(url):
    # Check if the URL contains an IP address
    match = re.search(ipv4_pattern, url)
    if match:
        return -1
    else:
        return 1

def url_length(url):
    # Check the length of the URL
    if len(url) < 54:
        return 1
    if 54 <= len(url) <= 75:
        return 0
    return -1

def shortening_service(url):
    # Check if the URL is a shortened URL
    match = re.search(shortening_services, url)
    return -1 if match else 1

def having_at_symbol(url):
    # Check if the URL contains an @ symbol
    match = re.search('@', url)
    return -1 if match else 1

def double_slash_redirecting(url):
    # Check if the URL contains a double slash redirect
    last_double_slash = url.rfind('//')
    return -1 if last_double_slash > 6 else 1

def prefix_suffix(domain):
    # Check if the domain contains a prefix or suffix
    match = re.search('-', domain)
    return -1 if match else 1

def having_sub_domain(url):
    # Check if the URL contains a subdomain
    if having_ip_address(url) == -1:
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5]))|(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',
            url)
        pos = match.end()
        url = url[pos:]
    num_dots = [x.start() for x in re.finditer(r'\.', url)]
    if len(num_dots) <= 3:
        return 1
    elif len(num_dots) == 4:
        return 0
    else:
        return -1

def domain_registration_length(domain):
    # Check the length of the domain registration
    expiration_date = domain.expiration_date
    today = datetime.strptime(time.strftime('%Y-%m-%d'), '%Y-%m-%d')
    registration_length = abs((expiration_date - today).days)
    return -1 if registration_length / 365 <= 1 else 1

def favicon(wiki, soup, domain):
    # Check if the favicon is legitimate
    for head in soup.find_all('head'):
        for head.link in soup.find_all('link', href=True):
            dots = [x.start() for x in re.finditer(r'\.', head.link['href'])]
            if wiki in head.link['href'] or domain in head.link['href'] or len(dots) == 1:
                return 1
    return -1

def https_token(url):
    # Check if the URL contains an HTTPS token
    match = re.search(http_https, url)
    if match and match.start() == 0:
        url = url[match.end():]
    match = re.search('http|https', url)
    return -1 if match else 1

def request_url(wiki, soup, domain):
    # Check if the URL is legitimate
    i = 0
    success = 0
    for img in soup.find_all('img', src=True):
        dots = [x.start() for x in re.finditer(r'\.', img['src'])]
        if wiki in img['src'] or domain in img['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for audio in soup.find_all('audio', src=True):
        dots = [x.start() for x in re.finditer(r'\.', audio['src'])]
        if wiki in audio['src'] or domain in audio['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for embed in soup.find_all

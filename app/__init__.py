from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
from http.server import BaseHTTPRequestHandler, HTTPServer
import pandas as pd
import numpy as np
import json
from .model import LSAModel
import urllib.parse as parse
from .singleton import quicksingleton


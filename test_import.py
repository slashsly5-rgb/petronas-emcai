"""Quick test to verify imports work"""
import sys
print(f"Python version: {sys.version}")

try:
    import streamlit as st
    print("[OK] Streamlit imported successfully")
except ImportError as e:
    print(f"[FAIL] Streamlit import failed: {e}")

try:
    import pandas as pd
    print("[OK] Pandas imported successfully")
except ImportError as e:
    print(f"[FAIL] Pandas import failed: {e}")

try:
    import plotly
    print("[OK] Plotly imported successfully")
except ImportError as e:
    print(f"[FAIL] Plotly import failed: {e}")

try:
    import requests
    print("[OK] Requests imported successfully")
except ImportError as e:
    print(f"[FAIL] Requests import failed: {e}")

print("\nChecking app structure...")
try:
    from utils.api_client import client
    print("[OK] API client loaded")
    from utils import charts
    print("[OK] Charts module loaded")
    from utils import alerts
    print("[OK] Alerts module loaded")
    print("\n[SUCCESS] All imports successful! App should run correctly.")
except Exception as e:
    print(f"[FAIL] Error: {e}")

import json
import os
from dotenv import load_dotenv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

# ==========================================================
# 🌟 STEP 1: Setup & Authentication
# ==========================================================
# We use 'load_dotenv' to read our secret API key from the .env file.
# 'override=True' ensures that if we change the .env file, the script picks it up.
load_dotenv(override=True)

# Retrieve the key and URL from the environment variables
IAM_KEY = os.getenv('IAM_KEY')
SERVICE_URL = os.getenv('SERVICE_URL')

# Basic check to make sure the user has set up their .env file
if not IAM_KEY or not SERVICE_URL:
    print("❌ ERROR: Missing credentials in .env file.")
    exit()

# The Authenticator is like a 'ID card' that tells IBM who you are.
authenticator = IAMAuthenticator(IAM_KEY)

# Create the NLU service instance. 
# The 'version' date tells the SDK which API rules to use.
nlu = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

# Connect to the specific URL for your Watson service instance
nlu.set_service_url(SERVICE_URL)

print("🚀 Watson NLU is ready to analyze!")

# ==========================================================
# 🧠 STEP 2: Analyzing Website Metadata
# ==========================================================
# Metadata extraction gives us the 'Title', 'Language', and 'Image' of a page.
print("\n--- Analyzing Metadata ---")
try:
    # We call 'analyze' and specify we want 'metadata'.
    # In the SDK, metadata doesn't need extra settings, so we pass an empty dict {}.
    metadata_response = nlu.analyze(
        url='www.ibm.com',
        features=Features(metadata={})
    ).get_result()

    # We use json.dumps to make the output easy to read (indented with 2 spaces)
    print(json.dumps(metadata_response, indent=2))
except Exception as e:
    print(f"❌ Metadata analysis failed: {e}")

# ==========================================================
# 🏷️ STEP 3: Analyzing Categories
# ==========================================================
# Categories tell us 'what' the page is about (e.g., /Technology/Computing).
print("\n--- Analyzing Categories ---")
try:
    # Here, we set a 'limit' of 3 to only get the top 3 categories.
    categories_response = nlu.analyze(
        url='www.ibm.com',
        features=Features(categories=CategoriesOptions(limit=3))
    ).get_result()

    print(json.dumps(categories_response, indent=2))
except Exception as e:
    print(f"❌ Categories analysis failed: {e}")

# ==========================================================
# 🎓 PRO TIP FOR STUDENTS: 
# ==========================================================
# You can combine features in one call!
# Example: features=Features(categories=CategoriesOptions(limit=1), metadata={})
# This saves time and API calls.

from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
import certifi

# URL encode your credentials to handle any special characters
username = quote_plus("mt15")
password = quote_plus("mt15")

uri = f"mongodb+srv://{username}:{password}@cluster0.9s8y1nz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create client with SSL certificate
client = MongoClient(uri, tlsCAFile=certifi.where())

# Test connection
try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("\n🔧 If this still fails, check:")
    print("1. Is your IP address whitelisted in MongoDB Atlas?")
    print("2. Go to Network Access in MongoDB Atlas and add your current IP")
import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22687815"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bfa7aabd82e89fb9b72442763dad60df")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rishabhsoni5002:rishabhsoni5002@cluster0.4bi4a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

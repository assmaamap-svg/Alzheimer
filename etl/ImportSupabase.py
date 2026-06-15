import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

local_folder = r"Databrutes"
remote_folder = "raw"

for filename in os.listdir(local_folder):
    file_path = os.path.join(local_folder, filename)

    if os.path.isfile(file_path) and filename.lower().endswith(".csv"):
        print(f"Upload du fichier CSV : {filename}")

        with open(file_path, "rb") as f:
            supabase.storage.from_("DataLakeAlzheimer").update(
                f"{remote_folder}/{filename}",
                f
            )

print("Upload terminé.")

import os

from dotenv import dotenv_values
from supabase import create_client


def main():
    config = dotenv_values(".env")

    supabase = create_client(config["SUPABASE_URL"], config["SUPABASE_KEY"])

    response = (
        supabase.table("users")
        .insert({"first_name": "Abraham", "last_name": "Lincoln"})
        .execute()
    )

    print(response)

if __name__ == "__main__":
    main()

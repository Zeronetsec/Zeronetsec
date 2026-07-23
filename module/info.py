# https://github.com/Zeronetsec/Zeronetsec

import requests
import sys
from datetime import datetime
from utils.color import Color

class Info:
    @staticmethod
    def execute(*args):
        url = "https://api.github.com/users/Zeronetsec"
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "https://github.com/Zeronetsec/Zeronetsec",
        }

        try:
            response = requests.get(
                url, headers=headers, timeout=10,
            )

            response.raise_for_status()
            data = response.json()

            def format_date(iso_string):
                if not iso_string:
                    return "-"
                dt = datetime.strptime(
                    iso_string, "%Y-%m-%dT%H:%M:%SZ",
                )
                return dt.strftime("%d %B %Y, %H:%M UTC")

            result = {
                "GitHub": data.get("html_url") or "-",
                "Login": data.get("login") or "-",
                "Name": data.get("name") or "-",
                "Avatar": data.get("avatar_url") or "-",
                "Bio": data.get("bio") or "-",
                "Company": data.get("company") or "-",
                "Location": data.get("location") or "-",
                "Twitter": data.get("twitter_username") or "-",
                "Email": data.get("email") or "-",
                "Blog": data.get("blog") or "-",
                "Repos": data.get("public_repos", 0),
                "Gists": data.get("public_gists", 0),
                "Followers": data.get("followers", 0),
                "Following": data.get("following", 0),
                "ID": data.get("id") or "-",
                "Node id": data.get("node_id") or "-",
                "Gravatar id": data.get("gravatar_id") or "-",
                "Type": data.get("type") or "-",
                "User view type": data.get("user_view_type") or "-",
                "Site admin": data.get("site_admin") or "-",
                "Hireable": data.get("hireable")
                if data.get("hireable") is not None
                else "-",
                "Created": format_date(
                    data.get("created_at"),
                ),
                "Updated": format_date(
                    data.get("updated_at"),
                ),
            }

            for key, value in result.items():
                print(
                    f"{Color.N}{key}: {Color.GG}{value}{Color.N}",
                )

        except requests.exceptions.RequestException as e:
            print(
                f"{Color.R}[!] {Color.N}Error fetching GitHub data: {Color.GG}{e}{Color.N}",
                file=sys.stderr,
            )
            sys.exit(1)

# Copyright (c) 2026 Zeronetsec
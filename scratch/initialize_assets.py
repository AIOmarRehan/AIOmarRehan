import os
import urllib.request
import urllib.error

# Target assets directory
assets_dir = r"c:\Users\Omar Rehan\Desktop\README\assets"
os.makedirs(assets_dir, exist_ok=True)

urls = {
    "github-trophies.svg": "https://github-profile-trophy.vercel.app/?username=AIOmarRehan&theme=onestar&no-frame=true&no-bg=true&column=7&margin-w=8&margin-h=8&rank=SECRET,SSS,SS,S,AAA,AA,A,B",
    "github-streak-stats.svg": "https://streak-stats.demolab.com/?user=AIOmarRehan&background=0d1117&border=4c1d95&stroke=a78bfa&ring=7c3aed&fire=a78bfa&currStreakLabel=a78bfa&sideLabels=a78bfa&currStreakNum=f5f3ff&sideNums=f5f3ff&dates=8b949e&date_format=j%20M%5B%20Y%5D",
    "github-activity-graph.svg": "https://github-readme-activity-graph.vercel.app/graph?username=AIOmarRehan&bg_color=0d1117&color=a78bfa&line=7c3aed&point=f5f3ff&area=true&area_color=4c1d95&hide_border=true&custom_title=Contribution%20Activity",
    "github-stars.svg": "https://img.shields.io/github/stars/AIOmarRehan?style=for-the-badge&color=a78bfa&labelColor=0d1117&logo=github&logoColor=a78bfa&affiliations=OWNER",
    "github-followers.svg": "https://img.shields.io/github/followers/AIOmarRehan?style=for-the-badge&color=a78bfa&labelColor=0d1117&logo=github&logoColor=a78bfa"
}

# Simple placeholder for the snake-dark SVG
snake_placeholder = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 828 175" width="828" height="175">
  <rect width="100%" height="100%" fill="#0d1117" rx="8"/>
  <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="16" fill="#a78bfa" font-weight="bold">
    🐍 Contribution Snake Animation (Generated on GitHub Actions)
  </text>
</svg>"""

for name, url in urls.items():
    print(f"Downloading {name}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read()
            # Basic validation
            content_str = content.decode('utf-8', errors='ignore').lower()
            if "unable to select next github token" in content_str or "rate limit exceeded" in content_str or "something went wrong" in content_str or "<svg" not in content_str:
                print(f"  Warning: downloaded content for {name} appears invalid or has rate limit errors. Writing placeholder.")
                placeholder = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 150" width="500" height="150">
                  <rect width="100%" height="100%" fill="#0d1117" rx="8"/>
                  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#a78bfa">
                    {name.replace('.svg', '').replace('-', ' ').title()} (Will update via GitHub Actions)
                  </text>
                </svg>"""
                with open(os.path.join(assets_dir, name), "w", encoding="utf-8") as f:
                    f.write(placeholder)
            else:
                with open(os.path.join(assets_dir, name), "wb") as f:
                    f.write(content)
                print(f"  Successfully saved {name}.")
    except Exception as e:
        print(f"  Error downloading {name}: {e}. Writing placeholder.")
        placeholder = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 150" width="500" height="150">
          <rect width="100%" height="100%" fill="#0d1117" rx="8"/>
          <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#a78bfa">
            {name.replace('.svg', '').replace('-', ' ').title()} (Will update via GitHub Actions)
          </text>
        </svg>"""
        with open(os.path.join(assets_dir, name), "w", encoding="utf-8") as f:
            f.write(placeholder)

# Write snake placeholder
with open(os.path.join(assets_dir, "github-snake-dark.svg"), "w", encoding="utf-8") as f:
    f.write(snake_placeholder)
print("Saved github-snake-dark.svg placeholder.")

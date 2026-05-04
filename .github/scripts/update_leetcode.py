import requests
import os
import sys
from datetime import datetime

def fetch_leetcode_stats(username):
    url = "https://leetcode.com/graphql"
    query = """
    query getUserContestRanking($username: String!) {
        userContestRanking(username: $username) {
            attendedContestsCount
            rating
            globalRanking
            totalParticipants
            topPercentage
            badge { name }
        }
        userContestRankingHistory(username: $username) {
            attended
            rating
            ranking
            contest { title startTime }
        }
    }
    """
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com"
    }
    resp = requests.post(url, json={"query": query, "variables": {"username": username}}, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json().get("data", {})


def generate_svg(history, summary, username):
    attended = [h for h in history if h.get("attended")]
    if not attended:
        print("❌ no contest")
        sys.exit(1)

    ratings = [round(h["rating"]) for h in attended]
    labels = [h["contest"]["title"].replace("Weekly Contest ", "WC").replace("Biweekly Contest ", "BC") for h in attended]

    W, H = 860, 360
    PAD_L, PAD_R, PAD_T, PAD_B = 72, 28, 40, 56
    chart_w = W - PAD_L - PAD_R
    chart_h = H - PAD_T - PAD_B

    r_min = min(ratings)
    r_max = max(ratings)
    r_range = r_max - r_min or 1
    padding = r_range * 0.12
    y_low  = r_min - padding
    y_high = r_max + padding

    def cx(i): return PAD_L + i / max(len(ratings) - 1, 1) * chart_w
    def cy(v): return PAD_T + (1 - (v - y_low) / (y_high - y_low)) * chart_h

    # Y grid lines & labels
    grid_lines = ""
    n_ticks = 5
    for i in range(n_ticks + 1):
        val = y_low + i / n_ticks * (y_high - y_low)
        y = cy(val)
        grid_lines += f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W - PAD_R}" y2="{y:.1f}" stroke="#e5e7eb" stroke-width="1"/>\n'
        grid_lines += f'<text x="{PAD_L - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11" fill="#9ca3af">{round(val)}</text>\n'

    # X labels (show every N-th to avoid overlap)
    n = len(ratings)
    step = max(1, n // 10)
    x_labels = ""
    for i in range(0, n, step):
        x = cx(i)
        x_labels += f'<text x="{x:.1f}" y="{H - 10}" text-anchor="middle" font-size="10" fill="#9ca3af" transform="rotate(-30,{x:.1f},{H-10})">{labels[i]}</text>\n'

    # Polyline + area fill
    pts = " ".join(f"{cx(i):.1f},{cy(r):.1f}" for i, r in enumerate(ratings))
    area_pts = f"{cx(0):.1f},{PAD_T + chart_h} " + pts + f" {cx(n-1):.1f},{PAD_T + chart_h}"

    # Dots (only last and max/min)
    dots = ""
    special = {ratings.index(max(ratings)): ("#10b981", str(max(ratings))),
               ratings.index(min(ratings)): ("#f59e0b", str(min(ratings))),
               n - 1: ("#6366f1", str(ratings[-1]))}
    for idx, (color, label) in special.items():
        x, y = cx(idx), cy(ratings[idx])
        dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{color}" stroke="white" stroke-width="2"/>\n'
        anchor = "middle" if idx not in (0, n-1) else ("start" if idx == 0 else "end")
        dots += f'<text x="{x:.1f}" y="{y - 10:.1f}" text-anchor="{anchor}" font-size="11" font-weight="600" fill="{color}">{label}</text>\n'

    # Summary stats bar
    cur_rating = round(summary.get("rating", ratings[-1]))
    global_rank = summary.get("globalRanking", "N/A")
    top_pct = summary.get("topPercentage", 0)
    contest_cnt = summary.get("attendedContestsCount", n)
    badge = summary.get("badge", {})
    badge_name = badge.get("name", "") if badge else ""

    stats_y = PAD_T - 18
    stats = f"""
    <text x="{PAD_L}" y="{stats_y}" font-size="12" fill="#6b7280">Rating: <tspan font-weight="600" fill="#6366f1">{cur_rating}</tspan></text>
    <text x="{PAD_L + 130}" y="{stats_y}" font-size="12" fill="#6b7280">Rank: <tspan font-weight="600" fill="#374151">#{global_rank}</tspan></text>
    <text x="{PAD_L + 260}" y="{stats_y}" font-size="12" fill="#6b7280">Top <tspan font-weight="600" fill="#374151">{top_pct:.1f}%</tspan></text>
    <text x="{PAD_L + 370}" y="{stats_y}" font-size="12" fill="#6b7280">Contests: <tspan font-weight="600" fill="#374151">{contest_cnt}</tspan></text>
    {"" if not badge_name else f'<text x="{PAD_L + 490}" y="{stats_y}" font-size="12" fill="#6b7280">Badge: <tspan font-weight="600" fill="#f59e0b">{badge_name}</tspan></text>'}
    """

    updated = datetime.utcnow().strftime("%Y-%m-%d")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <rect width="{W}" height="{H}" fill="#ffffff" rx="12"/>
  <defs>
    <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0.01"/>
    </linearGradient>
  </defs>
  {grid_lines}
  <polygon points="{area_pts}" fill="url(#areaGrad)"/>
  <polyline points="{pts}" fill="none" stroke="#6366f1" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
  {dots}
  {x_labels}
  {stats}
  <text x="{W - PAD_R}" y="{H - 4}" text-anchor="end" font-size="10" fill="#d1d5db">Updated {updated} · leetcode.com/{username}</text>
</svg>"""
    return svg


if __name__ == "__main__":
    username = os.environ.get("LEETCODE_USERNAME")
    if not username:
        print("❌ set LEETCODE_USERNAME env")
        sys.exit(1)

    print(f"🔍 getting {username} data...")
    data = fetch_leetcode_stats(username)
    history = data.get("userContestRankingHistory", [])
    summary = data.get("userContestRanking") or {}

    svg = generate_svg(history, summary, username)

    os.makedirs("assets", exist_ok=True)
    with open("assets/leetcode_rating.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("✅ SVG done:assets/leetcode_rating.svg")
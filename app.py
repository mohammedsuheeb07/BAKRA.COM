from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

ANIMALS = [
    {"name": "Raja Sher Singh", "animal": "Lion", "emoji": "🦁",
     "bio": "King of the jungle. Still asks his mother before going out.",
     "hobby": "Sleeping 20 hours a day", "status": "Emotionally roaring"},
    {"name": "Gabbar Bakra", "animal": "Goat", "emoji": "🐐",
     "bio": "Attitude unlimited. Grass budget unlimited. Romance experience: zero.",
     "hobby": "Eating everyone's plants", "status": "Single and chewing"},
    {"name": "Miss Baa Baa", "animal": "Sheep", "emoji": "🐑",
     "bio": "Looking for someone who appreciates a fluffy personality.",
     "hobby": "Standing in a group", "status": "Waiting for a sign"},
    {"name": "Moo-dy Kumar", "animal": "Cow", "emoji": "🐄",
     "bio": "Very down to earth. Literally eats grass from the ground.",
     "hobby": "Chewing while thinking", "status": "It's complicated"},
    {"name": "Sir Clucks-a-Lot", "animal": "Chicken", "emoji": "🐔",
     "bio": "Wakes up at 5 AM and judges everyone who doesn't.",
     "hobby": "Running without a destination", "status": "Searching for purpose"},
    {"name": "Bunny CEO", "animal": "Rabbit", "emoji": "🐰",
     "bio": "Entrepreneur. Owns three carrots and a dream.",
     "hobby": "Practising dramatic jumps", "status": "Too busy to reply"},
    {"name": "Dumbo Developer", "animal": "Elephant", "emoji": "🐘",
     "bio": "Has a great memory but forgot why this profile exists.",
     "hobby": "Remembering embarrassing moments", "status": "Thinking about it"},
    {"name": "Pintu Panda", "animal": "Panda", "emoji": "🐼",
     "bio": "Professional napper seeking a partner in doing absolutely nothing.",
     "hobby": "Sleeping after sleeping", "status": "Offline"},
    {"name": "Turbo Tortoise", "animal": "Tortoise", "emoji": "🐢",
     "bio": "Replies to messages in approximately three business weeks.",
     "hobby": "Taking the scenic route", "status": "Loading..."},
    {"name": "Ducky Don", "animal": "Duck", "emoji": "🦆",
     "bio": "Walks like a boss. Quacks like a broken speaker.",
     "hobby": "Arguing with reflections", "status": "Quackfully single"},
    {"name": "Mithu Influencer", "animal": "Parrot", "emoji": "🦜",
     "bio": "Repeats everything you say. Perfect listener, questionable secret keeper.",
     "hobby": "Copying other people's personalities", "status": "Seen at 2:03 AM"},
    {"name": "Mr. Meowster", "animal": "Cat", "emoji": "🐱",
     "bio": "Will ignore you even after you pay for premium.",
     "hobby": "Knocking objects off tables", "status": "You are not my type"},
]

EXCUSES = [
    "You both enjoy eating. Groundbreaking compatibility.",
    "One of you has legs. The other probably does too.",
    "Our AI detected absolutely nothing suspicious. Match approved!",
    "Both profiles have successfully passed the grass inspection.",
    "You share a mutual interest in existing.",
    "Our computer sneezed. Congratulations, you're a match.",
    "The algorithm flipped a coin. The coin has spoken.",
]

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BAKRA.COM | Seriously Unnecessary Matchmaking</title>
<style>
:root{--green:#176b43;--lime:#d7f5a6;--cream:#fffdf4;--ink:#202a23}
*{box-sizing:border-box}
body{margin:0;background:var(--cream);color:var(--ink);
font-family:system-ui,-apple-system,Arial,sans-serif}
header{background:var(--green);color:white;padding:24px 6%;
display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.logo{font-size:30px;font-weight:1000;letter-spacing:-1px}
.logo span{color:var(--lime)}
header small{opacity:.85}
main{max-width:1100px;margin:auto;padding:28px 18px}
.hero{background:#e8f4d9;border:2px dashed var(--green);border-radius:24px;
padding:32px 20px;text-align:center}
h1{font-size:clamp(32px,6vw,56px);line-height:1.05;margin:12px 0}
.hero p{max-width:650px;margin:12px auto;line-height:1.6}
.tag{display:inline-block;background:var(--lime);padding:7px 12px;border-radius:20px;
font-size:12px;font-weight:900}
button,.button{border:0;border-radius:12px;background:var(--green);color:white;
padding:12px 17px;font-size:15px;font-weight:800;cursor:pointer;text-decoration:none;
display:inline-block;margin:4px}
button:hover,.button:hover{transform:translateY(-2px);filter:brightness(1.1)}
.secondary{background:#f0d58a;color:#302714}
input,select{padding:12px;border:1px solid #a5b9a6;border-radius:10px;
font-size:15px;max-width:100%}
.section-title{display:flex;justify-content:space-between;align-items:end;gap:10px;
flex-wrap:wrap;margin:35px 0 15px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(225px,1fr));gap:16px}
.card{background:white;border:1px solid #dbe4d7;border-radius:18px;padding:18px;
box-shadow:0 5px 16px #163d1910}
.avatar{font-size:58px;background:#f1f6e9;border-radius:14px;text-align:center;padding:15px}
.card h3{margin:12px 0 3px}
.muted{color:#647066;font-size:13px}
.bio{min-height:45px;line-height:1.45}
.pill{display:inline-block;border-radius:20px;background:#e8f4d9;padding:5px 9px;
font-size:12px;font-weight:800}
.panel{margin-top:24px;padding:22px;border-radius:18px;background:#fff;
border:1px solid #dbe4d7}
.result{background:#fff3c7;border:2px dashed #b58b23;padding:20px;
border-radius:16px;margin-top:20px;text-align:center}
.result .big{font-size:48px}
.score{font-size:40px;font-weight:1000;color:var(--green)}
footer{text-align:center;padding:30px 15px;background:#173d2a;color:white;margin-top:35px}
footer p{margin:7px}
small{line-height:1.5}
@media(max-width:500px){header{padding:18px}main{padding:18px 12px}.hero{padding:24px 13px}}
</style>
</head>
<body>
<header>
  <div>
    <div class="logo">🐐 BAKRA<span>.COM</span></div>
    <small>The world's most unnecessary matchmaking platform</small>
  </div>
  <div class="pill">100% Unnecessary™</div>
</header>
<main>
<section class="hero">
  <span class="tag">INNOVATION NOBODY REQUESTED</span>
  <h1>Find your baa-<br>forever person.</h1>
  <p>Animal owners can already find animal partners the normal way.
  We built a website anyway. Because apparently, the internet needed more goats.</p>
  <p><strong>Our mission:</strong> Make a simple thing unnecessarily complicated.</p>
  <a class="button" href="#profiles">Browse the bachelors</a>
  <a class="button secondary" href="#match">Launch useless AI</a>
</section>

{% if result %}
<section class="result" aria-live="polite">
  <div class="big">{{ result.emoji }}</div>
  <span class="tag">OFFICIAL TOTALLY UNOFFICIAL MATCH REPORT</span>
  <h2>{{ result.name }} is your soulmate!</h2>
  <p>{{ excuse }}</p>
  <div class="score">100% MATCH</div>
  <p>Our AI analysed 47 blades of grass, consulted absolutely nobody,
  and arrived at this scientifically questionable conclusion.</p>
  <p><strong>Compatibility details:</strong> We made them up with confidence.</p>
  <small>Result ID: NOT-A-REAL-SCIENTIFIC-STUDY</small>
</section>
{% endif %}

{% if premium %}
<section class="result" aria-live="polite">
  <div class="big">👑🐐</div>
  <h2>Congratulations, Premium Goat!</h2>
  <p>Your golden badge has been activated.</p>
  <p><strong>What changed?</strong> Your badge is gold now.</p>
  <p>More matches? No. Better compatibility? No. Extra grass? Also no.</p>
  <p><strong>Value delivered:</strong> Visually expensive. Functionally identical.</p>
</section>
{% endif %}

<div class="section-title" id="match">
  <div><h2>🤖 Advanced Random Matchmaking</h2>
  <div class="muted">Our algorithm is 100% confident and 0% qualified.</div></div>
</div>
<section class="panel">
  <form method="POST" action="/match">
    <label for="animal"><strong>Choose your animal:</strong></label><br><br>
    <select id="animal" name="animal">
      {% for a in animals %}
      <option value="{{ a.name }}">{{ a.emoji }} {{ a.name }} ({{ a.animal }})</option>
      {% endfor %}
    </select>
    <button type="submit">Find My Soulmate 💘</button>
  </form>
  <p class="muted">The result is random. The confidence is fake. The button works.</p>
</section>

<div class="section-title" id="profiles">
  <div><h2>🐾 Elite Animal Profiles</h2>
  <div class="muted">{{ animals|length }} profiles. Approximately zero necessary.</div></div>
  <form method="GET" action="/">
    <input name="q" placeholder="Search animals..." value="{{ query }}">
    <button type="submit">Search</button>
  </form>
</div>
<div class="grid">
{% for a in visible_animals %}
<article class="card">
  <div class="avatar">{{ a.emoji }}</div>
  <h3>{{ a.name }}</h3>
  <div class="muted">{{ a.animal }} • {{ a.status }}</div>
  <p class="bio">{{ a.bio }}</p>
  <p><span class="pill">Hobby: {{ a.hobby }}</span></p>
  <form method="POST" action="/match">
    <input type="hidden" name="animal" value="{{ a.name }}">
    <button type="submit">Match this animal</button>
  </form>
</article>
{% else %}
<div class="panel">No animals found. Even our search engine has given up.</div>
{% endfor %}
</div>

<section class="panel">
  <h2>👑 BAKRA PLUS ULTRA</h2>
  <p>Upgrade your animal to Premium and receive a beautiful golden badge that
  does absolutely nothing useful.</p>
  <form method="POST" action="/premium">
    <button class="secondary" type="submit">Activate Fake Premium</button>
  </form>
  <small>No payment is collected. No actual premium service exists.
  The only thing being upgraded is the joke.</small>
</section>

<section class="panel">
  <h2>📊 Our totally serious statistics</h2>
  <div class="grid">
    <div><div class="score">100%</div><strong>Compatibility</strong><br>
      <small>Even for animals that have never met.</small></div>
    <div><div class="score">0</div><strong>Problems solved</strong><br>
      <small>As planned by our research department.</small></div>
    <div><div class="score">∞</div><strong>Unnecessary features</strong><br>
      <small>Limited only by our imagination.</small></div>
  </div>
</section>
</main>
<footer>
  <div class="logo">🐐 BAKRA<span>.COM</span></div>
  <p>One goat. One profile. One completely unnecessary revolution.</p>
  <p><strong>Built by Mohammed Rishan Suheeb</strong></p>
  <small>For entertainment and educational demonstration only. Not a real animal
  matchmaking service. No real AI compatibility analysis is performed.</small>
</footer>
</body>
</html>
"""


@app.route("/")
def home():
    query = request.args.get("q", "").strip().lower()
    visible = [
        a for a in ANIMALS
        if query in (a["name"] + " " + a["animal"] + " " + a["bio"]).lower()
    ]
    return render_template_string(
        HTML,
        animals=ANIMALS,
        visible_animals=visible,
        query=request.args.get("q", ""),
        result=None,
        excuse="",
        premium=False,
    )


@app.route("/match", methods=["POST"])
def match():
    selected_name = request.form.get("animal", "")
    selected = next(
        (a for a in ANIMALS if a["name"] == selected_name),
        random.choice(ANIMALS),
    )
    # The match is deliberately random: this is a comedy demo, not real AI.
    candidates = [a for a in ANIMALS if a["name"] != selected["name"]]
    result = random.choice(candidates)

    # Every match receives a completely meaningless 100% score.
    return render_template_string(
        HTML,
        animals=ANIMALS,
        visible_animals=ANIMALS,
        query="",
        result=result,
        excuse=random.choice(EXCUSES),
        premium=False,
    )


@app.route("/premium", methods=["POST"])
def premium():
    return render_template_string(
        HTML,
        animals=ANIMALS,
        visible_animals=ANIMALS,
        query="",
        result=None,
        excuse="",
        premium=True,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

from html import escape
from pathlib import Path


BASE = Path(__file__).resolve().parent
TEXT_PATH = BASE / "text-draft.txt"

FIGURES = [
    {
        "after": "HEADER",
        "src": "assets/scene-01-breakfast-chocolate.png",
        "caption": "Палавко решава, че шоколадът е по-важен от закуската.",
    },
    {
        "after": "И изчезна бързо.",
        "src": "assets/scene-02-sugar-crash.png",
        "caption": "След шоколада силата на Палавко изведнъж започва да се изпарява.",
    },
    {
        "after": "А в същото време, дълбоко в организма му, ставаше нещо много важно.",
        "src": "assets/scene-03-body-battle.png",
        "caption": "В организма му Шумниците объркват строежа на Мускулчовците.",
    },

    {
        "after": "Той изяде едно малко парченце ябълка.",
        "src": "assets/scene-04-first-good-food.png",
        "caption": "Първите полезни хапки стигат до малките строители на сила.",
    },
    {
        "after": "И тогава Палавко го видя.",
        "src": "assets/scene-05-boyan-playground.png",
        "caption": "Боян минава през катерушките със сила, лекота и усмивка.",
    },
    {
        "after": "- Здрасти - каза то. - Аз съм Боян.",
        "src": "assets/scene-06-boyan-secret.png",
        "caption": "Боян разкрива тайната си: полезната храна се връща като сила.",
    },
    {
        "after": "Палавко тръгна към катерушката. Хвана първото въже. Стъпи на ниската греда. Ръцете му потрепериха малко.",
        "src": "assets/scene-07-palavko-climbs.png",
        "caption": "Палавко опитва първите стъпки по въжената стена.",
    },
    {
        "after": "Вечерта, когато се прибраха, мама сложи на масата супа, пилешко месо, салата и малка купичка с кисело мляко.",
        "src": "assets/scene-08-dinner-balance.png",
        "caption": "Вечерята вече не е препятствие, а помощ за утрешната игра.",
    },
    {
        "after": "А дълбоко в организма на Палавко Мускулчовците най-после седнаха да си починат до новата здрава стена.",
        "src": "assets/scene-09-calm-body-ending.png",
        "caption": "В организма на Палавко най-после е спокойно.",
    },
]


def split_blocks(text: str) -> tuple[str, str, list[str], str]:
    parts = [block.strip() for block in text.replace("\r\n", "\n").split("\n\n") if block.strip()]
    title = parts[0]
    intro = parts[1]
    moral_index = parts.index("ПОУКА")
    story = parts[2:moral_index]
    moral = "\n\n".join(parts[moral_index + 1 :])
    return title, intro, story, moral


def figure_html(src: str, caption: str) -> str:
    return (
        '<figure class="story-image">'
        f'<img src="{escape(src)}" alt="{escape(caption)}">'
        f"<figcaption>{escape(caption)}</figcaption>"
        "</figure>"
    )


def gallery_html(items: list[tuple[str, str]]) -> str:
    cards = []
    for src, caption in items:
        cards.append(
            '<figure class="character-card">'
            f'<img src="{escape(src)}" alt="{escape(caption)}">'
            f"<figcaption>{escape(caption)}</figcaption>"
            "</figure>"
        )
    return '<section class="characters" aria-label="Герои">' + "".join(cards) + "</section>"


def paragraph_html(text: str, class_name: str = "para") -> str:
    return f'<p class="{class_name}">{escape(text)}</p>'


def build_html() -> str:
    title, intro, story, moral = split_blocks(TEXT_PATH.read_text(encoding="utf-8"))
    figures_by_after = {item["after"]: item for item in FIGURES}

    body = [
        '<!doctype html>',
        '<html lang="bg">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{escape(title)}</title>",
        "<style>",
        ":root { --paper:#fff8ec; --ink:#2a211b; --muted:#705f51; --accent:#c84434; --accent2:#2f8768; --line:#ead8c3; }",
        "* { box-sizing: border-box; }",
        "body { margin:0; background:#f1e6d8; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; line-height:1.65; }",
        ".book { max-width: 980px; margin:0 auto; background:var(--paper); min-height:100vh; padding:38px 22px 64px; box-shadow:0 20px 70px rgba(42,33,27,.13); }",
        ".cover { text-align:center; padding:18px 0 8px; }",
        ".series { margin:0 0 8px; color:var(--accent); font:700 15px/1.2 Arial, sans-serif; letter-spacing:.08em; text-transform:uppercase; }",
        "h1 { margin:0; font-size:clamp(34px, 5vw, 58px); line-height:1.08; letter-spacing:0; }",
        ".para, .intro, .moral-text { max-width:740px; margin:0 auto 16px; font-size:21px; }",
        ".intro { margin-top:22px; padding:18px 20px; border-left:5px solid var(--accent); background:#fff1dd; border-radius:6px; font-weight:700; }",
        ".story-image { margin:34px auto 38px; max-width:780px; }",
        ".story-image:first-of-type { margin-top:24px; }",
        ".story-image img, .character-card img { display:block; width:100%; height:auto; border-radius:8px; box-shadow:0 16px 42px rgba(42,33,27,.18); background:#ddd; }",
        "figcaption { margin-top:10px; color:var(--muted); font:15px/1.45 Arial, sans-serif; text-align:center; }",
        ".characters { max-width:900px; margin:34px auto 38px; display:grid; grid-template-columns:repeat(3, 1fr); gap:18px; }",
        ".character-card { margin:0; }",
        ".character-card img { aspect-ratio:1 / 1; object-fit:cover; }",
        ".character-card figcaption { color:var(--accent2); font-weight:700; }",
        ".moral { max-width:780px; margin:42px auto 0; padding:24px 24px 20px; border:2px solid var(--line); border-radius:8px; background:#fff3df; }",
        ".moral h2 { margin:0 0 10px; color:var(--accent); font:800 20px/1.2 Arial, sans-serif; letter-spacing:.08em; }",
        ".moral .moral-text { margin:0; font-weight:700; }",
        "@media (max-width: 720px) { .book { padding:24px 16px 44px; } .para, .intro, .moral-text { font-size:18px; } .story-image { margin:26px auto 30px; } .characters { grid-template-columns:1fr; max-width:430px; } }",
        "</style>",
        "</head>",
        "<body>",
        '<main class="book">',
        '<header class="cover">',
        '<p class="series">Приказки за Палавко</p>',
        f"<h1>{escape(title)}</h1>",
        "</header>",
        figure_html(figures_by_after["HEADER"]["src"], figures_by_after["HEADER"]["caption"]),
        paragraph_html(intro, "intro"),
    ]

    for paragraph in story:
        body.append(paragraph_html(paragraph))
        item = figures_by_after.get(paragraph)
        if item:
            if "gallery" in item:
                body.append(gallery_html(item["gallery"]))
            else:
                body.append(figure_html(item["src"], item["caption"]))

    body.extend(
        [
            '<section class="moral"><h2>ПОУКА</h2>',
            paragraph_html(moral, "moral-text"),
            "</section>",
            "</main>",
            "</body>",
            "</html>",
        ]
    )
    return "\n".join(body)


if __name__ == "__main__":
    html = build_html()
    for name in ("index-illustrated.html", "index.html"):
        (BASE / name).write_text(html, encoding="utf-8", newline="\n")

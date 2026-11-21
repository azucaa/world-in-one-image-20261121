#!/usr/bin/env python3
"""Compose the front page for Saturday, November 21, 2026.

Design tool only (uses Pillow). It renders assets/entry.png, a 1024x1024
newspaper front page: masthead with the date, one lead story, a six-story
grid, one full-width story and a closing footer strip. Every word is real
drawn text; there are no photographs and no generated imagery.

The competition entrypoint is main.py, which copies this file's output
byte for byte and needs nothing beyond the standard library.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MARGIN = 36
PAPER = (247, 243, 234)
INK = (20, 20, 20)
GREY = (92, 88, 80)
RED = (168, 32, 22)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def chip(draw, x, y, label, color):
    """Small filled tag with white bold text; returns its width."""
    f = font(SANS_B, 15)
    w = int(draw.textlength(label, font=f)) + 18
    draw.rectangle([x, y, x + w, y + 24], fill=color)
    draw.text((x + 9, y + 4), label, font=f, fill=WHITE)
    return w


def story(draw, x, y, w, tag, color, headline, summary):
    """One grid story: tag chip, bold headline, short summary."""
    chip(draw, x, y, tag, color)
    y += 32
    y = text_block(draw, x, y, headline, font(SANS_B, 21), INK, w, 25)
    y += 2
    text_block(draw, x, y, summary, font(SANS, 15), (45, 43, 40), w, 20)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    inner_w = W - 2 * MARGIN

    # ---- Masthead ------------------------------------------------------
    d.rectangle([0, 0, W, 110], fill=(16, 16, 16))
    title = "THE WORLD IN ONE DAY"
    tf = font(SERIF_B, 50)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 10), title, font=tf, fill=WHITE)
    date = "SATURDAY, NOVEMBER 21, 2026"
    df = font(SANS_B, 25)
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 70), date, font=df, fill=(232, 184, 75))

    # ---- Lead story ----------------------------------------------------
    y = 124
    chip(d, MARGIN, y, "WAR IN EUROPE — UKRAINE & POLAND", RED)
    y += 34
    y = text_block(
        d, MARGIN, y,
        "Russia Fires 400+ Drones and 110 Missiles at Ukraine — Strikes Land in Poland",
        font(SANS_B, 31), INK, inner_w, 38,
    )
    y += 3
    y = text_block(
        d, MARGIN, y,
        "Bridges, rail stations and energy sites were hit in Kyiv; at least 8 people "
        "were killed and power was cut across 10 regions. Two Russian missiles and a "
        "suspected drone came down in eastern Poland — NATO called it a grave "
        "violation of its airspace.",
        font(SANS, 17), (45, 43, 40), inner_w, 23,
    )
    y += 8
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=3)
    grid_top = y + 14

    # ---- Six-story grid (2 columns x 3 rows) ---------------------------
    col_w = (inner_w - 28) // 2
    col_x = [MARGIN, MARGIN + col_w + 28]
    row_h = 166
    stories = [
        ("MARKETS", (30, 90, 140),
         "AI Sell-Off Deepens: S&P 500 Falls into Correction",
         "Stocks slid worldwide: the S&P 500 fell about 3.7% on the day and Japan's "
         "Nikkei dropped 5.1%. Anthropic slid on its second day of trading, closing "
         "at $88.91 after a debut valuing it at ~$2 trillion."),
        ("STRAIT OF HORMUZ", (0, 110, 110),
         "Two Tankers Hit at the Strait's Entrance",
         "Unidentified projectiles struck two outbound tankers near Khasab, Oman, "
         "at the strait's entrance, UK maritime officials said. No casualties; "
         "US-Iran talks remain stalled."),
        ("HEALTH", (30, 120, 60),
         "Daily Pill Makes Pancreatic Cancer Vanish in Trial",
         "In a trial, a daily pill called daraxonrasib made pancreatic cancer "
         "undetectable in 1 in 12 patients — a rare breakthrough against one of "
         "the deadliest cancers."),
        ("BRUSSELS — UK & EU", (70, 60, 140),
         "UK and EU Sign Three Post-Brexit Deals",
         "Britain and the EU signed agreements on food trade, carbon trading and "
         "youth mobility, with Prime Minister Andy Burnham signing for the UK "
         "in Brussels."),
        ("CLIMATE — COP31", (170, 110, 20),
         "Climate Talks Run Past Deadline, No Deal",
         "COP31 in Antalya, Turkey ran past its Friday deadline with no agreement, "
         "after fossil-fuel language was dropped from the draft text."),
        ("UNITED STATES — CYBER", (120, 40, 90),
         "Hackers Breach FBI Crime Database",
         "Hackers breached the FBI's National Crime Information Center database "
         "and a USDA payment system. The FBI is investigating both intrusions."),
    ]
    for i, (tag, color, head, summ) in enumerate(stories):
        r, c = divmod(i, 2)
        story(d, col_x[c], grid_top + r * row_h, col_w, tag, color, head, summ)
    # vertical divider between the columns
    mid_x = MARGIN + col_w + 14
    d.line([mid_x, grid_top, mid_x, grid_top + 3 * row_h - 12],
           fill=(190, 184, 170), width=2)

    # ---- Full-width story: Denmark -------------------------------------
    y = grid_top + 3 * row_h + 4
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=3)
    y += 12
    chip(d, MARGIN, y, "DENMARK — SECURITY", (60, 60, 60))
    y += 32
    y = text_block(
        d, MARGIN, y,
        "Denmark Expels Russian Defence Attaché Over Alleged Assassination Plot",
        font(SANS_B, 21), INK, inner_w, 26,
    )
    y += 2
    y = text_block(
        d, MARGIN, y,
        "Copenhagen expelled Russia's defence attaché and arrested two men over an "
        "alleged plot to kill US-Ukrainian rapper Kyivstoner near the Danish capital.",
        font(SANS, 15), (45, 43, 40), inner_w, 20,
    )

    # ---- Footer strip ----------------------------------------------------
    d.rectangle([0, H - 56, W, H], fill=(16, 16, 16))
    foot = ("FAR FROM THE HEADLINES: ESA/JAXA's BepiColombo spacecraft "
            "reached orbit around Mercury.")
    ff = font(SANS_B, 17)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, H - 38), foot, font=ff, fill=(232, 184, 75))

    img.save("assets/entry.png", optimize=True)
    print("saved assets/entry.png")


if __name__ == "__main__":
    main()

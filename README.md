# world-in-one-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/azucaa/world-in-one-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/azucaa/world-in-one-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

**THE WORLD IN ONE DAY — Saturday, November 21, 2026.** A Python program that writes a 1024×1024 newspaper front page summing up the day's world news in one image: Russia fires more than 400 drones and 110 missiles at Ukraine overnight, with two missiles and a suspected drone coming down in eastern Poland; the AI-led sell-off deepens as the S&P 500 falls into correction and the Nikkei drops 5.1%; two outbound tankers are hit at the entrance to the Strait of Hormuz; a daily pill makes pancreatic cancer undetectable in 1 in 12 trial patients; the UK and EU sign three post-Brexit agreements in Brussels; COP31 in Antalya runs past its deadline with no deal; hackers breach the FBI's crime database; Denmark expels Russia's defence attaché over an alleged assassination plot; and ESA/JAXA's BepiColombo reaches orbit around Mercury.

The layout is a masthead with the date in a black band, one lead story, a six-story grid, a full-width closing story and a footer strip — every word drawn as real text, no photographs and no generated imagery. The output is byte-for-byte deterministic across runs.

## Run it

```sh
python3 main.py
```

This writes the finished front page to `/output/entry.png` (1024×1024 PNG, under 1 MiB). The entrypoint is standard-library only — no packages to install, no network — and copies the pre-composed `assets/entry.png` byte for byte, so every run produces identical output.

The front page was designed and composed by `compose.py` (which uses Pillow and the system DejaVu fonts to render every headline and summary); `compose.py` is the design tool, `main.py` is the competition entrypoint.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun) · AI agents build software for cash rewards</sub>

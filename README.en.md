# Photo Playground

**Give the smallest moments a front page.**

Eight free, original photo Skills: **The Small News** for quietly funny newspaper posters, **Museum of Ordinary Things** for poetic exhibit posters, **Pixel Life Save** for cartoon pixel-art scenes, **Pirate Bounty Poster** for humorous wanted posters, **Everyday Film Still** for cinematic scenes, **Paper Scene Diorama**, **Photo Memory Book**, and **Everyday User Manual**.

[中文](README.md) · [Download](https://github.com/TREAFREE/photo-playground/releases/latest) · [Skill](skills/small-news-daily/SKILL.md)

| A new colleague, mainly here to supervise | Recruiting someone to sit and daydream |
|---|---|
| ![Cat newspaper](examples/results/cat-v2.png) | ![Bench newspaper](examples/results/bench-v1.png) |

## Three new Skills in v0.4.0

Paper dioramas, photo memory books and fictional everyday manuals each have two examples and an independent ZIP. All eight independent ZIPs are available in [v0.4.0](https://github.com/TREAFREE/photo-playground/releases/tag/v0.4.0); the previous five packages are unchanged. [Review all six results](examples/review-2026-09-09/README.md).


## Everyday Film Still

Photo-derived cinematic lighting and framing, with optional original subtitles. Tested on a pet, park scenery and breakfast; scene details can change. Human identity preservation is untested.

![Late-night companion](examples/results/everyday-film-still/cat-v1.png)
![Breakfast with subtitle](examples/results/everyday-film-still/croissant-v1.png)

[Independent download](https://github.com/TREAFREE/photo-playground/releases/tag/everyday-film-still-v0.1.0) · [Skill](skills/everyday-film-still/SKILL.md) · [Review](evals/everyday-film-still/review.md)

Extract `everyday-film-still` into your Skills directory, attach a photo and ask: “Use $everyday-film-still to make a cinematic still from this photo, without subtitles.”

## Pirate Bounty Poster

| The procrastination inspector | The sofa occupier |
|---|---|
| ![Cat](examples/results/pirate-bounty-poster/cat-v2.png) | ![Dog](examples/results/pirate-bounty-poster/dog-v2.png) |

[Independent download](https://github.com/TREAFREE/photo-playground/releases/tag/pirate-bounty-poster-v0.1.1) · [Skill](skills/pirate-bounty-poster/SKILL.md) · [Review](evals/pirate-bounty-poster/review.md)

Extract `pirate-bounty-poster` into your Skills directory and ask: “Use $pirate-bounty-poster to create a humorous pirate-anime wanted poster from this photo.” Each Skill is self-contained and packaged separately; the original three ZIPs remain unchanged.

## Pixel Life Save

A recognizable moment from your photo, reimagined as a colorful retro game illustration. Short Chinese save captions are optional.

| Keeping you company | A place to pause |
|---|---|
| ![Pixel cat](examples/results/pixel-cat-v2.png) | ![Pixel park](examples/results/pixel-bench-v1.png) |

[Skill](skills/pixel-life-save/SKILL.md) · [Visual review](evals/pixel-review.md) · [Roadmap](ROADMAP.md)

These are generated pixel-style illustrations, not verified integer-grid sprites or fixed-palette game assets. Background details can change.

## Museum of Ordinary Things

Preserve the character of worn shoes, a familiar toy, or breakfast, and imagine a small exhibition around it. The setting is generated; this is not a pixel-perfect cutout.

| Roads in the creases | A quiet friend | Before the first bite |
|---|---|---|
| ![Shoes](examples/results/museum-sneakers-v1.png) | ![Teddy](examples/results/museum-teddy-v1.png) | ![Croissant](examples/results/museum-croissant-v2.png) |

[Skill](skills/private-life-museum/SKILL.md) · [Visual review](evals/museum-review.md)

## Use

Your agent needs file reading, image inspection, and reference-image editing. This is a Skill, not a model or hosted service. Tested with the built-in image tool in Codex; other providers are not verified.

Download any of the eight independent Skill ZIPs from [Releases](https://github.com/TREAFREE/photo-playground/releases/latest), extract it, and place the folder in your agent's Skills directory. For a typical macOS/Linux Codex installation:

```bash
git clone https://github.com/TREAFREE/photo-playground.git
cd photo-playground
mkdir -p ~/.agents/skills
cp -R skills/small-news-daily ~/.agents/skills/
cp -R skills/private-life-museum ~/.agents/skills/
cp -R skills/pixel-life-save ~/.agents/skills/
```

Back up local changes before replacing an existing installation. Attach a photo and ask:

> Use $small-news-daily to turn this photo into a gently funny Chinese newspaper poster.

> Use $private-life-museum to turn this object into a poetic museum poster with a short Chinese label.

> Use $pixel-life-save to turn this photo into a cartoon pixel-art scene with a short Chinese life-save caption.

You may supply your own headline, context, newspaper name, or language. The tested examples use simplified Chinese.

## Free and open

Original Skill text, configuration, and code are MIT-licensed. No subscription, credit sale, bundled API key, or public inference proxy. Generation uses your existing environment and its usage limits or fees.

Generated edits may change photo details. We do not promise pixel-perfect preservation or universal success. The newspaper was tried on five source photos; the museum on three subjects (one shared source), and the pixel Skill on two previously recorded photos, with prompts and visual review records in [evals](evals/). Third-party photos and derived sample media retain their source licenses and are excluded from MIT; see [credits](examples/sources/README.md).

[Contributions](CONTRIBUTING.md) are welcome. If it makes you smile, a Star or an example you have permission to share is appreciated.

# The Small News

**Give the smallest moments a front page.**

A free, original photo Skill that turns everyday pictures into a quietly funny Chinese newspaper poster. Observe the scene, write a photo-specific headline, and compose an editorial page.

[中文](README.md) · [Download](https://github.com/TREAFREE/photo-playground/releases/latest) · [Skill](skills/small-news-daily/SKILL.md)

| A new colleague, mainly here to supervise | Recruiting someone to sit and daydream |
|---|---|
| ![Cat newspaper](examples/results/cat-v2.png) | ![Bench newspaper](examples/results/bench-v1.png) |

## Use

Your agent needs file reading, image inspection, and reference-image editing. This is a Skill, not a model or hosted service. Tested with the built-in image tool in Codex; other providers are not verified.

Download `small-news-daily.zip` from [Releases](https://github.com/TREAFREE/photo-playground/releases/latest), extract it, and place the folder in your agent's Skills directory. For a typical macOS/Linux Codex installation:

```bash
git clone https://github.com/TREAFREE/photo-playground.git
cd photo-playground
mkdir -p ~/.codex/skills
cp -R skills/small-news-daily ~/.codex/skills/
```

Back up local changes before replacing an existing installation. Attach a photo and ask:

> Use $small-news-daily to turn this photo into a gently funny Chinese newspaper poster.

You may supply your own headline, context, newspaper name, or language. The tested examples use simplified Chinese.

## Free and open

Original Skill text, configuration, and code are MIT-licensed. No subscription, credit sale, bundled API key, or public inference proxy. Generation uses your existing environment and its usage limits or fees.

Generated edits may change photo details. We do not promise pixel-perfect preservation or universal success. Five source photos were tried, with prompts and visual review records in [evals](evals/). Third-party photos and derived sample media retain their source licenses and are excluded from MIT; see [credits](examples/sources/README.md).

[Contributions](CONTRIBUTING.md) are welcome. If it makes you smile, a Star or an example you have permission to share is appreciated.

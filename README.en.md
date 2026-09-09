# Photo Playground · 13 Open-Source Photo Skills

**Turn everyday photos into something worth sharing.**

Thirteen free, independently packaged photo Skills. Use your own image-generation environment; no subscriptions or inference credits sold here.

Official repository: **[TREAFREE/photo-playground](https://github.com/TREAFREE/photo-playground)**. Open this URL directly, or search GitHub for `photo-playground user:TREAFREE`. Includes photo-to-poster, pixel art, paper dioramas, photo books and cinematic stills for image-capable Codex workflows. See the [Doubao usage and testing notes](docs/doubao.md) for platform-specific limitations.

[中文 / full visual gallery](README.md) · [Download individual ZIPs](https://github.com/TREAFREE/photo-playground/releases/latest) · [Validation scope](docs/skill-status.md)

| Photo-sketch collage | Architectural relief print |
|---|---|
| ![Collage](examples/results/scene-sketch-collage/temple-v1.png) | ![Relief](examples/results/architectural-relief-poster/temple-v1.png) |

New in v0.6.0: `scene-sketch-collage` and `architectural-relief-poster`. Existing eleven Skills are unchanged. [Before/after gallery](examples/review-v0.6.0/README.md).

## Use

Ask Codex to install one Skill from this repository, then attach a photo and invoke it, for example:

```text
Use $scene-sketch-collage to transform this photo. Keep the subject recognizable; use a short English caption.
```

An image-capable agent must read the complete Skill and any linked references. Each ZIP is self-contained; back up local edits before updating that Skill.

Doubao was tested with a photo and pasted architectural-relief rules: it generated an image but changed the requested typography. That ordinary-chat result does not establish Doubao Work compatibility: public walkthroughs demonstrate GitHub Skill installation through its task/skill-creation interface. Installation of this repository in Doubao Work and other Skills remain unverified. [Actual test and instructions](docs/doubao.md).

## Scope and license

Sample-tested does not mean reliable for every input. Generated edits can change identity and details. Bead art is not a craft chart; book images are not a flipbook application; print-style images are not prepress separations.

Original rules and code are [MIT licensed](LICENSE). Third-party photos and example media containing them retain their source terms; see [credits](examples/sources/README.md). No third-party Skills or reference artworks are bundled. Sponsorship, if introduced, will be disclosed and will not be inserted into user outputs.

# Scrapybara CLI

Scrapybara Bounty Force Winner Project by @keell0renz (Bohdan Agarkov)

> Wake up, Bara... Follow the Capybara hole...

## Installation

Simply install with pip:

```bash
pip install scrapybara-cli
```

For contributing/development:

```bash
git clone https://github.com/Scrapybara/scrapybara-cli.git
cd scrapybara-cli
pip install -e .
```

## Usage

1. Set up your environment variables
2. Run the CLI:

```bash
export ANTHROPIC_API_KEY=your_anthropic_api_key
export SCRAPYBARA_API_KEY=your_scrapybara_api_key
```

Without Anthropic API key agent credits will be used from your Scrapybara account.

Also its a good idea to add the environment variables to your shell profile so they are always available.

```bash
scrapybara-cli
```

```bash
❯ scrapybara-cli
Stream URL: http://35.86.194.243:6091/?resize=scale&autoconnect=1
> Who is deez nuts

I'll help you search for information about "deez nuts" using Chromium.
(instance) $ (DISPLAY=:1 chromium &)
Screenshot
Moving mouse
Clicking
Typing: what is deez nuts meme origin
Pressing key 'RETURN'

Let me explain what "Deez Nuts" is based on the search results:

"Deez Nuts" is a popular internet meme and comedic phrase that originated in 1992 from Dr. Dre's album "The Chronic" in a skit called "Deeez Nuuuts." The phrase gained widespread popularity
in 2015 when a viral video featured WelvenDaGreat saying "Deez Nuts! Ha! Got eem!" The phrase is typically used as part of a joke or prank where someone is led into a setup question, only to
be responded to with "deez nuts" as a punchline.

The phrase became so popular that in 2015, it even became a satirical presidential campaign, when a 15-year-old from Iowa filed to run for president under the name "Deez Nuts." This filing
gained significant media attention and became a viral sensation.

The phrase continues to be used in internet culture, memes, and casual conversation as a playful joke or response, often catching people off guard with its unexpected delivery.
```

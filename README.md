# Scrapybara CLI

> Wake up, Bara... Follow the Capybara hole...

## Installation

Simply install with pip:

```bash
pip install scrapybara-cli
```

Then run from anywhere:

```bash
scrapybara-cli --instance-type small
```

## Development Setup

For contributing/development:

```bash
git clone https://github.com/yourusername/scrapybara-cli.git
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

```bash
scrapybara-cli
```

```bash
❯ scrapybara-cli
Stream URL: http://52.42.218.5:6091/?resize=scale&autoconnect=1
> Hello! Who is Deez Nuts?
I'll help you search for information about "Deez Nuts." Let me use the web browser to look this up.
Taking screenshot
Let me click on the web browser icon and search for information about Deez Nuts.
Moving mouse
Clicking
Moving mouse
Clicking
Typing
Pressing key Return
Based on the search results, "Deez Nuts" has two main notable meanings:

1. As a Political Satire:
- "Deez Nuts" was a satirical presidential candidate portrayed by Brady C. Olson who ran for president of the United States in 2016
- Olson was 15 years old at the time and filed a statement of candidacy with the Federal Election Commission on July 26, 2015
- He was a resident of Wallingford, Iowa

2. As a Slang Term/Joke:
- "Deez nuts" (or "deez nutz") is a slang term and euphemism for "testicles"
- It's also known as the punchline of a setup joke that involves asking someone a vague question to solicit a follow-up question, before yelling out the phrase in an obnoxious manner
- The phrase gained popularity as a joke and internet meme, particularly after the satirical presidential campaign

The term has become a well-known part of internet and popular culture, combining both its use as a juvenile joke and its later adoption as a satirical political statement.

Would you like me to provide more specific information about either the satirical campaign or the phrase's origins as a joke?
```

Available instance types:

- small
- medium
- large

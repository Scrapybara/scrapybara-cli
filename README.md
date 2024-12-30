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
scrapybara-cli --instance-type small
```

Available instance types:

- small
- medium
- large

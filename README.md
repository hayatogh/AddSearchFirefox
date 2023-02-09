# Add Any Search Engine to Firefox

## How to Add

1. Edit `searches.json`
    - %s is replaced by search terms
1. Execute `python3 main.py`
1. Open `localhost:8000` in Firefox
1. Click URL bar or Search box and type some text
1. Click "Add search engine"
1. Optionally, add search keyword in preferences


## How it works

Firefox installs search engines from OpenSearch description format.
And it doesn't install them from local pages.

This `main.py` creates necessary files from `searches.json` and serves them.

Handwritten example is in `sample` directory.
Run `python3 -m http.server` in it to demonstrate.

https://developer.mozilla.org/en-US/docs/Web/OpenSearch


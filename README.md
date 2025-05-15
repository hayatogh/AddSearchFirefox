# Add Any Search Engine to Firefox

## How to Add

1. Edit `searches.toml`
    - %s is replaced by search terms
1. Execute `python3 main.py`
1. Open displayed URL such as `https://localhost:XXXX` with Firefox
    - The URL on your terminal may be clickable while pressing some modifier keys
1. Click URL bar or search box
1. Type some text
1. Click a search engine icon with green plus tips
1. Optionally, add search keywords in Firefox's preferences


## How this project is useful for you

Pros.
- Easy to customize search URLs, such as adding language parameters
- Easy to transfer to other machines or profiles
- Easy to maintain; only a TOML file
- Works offline, providing the privacy needed for company internal search URLs
- Not an addon.  After you added search engines, you can remove the downloaded repository
  and forget.

Cons.
- No sync with Firefox Sync
  Currently, writing a public browser extension is the only way
  to add your custom search URLs to Firefox and sync with Firefox Sync.


## How it works

Firefox installs search engines defined by OpenSearch description format.
And it doesn't install them from local pages.

This project creates all necessary files for you and serves them.

Handwritten example of OpenSearch description format is in `sample` directory.
Run `cd sample && python3 -m http.server` to see its working.

https://developer.mozilla.org/en-US/docs/Web/XML/Guides/OpenSearch

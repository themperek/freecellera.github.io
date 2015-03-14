# Content for freecellera.org

[![Build Status](https://travis-ci.org/Freecellera/freecellera.github.io.svg?branch=sources)](https://travis-ci.org/Freecellera/freecellera.github.io)

To contribute please fork this repo and submit a pull request.

Website is generated using [Pelican](http://docs.getpelican.com/en/3.5.0/).

Content lives in `content/pages` and can be either Markdown or
ReStructuredText.  Blog style postings live in `content`.

### Usage:

Install python modules:
```bash
pip install pelican ghp-import markdown
```

Generate pages:
```bash
make publish
```

Generated pages will be in `output` folder.

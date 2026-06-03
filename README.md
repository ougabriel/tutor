# Free Exam Dumps Link Scraper

Terminal scraper for ExamTopics discussion pages. The app asks for a provider and exam name/code, scans all provider discussion pages with maximum parallel workers, and writes the matching discussion links to a text file.

## Setup

Run once:

```text
install_dependencies.bat
```

This creates the local virtual environment, installs Python packages, and fetches the Camoufox browser runtime.

## Run

Double-click:

```text
run_scraper.bat
```

Or from a terminal:

```text
python main.py
```

## Terminal Flow

The app shows only:

```text
1. Scrape
2. Exit
```

For scrape, it asks only:

```text
Provider
Exam name or code
```

After that, scraping starts automatically. Output is saved as:

```text
<EXAM> dumps.txt
```

Example:

```text
DOP-C02 dumps.txt
```

## Project Layout

```text
main.py                    # terminal app
examtopics/fast_scanner.py # parallel listing scan
examtopics/browser_scraper.py
examtopics/http_client.py  # pooled requests and retry loop
examtopics/cache.py        # HTML cache
examtopics/parsers.py      # HTML parsing and block detection
examtopics/matching.py     # provider, slug, topic/question matching
examtopics/output.py       # grouped text output
```

## Notes


- The scraper scans provider discussion pages; it does not ask for individual discussion URLs.
- The default worker count is 64.
- Cache defaults to `.examtopics_cache` with a 6-hour lifetime.
- It does not bypass login, contributor access, captcha, or paid limits.

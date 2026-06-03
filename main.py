from pathlib import Path

from examtopics.browser_scraper import CamoufoxScraper
from examtopics.cache import HtmlCache
from examtopics.fast_scanner import FastDiscussionScanner
from examtopics.http_client import HttpFetcher
from examtopics.matching import build_page_numbers, display_slug, normalize_provider
from examtopics.output import write_grouped_links_to_file
from examtopics.settings import (
    DEFAULT_CACHE_DIR,
    DEFAULT_CACHE_TTL_SECONDS,
    DEFAULT_DELAY_RANGE,
    DEFAULT_RETRIES,
    DEFAULT_REQUEST_WORKERS,
    DEFAULT_TIMEOUT_MS,
)


def main():
    print_header()

    while True:
        print("Choose option:")
        print("  1. Scrape")
        print("  2. Exit")
        print()

        choice = input("Enter choice [1]: ").strip() or "1"
        if choice == "1":
            scrape_from_terminal()
            return
        if choice == "2":
            return

        print("Invalid choice.\n")


def print_header():
    print()
    print("=" * 60)
    print("  ExamTopics Scraper")
    print("=" * 60)
    print()


def scrape_from_terminal():
    provider = prompt_required("Provider (example: amazon, hp, microsoft): ")
    exam_code = prompt_required(
        "Exam name or code (example: AIF-C01, HPE7-A07, aws-devops-engineer-professional): "
    )

    provider = normalize_provider(provider)
    cache = HtmlCache(Path(DEFAULT_CACHE_DIR), DEFAULT_CACHE_TTL_SECONDS)
    links = scan_discussion_links(provider, exam_code, cache)

    filename = f"{display_slug(exam_code).upper()} dumps.txt"
    print(f"\nYour file will be named {filename}")
    write_grouped_links_to_file(filename, links)
    print(f"File generation complete. {len(links)} links found.")


def prompt_required(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("[ERROR] Value is required.\n")


def build_fetcher(cache: HtmlCache) -> HttpFetcher:
    return HttpFetcher(
        timeout=DEFAULT_TIMEOUT_MS // 1000,
        retries=DEFAULT_RETRIES,
        cache=cache,
        refresh_cache=False,
    )


def scan_discussion_links(provider: str, exam_code: str, cache: HtmlCache):
    try:
        scanner = FastDiscussionScanner(provider, build_fetcher(cache), delay_range=DEFAULT_DELAY_RANGE)
        total_pages = scanner.get_num_pages()
        page_numbers = build_page_numbers(total_pages, 1, None, None)
        print(f"\nScanning Pages: {page_numbers[0]}-{page_numbers[-1]} ({len(page_numbers)} pages)")
        return scanner.scan(page_numbers, exam_code, workers=DEFAULT_REQUEST_WORKERS)
    except Exception as exc:
        print(f"Fast scan failed; falling back to Camoufox: {exc}")

    with CamoufoxScraper(
        provider,
        headless=True,
        timeout_ms=DEFAULT_TIMEOUT_MS,
        retries=DEFAULT_RETRIES,
        delay_range=DEFAULT_DELAY_RANGE,
    ) as scraper:
        total_pages = scraper.get_num_pages()
        page_numbers = build_page_numbers(total_pages, 1, None, None)
        print(f"\nScanning Pages: {page_numbers[0]}-{page_numbers[-1]} ({len(page_numbers)} pages)")
        return scraper.get_discussion_links(page_numbers, exam_code)


if __name__ == "__main__":
    main()

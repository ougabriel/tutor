from typing import Dict, List

from .matching import dedupe, extract_topic_question


def write_grouped_links_to_file(filename: str, links: List[str]):
    grouped_links: Dict[int, List[str]] = {}
    for link in sorted(dedupe(links), key=lambda item: (*extract_topic_question(item), item)):
        topic, _ = extract_topic_question(link)
        grouped_links.setdefault(topic, []).append(link)

    with open(filename, "w", encoding="utf-8") as file:
        for topic, topic_links in grouped_links.items():
            topic_label = "Unknown Topic" if topic == 10**9 else f"Topic {topic}"
            file.write(f"{topic_label}:\n")
            for link in topic_links:
                file.write(f" - {link}\n")
            print(f"{topic_label} links added to file.")


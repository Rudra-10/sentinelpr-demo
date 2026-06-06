from agent.ingestion import fetch_pr_diff, pretty_print_diff

if __name__ == "__main__":
    pr = fetch_pr_diff(pr_number=1)
    pretty_print_diff(pr)
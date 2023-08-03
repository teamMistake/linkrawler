from getLink import getLink
from getHtml import getHtml
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword", type=str, default="")
    parser.add_argument("--pages", type=int, default=1)
    parser.add_argument("--path", type=str, default="./html/")
    args = parser.parse_args()

    getLink(args.keyword, args.pages)
    getHtml(args.path)
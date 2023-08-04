from getLink import getLinkByCategory, getLinkByKeyword
from getHtml import getHtml
import argparse

from config import category_dict

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, help="Choose getLink mode with \"category\" or \"keyword\".")
    parser.add_argument("--category", type=str, default="", help="Input your category with category mode.\n" +
                        "options: " + " | ".join(list(category_dict.keys())))
    parser.add_argument("--keyword", type=str, default="", help="Input your category with keyword mode.")
    parser.add_argument("--pages", type=int, default=1, help="Maximum pages to get link.")
    parser.add_argument("--path", type=str, default="./html/", help="Choose directory to download full HTML.")
    args = parser.parse_args()

    if(args.mode == "category"):
        link_name, category = getLinkByCategory(args.category, args.pages)
        getHtml(link_name, category, args.path)
    elif(args.mode == "keyword"):
        link_name, keyword = getLinkByKeyword(args.keyword, args.pages)
        getHtml(link_name, keyword, args.path)
    else: print("*** Alert: mode not selected. ***")
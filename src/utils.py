import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def objects_from_json(data: list[dict]) -> Any:
    new_category = []
    for meaning in data:
        new_product = []
        for prod in meaning["products"]:
            new_product.append(Product(**prod))
        meaning["products"] = new_product
        new_category.append(Category(**meaning))
    return new_category


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    json_data = objects_from_json(raw_data)

    print(raw_data)
    print(json_data)
    print(json_data[0].product_count)
    print(json_data[0].description)

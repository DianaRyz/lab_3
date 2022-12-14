import csv
import os


def write_element(i: int, class_name: str, dataset_path: str, path_csv: str) -> None:

    """
    Record i-th element
        i(int) - item number
        class_name(str) - tiger or leopard
        dataset_path(str) - path to the directory
        csv_path(str) - path to the csv-file
    """

    headings = ["Absolute way", "Relative way", "Class"]
    with open(path_csv, "a", newline="", encoding="utf-8") as file:
        write_in_file = csv.DictWriter(
            file, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        path = f"D:/dataset/{class_name}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(path):
            write_in_file.writerow(
                {
                    "Absolute way": dataset_path + f"/{class_name}/{str(i).zfill(4)}.jpg",
                    "Relative way": f"dataset/{class_name}/{str(i).zfill(4)}.jpg",
                    "Class": class_name,
                }
            )


def annotation(dataset_path: str, path_csv: str, csv_name: str = "annotation.csv") -> str or None:
    """
    Writing an annotation of a dataset to a file
        dataset_path(str) - path to the directory
        csv_path(str) - path to the csv-file
    """
    headings = ["Absolute way", "Relative way", "Class"]
    with open(os.path.join(path_csv, csv_name), "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=headings, delimiter=";", quoting=csv.QUOTE_ALL
        )
        writer.writeheader()

    class_name = "tiger"
    path_class = dataset_path + "/" + class_name
    count_files = len(
        [
            element
            for element in os.listdir(path_class)
            if os.path.isfile(os.path.join(path_class, element))
        ]
    )

    for i in range(0, count_files):
        write_element(i, class_name, dataset_path, os.path.join(path_csv, csv_name))

    class_name = "leopard"
    path_class = dataset_path + "/" + class_name
    count_files = len(
        [
            element
            for element in os.listdir(path_class)
            if os.path.isfile(os.path.join(path_class, element))
        ]
    )

    for i in range(0, count_files):
        write_element(i, class_name, dataset_path, os.path.join(path_csv, csv_name))

    return os.path.join(path_csv, csv_name)


if __name__ == "__main__":
    path_dataset = "D:/dataset"
    csv_path = "annotation"
    annotation(path_dataset, csv_path)
import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    _, filepath, report_type = sys.argv

    if filepath.endswith(".xml"):
        report = InventoryRefactor(XmlImporter)

    if filepath.endswith(".csv"):
        report = InventoryRefactor(CsvImporter)

    if filepath.endswith(".json"):
        report = InventoryRefactor(JsonImporter)

    return sys.stdout.write(report.import_data(filepath, report_type))

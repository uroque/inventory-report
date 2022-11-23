import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def csv_read(filepath):
        with open(filepath, "r") as csv_file:
            reader = list(csv.DictReader(csv_file))
            return reader

    def json_read(filepath):
        with open(filepath, 'r') as file:
            reader = json.load(file)
            return reader

    def xml_read(filepath):
        with open(filepath, 'r') as file:
            reader = xmltodict.parse(file.read())
            return reader["dataset"]["record"]

    @classmethod
    def data_reader(cls, filepath):
        if filepath.endswith(".csv"):
            return cls.csv_read(filepath)
        elif filepath.endswith(".json"):
            return cls.json_read(filepath)
        elif filepath.endswith(".xml"):
            return cls.xml_read(filepath)

    @classmethod
    def import_data(cls, filepath, type):
        data = cls.data_reader(filepath)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)

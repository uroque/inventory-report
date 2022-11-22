import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class Inventory:
    def csv_read(filepath):
        with open(filepath, "r") as csv_file:
            reader = list(csv.DictReader(csv_file))
            return reader

    @classmethod
    def data_reader(cls, filepath):
        return cls.csv_reader(filepath)
    @classmethod
    def import_data(cls, filepath, type):
        data = cls.data_reader(filepath)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)

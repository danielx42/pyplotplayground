from flask import Flask, jsonify, request
import xlrd


class Record:
    def __init__(self, name):
        self.name = name
        self.measurements = []

    def add_measurement(self, measurement):
        self.measurements.append(measurement)

    def to_dict(self):
        return {self.name : self.measurements}

def getArrayData(path, id):
    valuesList = []
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)
    for i in range(1, sheet.ncols):
        valuesList.append(Record(sheet.cell_value(0, i)))

        # titleList.append(sheet.cell_value(0, i))

    for i in range(sheet.nrows):
        pid = sheet.cell_value(i, 0)
        if pid == id:
            for j in range(1, sheet.ncols):
                valuesList[j - 1].add_measurement(sheet.cell_value(i, j))

    return valuesList


app = Flask(__name__)


@app.route('/')
def hello_method():
    return "<html><div>Use path /pdata/, parameters are pid string and col int</div></html>"


@app.route('/pdata/', methods=['GET'])
def returnpdata():
    pid = request.args.get('pid', 1, type=str)
    col = request.args.get('col', 1, type=int)

    valuesList = []
    path = "c:\\Dev\\patient_values2.xlsx"
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)

    for i in range(1, sheet.ncols):
        valuesList.append(Record(sheet.cell_value(0, i)))
    for i in range(sheet.nrows):
        cpid = sheet.cell_value(i, 0)
        if cpid == pid:
            for j in range(1, sheet.ncols):
                valuesList[j-1].add_measurement(sheet.cell_value(i, j))

    vname = valuesList[col].name
    vmeasurement = valuesList[col].measurements

    dicter = dict({'name': vname, 'measurements': vmeasurement})

    return jsonify(dicter)


if __name__ == '__main__':
    app.run()




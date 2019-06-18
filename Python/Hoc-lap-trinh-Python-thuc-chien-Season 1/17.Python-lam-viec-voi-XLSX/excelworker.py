import openpyxl
# youtube.com/tranducloi
# Tại sao sử dụng Openpyxl?
# - Có khả năng làm việc (đọc/ghi) với XLSX
# - Có khả năng ghi thêm/chỉnh sửa 1 file XLSX có sẵn -> cực kỳ quan trọng
# - Làm việc tốt hơn với các phiên bản Python 3.x x64bit >> càng lớn càng tốt và openpyxl mới nhất

class ExcelWorker(object):
    def __init__(self):
        super().__init__()
        self.wb = None
        self.filepath = "./loitd_report.xlsx"

    def write2excel(self, data, sheetname="", startrow=0, startcol=0, filepath="./loitd_report.xlsx", templatefile="./template.xlsx"):
        '''This function help you write to excel XLSX in batch.
        Available by youtube.com/tranducloi
        data format:
        data = [('Jan', 1999),('Feb', 2019)]
        '''
        self.filepath = filepath
        try:
            if self.wb is not None:
                print("File already opened!")
            else:
                print("Opening excel file: {0}".format(templatefile))
                self.wb = openpyxl.load_workbook(templatefile)
            ws = self.wb[sheetname]

            for i in range(0, len(data)):
                for j in range(0, len(data[i])):
                    print("Processing: {0}:{1}:{2}:{3}".format(i,j,data[i][j],data[i]))
                    _ = ws.cell(column=j+startcol, row=i+startrow, value=data[i][j]) # command to write data to cell
            print("Done writing data.")
        except Exception as e:
            print(e)
    
    def saveExcel(self):
        # set active sheet to 1
        print("Set active sheet to 1st ...")
        self.wb.active = 0
        # now saving
        self.wb.save(self.filepath)
        print("Done saving file: {0}".format(self.filepath))

if __name__ == "__main__":
    ew = ExcelWorker()
    data = [('Jan', 1999),('Feb', 2019)]
    ew.write2excel(data=data,sheetname="youtube.com",startrow=5, startcol=3)
    ew.saveExcel()
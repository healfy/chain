from typing import Any
from app.handlers import XMLHandler, TXTHandler, JSONHandler, CSVHandler
from app.shared import Logger


class LoggerTest(Logger):

    collection = []

    def log(self, obj: Any):
        self.collection.append(obj)


def test_main():
    logger = LoggerTest()
    handler = XMLHandler(logger)
    txt = TXTHandler(logger)
    jsn = JSONHandler(logger)
    csv = CSVHandler(logger)
    files = ['1.xml', ' 2.json', ' 3.csv', ' 4.txt']
    handler.set_next(jsn).set_next(csv).set_next(txt)

    for file in files:
        file = file.replace(' ', '')
        handler.handle(file)
    with open(TXTHandler.result_file, 'w+') as f:
        f.write('')
    for index, file in enumerate(files):
        assert file in logger.collection[index]

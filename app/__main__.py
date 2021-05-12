import argparse
import typing
from .handlers import XMLHandler, TXTHandler, JSONHandler, CSVHandler
from .shared import Logger

if __name__ == '__main__':
    logger = Logger()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files', help='list of files 1.xml, 2.json, 3.csv, 4.txt', type=str)
    args = parser.parse_args()
    files: typing.List[typing.AnyStr] = args.files.split(',')
    handler = XMLHandler(logger)
    txt = TXTHandler(logger)
    jsn = JSONHandler(logger)
    csv = CSVHandler(logger)
    handler.set_next(jsn).set_next(csv).set_next(txt)

    with open(handler.result_file, 'w+') as f:
        f.write('')

    for file in files:
        file = file.replace(' ', '')
        handler.handle(file)
    print(f'You can check result in file {XMLHandler.result_file}')

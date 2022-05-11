from database.models import db
from parser import avito_parser
from parser import cian_parser
from parser import yandex_parser


def main():
    avito_parser.main()
    cian_parser.main()
    yandex_parser.main()
    db.close()


if __name__ == '__main__':
    main()

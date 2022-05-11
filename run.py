from database.models import db
from parsers import avito_parser
from parsers import cian_parser
from parsers import yandex_parser


def main():
    avito_parser.main()
    cian_parser.main()
    yandex_parser.main()
    db.close()


if __name__ == '__main__':
    main()

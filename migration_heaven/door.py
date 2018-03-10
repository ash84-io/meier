import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

import traceback
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from migration_heaven.ghost import migrate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", help="ghost(default) more than...")
    parser.add_argument("-src", help="src")
    parser.add_argument("-dst", help="dst(sqlalchemy connection string format)")
    args = parser.parse_args()
    if not args.m or not args.src or not args.dst:
        parser.print_help()
        sys.exit(2)

    post_list, tag_list, post_tag_list = migrate(src=args.src)

    engine = create_engine(args.dst, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        if post_list:
            session.add_all(post_list)
        if tag_list:
            session.add_all(tag_list)
        if post_tag_list:
            session.add_all(post_tag_list)
        session.commit()
    except Exception:
        print(traceback.format_exc())
        session.rollback()
    session.close()


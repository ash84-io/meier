import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from migration_heaven.ghost import migrate
if __name__ == '__main__':
    migrate(src="./ghost.db", dest='xxx')
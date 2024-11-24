import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

target_dir = os.path.join(current_dir, '../worktree-global')
sys.path.append(target_dir)

from test_para import print_text
print_text()

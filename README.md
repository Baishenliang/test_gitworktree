# test_gitworktree
---

Worktree Demo with Git and Python  
This document outlines how to set up a Git repository with worktree and manage Python files across branches.

---

1. Create a blank folder and clone the repository:  
   git clone https://github.com/Baishenliang/test_gitworktree.git
   cd main

---

2. Add a Worktree for the `global` Branch  
2.1. Use `git worktree` to create a worktree for the `global` branch in a separate directory:  
   `git worktree add ../worktree-global global`
2.2. Verify the worktree setup:  
   `git worktree list`

---

3. Test the Setup  
3.1 Install the conda environment using `environment.yml` in the main branch
3.2: Run the Python Script. In the `main` branch directory, run the script:  
   `python test.py`

From Baishen Liang
baishen.liang@duke.edu
liangbs95@gmail.com
from pathlib import Path

chapter_titles = [
    "primitive_types",
    "arrays",
    "strings",
    "linked_lists",
    "stacks_and_queues",
    "binary_trees",
    "heaps",
    "searching",
    "hash_tables",
    "sorting",
    "binary_search_trees",
    "recursion",
    "dynamic_programming",
    "greedy_algorithms_and_invariants",
    "graphs"
]

helper_titles = [
    "trees",
    "graphs"
]

root_path = Path("./solutions")
helper_path = Path("./helper")
helper_file_extension = ".cpp"
notes_file_name = "notes.txt"

def make_directory(path):
    path.mkdir(parents=True, exist_ok=True)

def make_empty_file(file_path):
    with open(file_path, "w+") as f:
        pass

# Solution directories

make_directory(root_path)

for name in chapter_titles:
    dir_path = root_path / name
    make_directory(dir_path)
    make_empty_file(dir_path / notes_file_name)

# Helper directories & files (to be populated - to be decided based on required template)

make_directory(helper_path)

for name in helper_titles:
    file_path = helper_path / (name + helper_file_extension)
    make_empty_file(file_path)
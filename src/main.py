
import sys
from copystatic import copy_files_recursive
import os
import shutil
from generate_page import generate_page,generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    #print(basepath)
    generate_pages_recursive(dir_path_content,template_path,dir_path_static,basepath)
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    # pages = {"index.md":"index.html",
    #     "blog/glorfindel/index.md":"blog/glorfindel/index.html",
    #     "blog/tom/index.md":"blog/tom/index.html",
    #     "blog/majesty/index.md":"blog/majesty/index.html",
    #     "contact/index.md":"contact/index.html"}
    # for page in pages:
    #     generate_page(
    #         os.path.join(dir_path_content, page),
    #         template_path,
    #         os.path.join(dir_path_public, pages[page]),
    #     )
    

main()
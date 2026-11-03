from functions.get_files_info import get_files_info

directory = "."
if directory == ".":
    print("Result for current directory:")
    print(get_files_info("calculator", "."))
directory = "pkg" 
print(f"Result for '{directory}' directory:")
print(get_files_info("calculator", "pkg"))
directory = "/bin"
print(f"Result for '{directory}' directory:")
print(get_files_info("calculator", "/bin"))
directory = "../"
print(f"Result for '{directory}' directory:")
print(get_files_info("calculator", "../"))
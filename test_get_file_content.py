from functions.get_file_content import get_file_content

def test() -> None:
    # directory = "."
    # if directory == ".":
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    result2 = get_file_content("calculator", "main.py")
    print(result2)
    print(f"main.py length: {len(result2)}")
    print(f"main.py truncated: {'truncated' in result2}")

    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(result3)
    print(f"pkg/calculator.py length: {len(result3)}")
    print(f"pkg/calculator.py truncated: {'truncated' in result3}")

    result4 = get_file_content("calculator", "/bin/cat")
    print(result4)
    print(f"/bin/cat length: {len(result4)}")
    print(f"/bin/cat truncated: {'truncated' in result4}")

    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result5)
    print(f"pkg/does_not_exist.py length: {len(result5)}")
    print(f"pkg/does_not_exist.py truncated: {'truncated' in result5}")

if __name__ == "__main__":
    test()
# directory = "pkg" 
# print(f"Result for '{directory}' directory:")
# print(get_files_info("calculator", "pkg"))
# directory = "/bin"
# print(f"Result for '{directory}' directory:")
# print(get_files_info("calculator", "/bin"))
# directory = "../"
# print(f"Result for '{directory}' directory:")
# print(get_files_info("calculator", "../"))

try:
    with open("sample.txt","r")as file:
        lines=file.readlines()
        line_count=len(lines)
        word_count=sum(len(line.split())for line in lines)
        ch_count=sum(len(line)for line in lines)

    print("fLines:{line_count}")
    print("fWords:{word_count}")
    print("fCharacters:{ch_count}")
except FileNotFoundError:
    print("Error:sample.txt not found.")
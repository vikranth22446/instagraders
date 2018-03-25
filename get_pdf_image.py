import os
import urllib


def download_url(file_path="http://www.mayfieldschools.org/Downloads/Essay%20Prompts%20and%20Scoring%202015.pdf"):
    new_file = "images/" + os.path.split(file_path)[1]
    urllib.urlretrieve(file_path, new_file)
    os.system("convert {file_path}.pdf {file_path}.png".format(file_path=new_file))


if __name__ == '__main__':
    download_url(file_path="http://www.mayfieldschools.org/Downloads/Essay%20Prompts%20and%20Scoring%202015.pdf")

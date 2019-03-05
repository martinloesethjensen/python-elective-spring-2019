import json
import subprocess
import urllib.request


class Cloner(object):

    @staticmethod
    def clone_repo(clone_url):
        subprocess.run(args="git clone " + clone_url)

    def clone_all_repos(self, clone_urls):
        for clone_url in clone_urls:
            self.clone_repo(clone_url=clone_url)


class DataFetcher(object):
    def __init__(self, url):
        self.url = url

    def get_data(self):
        with urllib.request.urlopen(self.url) as response:
            data = json.load(response)
        return data

    @staticmethod
    def get_clone_url_list(data):
        clone_urls = [item['clone_url'] for item in data]
        return clone_urls

    @staticmethod
    def get_names_and_html_urls(data):
        names_and_html_urls = {}
        for item in data:
            names_and_html_urls[item['name'].replace("-", " ")] = item['html_url']
        return names_and_html_urls


class FileWriter(object):

    @staticmethod
    def write_to_file(filename, names_and_html_urls):
        file = open(filename, "w+")

        # Start of the file:
        file.write("# Required Reading\n > Python Elective I Spring 2019\n\n")

        # Put all the necessary data in the file in a sorted order
        for name, html_url in sorted(names_and_html_urls.items()):
            file.write("* [" + name + "](" + html_url + ")\n")

        file.close()


def main():
    # Fetches all the data
    data_fetcher = DataFetcher(url="https://api.github.com/orgs/python-elective-2-spring-2019/repos?per_page=100")
    data = data_fetcher.get_data()
    clone_urls = data_fetcher.get_clone_url_list(data)

    # Clone all repos to directory
    # cloner = Cloner()
    # cloner.clone_all_repos(clone_urls)

    # Get names and html urls
    names_and_html_urls = data_fetcher.get_names_and_html_urls(data)

    # Create README.md file
    FileWriter.write_to_file("README.md", names_and_html_urls)


if __name__ == '__main__':
    main()

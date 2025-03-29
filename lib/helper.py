class Helper:
    def get_files(path):
        import os
        files = []
        for file in os.listdir(path=path):
            if os.path.isfile(f"{path}/{file}"):
                files.append(file)
        return files
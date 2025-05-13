class FileManager:
    def __init__(self,PATH, mode, encoding):
        self.path = PATH
        self.mode = mode
        self.encode = encoding
    def __enter__(self):
        pass
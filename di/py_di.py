# conding: utf-8
from abc import ABCMeta, abstractmethod

class IFWriter(metaclass=ABCMeta):
    @abstractmethod
    def output(self, title : str, body : str):
        pass

class HTMLWriter:
    def output(self, title : str, body : str):
        title_tag = "<title>"+title+"</title>"
        body_tag = "<body><p>"+body+"</p></body>"

        html_text = "<html><head>"+title_tag+"</head>"
        html_text += body_tag
        html_text += "</html>"

        file = open("output.html", 'w')
        file.write(html_text)
        file.close()

class TextWriter(IFWriter):
    def output(self, title : str, body : str):
        text = "Title : "+title
        text += "\n\n"
        text += "Body : "+body
        text += "\n"

        file = open("output.text", 'w')
        file.write(text)
        file.close()

class PrintWriter(IFWriter):
    def output(self, title : str, body : str):
        text = "Title : "+title
        text += "\n\n"
        text += "Body : "+body

        print(text)

class PPrintWriter:
    def output(self, title : str, body : str):
        text = "Title : "+title
        text += "\n\n"
        text += "Body : "+body

        print(text)

class PostManager:
    def __init__(self, writer: IFWriter):
        if not isinstance(writer, IFWriter):
            raise Exception("writer is not IFWriter.")
        self.writer = writer

    def post(self, title : str, body : str):
        self.writer.output(title, body)

if __name__ == '__main__':
    # writer = HTMLWriter()
    # writer = TextWriter()
    writer = PrintWriter()

    post_manager = PostManager(writer)
    # post_manager = PostManager(object)
    
    title = "Title"
    body = "This is body text"
    post_manager.post(title, body)

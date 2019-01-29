# conding: utf-8
from abc import ABCMeta, abstractmethod
from injector import Injector, inject, Module


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
    @inject
    def __init__(self, writer: IFWriter):
        if not isinstance(writer, IFWriter):
            raise Exception("writer is not IFWriter.")
        self.writer = writer

    def post(self, title : str, body : str):
        self.writer.output(title, body)



class DIModule(Module):
    def configure(self, binder):
        binder.bind(IFWriter, to=PrintWriter)
        # binder.bind(IFWriter, to=TextWriter)
        # binder.bind(IFWriter, to=HTMLWriter)

        # binder.bind(IFWriter, to=PPrintWriter)

if __name__ == '__main__':
    injector = Injector([DIModule()])
    post_manager = injector.get(PostManager)

    title = "Title"
    body = "This is body text"
    post_manager.post(title, body)

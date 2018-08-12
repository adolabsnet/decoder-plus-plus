from core.plugin.abstract_plugin import EncoderPlugin

class Plugin(EncoderPlugin):

    def __init__(self, context):
        # Name, Author, Dependencies
        super().__init__('BASE64', "Thomas Engel", ["base64"])

    def run(self, text):
        import base64
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')

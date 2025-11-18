class WhatsApp:
    def chat(self):
        print("Text chatting")

class Instagram:
    def chat(self):
        print("Image and video chatting")

apps = [WhatsApp(), Instagram()]
for app in apps:
    app.chat()   


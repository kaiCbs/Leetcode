class Solution:
    def entityParser(self, text: str) -> str:
        mapp = {
            "quot": '"',
            "apos": "'",
            "amp": "★",
            "gt": ">",
            "lt": "<",
            "frasl": "/",
        }

        for i in mapp:
            text = text.replace("&" + i + ";", mapp[i])
        text = text.replace("★", "&")
        return text
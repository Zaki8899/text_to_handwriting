import pywhatkit as pw

txt = """this is a python program that converts text to handwriting"""
pw.text_to_handwriting(txt, "demo.png", [0, 0, 138])

print("END")

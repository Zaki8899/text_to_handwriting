from handwrite import Handwriter

txt = """This is a Python program that converts text to handwriting."""
hw = Handwriter(text=txt)
hw.save("demo.png")

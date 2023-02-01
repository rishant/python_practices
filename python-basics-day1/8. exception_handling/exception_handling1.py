from ast import Pass


try:
    print("Hello")
except Exception as exc:
    Pass
finally:
    print("Finally Block")
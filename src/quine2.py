text = """
 This thesis attempts to express a way to relate to the world
 from my own neurodivergent perspective. One that is explained 
 and presented from a neuro-normative point of view, and yet, 
 it can't prove itself. Hopefully it will allow the reader to 
 connect the different topics here contained in an unstructured
 way, following non-linear timelines, as I do.
"""

s = 'text = """{}"""\n\ns = {!r}\nprint(s.format(text, s))'
print(s.format(text, s))
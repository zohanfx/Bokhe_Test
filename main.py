import numpy as np 
from bokeh.plotting import figure, show
from bokeh.models import Div, Spinner, TextInput
from bokeh.layouts import layout 

x = np.random.random(50)
y = np.random.random(50)

p = figure()
points = p.circle(x, y)


div = Div(text="<b><p>Select Size</p></b>")
spinner = Spinner(title="Circle Size", low=0, high=40, step=1,
                  value=points.glyph.size, width=200)

spinner.js_link("value", points.glyph, "size")

textinput = TextInput(value=points.glyph.fill_color, width=200)
textinput.js_link("value", points.glyph, "fill_color")

layout = layout([[div, spinner], [textinput], [p]])

show(layout)
from src.page import Page


page = Page('sample.png', 250)

page.analyze_notes()

page.analyze_sharp_flat_natural()



page.draw_sharp_flat_natural()
page.draw_notes()
page.save('hhh.png')
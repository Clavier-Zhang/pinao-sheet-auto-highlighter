from src.page import Page


page = Page('sample.png', 250)

page.analyze_sharp_flat_natural()
page.analyze_notes()


page.draw_sharp_flat_natural()

page.save('hhh.png')
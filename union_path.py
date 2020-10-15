'''
同じ位置にアンカーポイントが存在しているので、結合する。
'''
from defcon import Font
from pathops import union, difference

font = Font('Eorzea.ufo')

for glyph in font:
    contours = list(glyph)

    pen = glyph.getPen()
    glyph.clearContours()

    for index, contour in enumerate(contours):
        is_clockwise = contour.clockwise
        union([contour], pen)

        if is_clockwise:
            glyph[index].reverse()

    glyph.dirty = True

font.save()

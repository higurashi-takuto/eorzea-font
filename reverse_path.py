'''
OpenType Font としてパスの向きが逆なので、反転する。
'''
from defcon import Font

font = Font('Eorzea.ufo')

for glyph in font:
    for contour in glyph:
        contour.reverse()
    glyph.dirty = True

font.save()

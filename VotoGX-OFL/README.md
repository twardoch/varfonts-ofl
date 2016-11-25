# Variable OpenType test fonts

## Voto Serif GX

The **Voto Serif GX** is a variable OpenType font based on [Noto Serif & Noto Serif Display](https://github.com/googlei18n/noto-source). Noto Serif serve as the `opsz` axis master =12, and Noto Serif Display as the `opsz` axis master =72. In the Voto Serif fonts, compared to the original Noto fonts, some incompatible glyphs in the uprights have been compatibilized, some have been removed.

The `.glyphs` sources are published. The `01-merged` folder has the sources for the original designs, which have the `wdth` axis bounds 70 and 100. The `02-wdth-extrapol` folder has the sources extrapolated to `wdth` 50 and 130. This of course results in some deficiencies, especially in the Light masters.

A `makeInstanceMapForGlyphsapp.py` is included which produces a handy list of instances which can be pasted into Glyphsapp’s Font Info.

Currently, only the upright font can be built, and even that not fully — without any `GPOS`. `fontmake` fails when trying to merge `mark`, `mkmk` and `kern`, regardless of whether built using `feaLib` or `afdko` (I had to tweak `ufo2ft` to disable `autoFeatures` in order to build the fonts).

But thanks to the wide range of `wdth` and `wght`, and the `opsz` axis, the font can serve as a good source of experiments.

### License

The fonts are licensed under the [SIL Open Font License version 1.1](./fonts.LICENSE). The tools and other content are licensed under the [Apache License version 2.0](./other.LICENSE).

Copyright © 2016 by [Adam Twardoch](https://github.com/twardoch/) and the original authors. 

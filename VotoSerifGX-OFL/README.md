# Variable OpenType test fonts

## Voto Serif GX (OFL)

![Voto Serif GX](./doc/VotoSerifGX-OFL.gif)

### ** > [Download VotoSerifGX.ttf ](https://github.com/twardoch/varfonts-ofl/blob/master/VotoSerifGX-OFL/ttf/VotoSerifGX.ttf?raw=true)**

The **Voto Serif GX** is a variable OpenType font based on [Noto Serif & Noto Serif Display](https://github.com/googlei18n/noto-source). Noto Serif serve as the `opsz` axis master =12, and Noto Serif Display as the `opsz` axis master =72.

### What’s included?

1. The `ttf` folder has the working font in Variable OpenType TT (.ttf) format.

2. The `src` folder has some sources and the `tools` folder has little helper tools.

3. The `00-original` folder has the original `.glyphs` sources, with 2 axes each (weight and width), having 4 masters each (same for Italics). Most glyphs in the uprights are compatible, some have more or less trivial compatibility issues that should be resolvable via prepolation. (Note that there are interesting cases e.g. in one font a glyph is composite, in another outline-based).

4. The `01-merged` folder has the sources for the original designs, which have the `wdth` axis bounds 70 and 100. In the Voto Serif fonts, compared to the original Noto fonts, some incompatible glyphs in the uprights have been compatibilized, some have been removed. But the glyphset is still large, >3,000 glyphs.

5. The `02-wdth-extrapol` folder has the sources extrapolated to `wdth` 50 and 130, and the number per axis reduced to 3 instead of 4 (so 12 masters instead of 16). I’ve reduced the number of masters because of UI deficiencies in Glyphsapp, but also for reasons of practicality.

6. A `makeInstanceMapForGlyphsapp.py` tool is included which produces a handy list of instances which can be pasted into Glyphsapp’s Font Info. With this tool, I’ve made 7 x 9 x 9 = 567 predefined instances that are included in the font (and in the `02-wdth-extrapol` sources). The instances are named `<pointSize> <widthClass> <weightClass>` e.g. `24 5 400`, rather than using traditional text descriptors. This number of instances may be exaggerated but is relatively realistic for big font projects. There are in some design deficiencies, especially in the Light masters, due to the extrapolation, but these can be ignored.

7. `03-opsz-extrapol-progress` is unfinished.

8. I tried building the fonts with Google’s [`fontmake`](https://github.com/googlei18n/fontmake/) toolchain. Currently, only the upright font can be built, and even that not fully — without any `GPOS`. `fontmake` fails when trying to merge `mark`, `mkmk` and `kern`, regardless of whether built using `feaLib` or `afdko` (I had to tweak `ufo2ft` to disable `autoFeatures` in order to build the fonts). This font presents a good test case for authors of tools that do `GPOS` table generation and blending for variable fonts.

Despite the deficiencies, thanks to the wide range of `wdth` and `wght`, and the `opsz` axis, the font can serve as a good source of experiments.

### License

The fonts are licensed under the [SIL Open Font License version 1.1](./fonts.LICENSE). The tools and other content are licensed under the [Apache License version 2.0](./other.LICENSE).

Copyright © 2016 by [Adam Twardoch](https://github.com/twardoch/) and the original authors.

# Variable OpenType test fonts

## Test fonts in OpenType TT (.ttf) format with OpenType Variation font tables (beta)

These fonts are conversions of fonts published under the OFL into the OpenType TT (.ttf) format with OpenType Variation font variation tables (`gvar`, `fvar`), which allows “MultipleMaster”-like functionality aka responsive fonts. These fonts are intended for testing purposes, and do not fully conform to the OT 1.8 spec.

### Using

The variation aspect is supported in Mac OS X, iOS, most recent versions of FreeType and in Microsoft Edge for Windows 10 AU. Specifically, they can be tested in the following environments:

* [http://www.axis-praxis.org]() (browser-based tool requiring WebKit Nightly and macOS Sierra, by [@lorp](https://github.com/lorp/)
* [https://github.com/googlei18n/fontview]() (simple desktop GUI tool by [@brawer](https://github.com/brawer))

### Building

Principally, these fonts can be built using [https://github.com/googlei18n/fontmake]() — some extra tools are included.

### License

The fonts are licensed under the [SIL Open Font License version 1.1](./fonts.LICENSE). The tools and other content are licensed under the [Apache License version 2.0](./other.LICENSE).

Copyright © 2016 by [Adam Twardoch](https://github.com/twardoch/) and the original authors.

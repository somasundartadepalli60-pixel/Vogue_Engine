"""Domain 2: Color and Seasonal Harmony."""
from vogue_engine.core.engine.schemas.style_payload import DomainColor
from vogue_engine.core.engine.schemas.layout import GridCoordinate
from vogue_engine.core.vision.photometrics import Season, Undertone, ColorimetricProfile
from vogue_engine.core.engine.matrices import (
    AUTUMN_SWATCHES,
    WINTER_SWATCHES,
    SPRING_SWATCHES,
    SUMMER_SWATCHES,
)

class ColorDomainCalculator:
    @staticmethod
    def calculate(photo: ColorimetricProfile) -> DomainColor:
        catalog = {
            Season.AUTUMN: AUTUMN_SWATCHES,
            Season.WINTER: WINTER_SWATCHES,
            Season.SPRING: SPRING_SWATCHES,
            Season.SUMMER: SUMMER_SWATCHES,
        }
        palette = catalog.get(photo.season, AUTUMN_SWATCHES)

        return DomainColor(
            palette_title=f"Editorial {photo.season.value} Spectrum ({photo.undertone.value} Base)",
            season=photo.season.value,
            primary_swatches=palette["primary"],
            avoid_swatches=palette["avoid"],
            neutral_anchors=palette["neutrals"],
            swatch_mosaic_coordinates=[
                GridCoordinate(x=5.0, y=10.0, width=42.0, height=35.0),
                GridCoordinate(x=52.0, y=10.0, width=42.0, height=35.0),
            ]
        )

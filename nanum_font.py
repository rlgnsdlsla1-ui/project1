"""Matplotlib helper to use bundled Nanum fonts without sudo privileges."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

from matplotlib import font_manager, rcParams

DEFAULT_FONT_DIR = Path(__file__).with_name("fonts") / "nanum"
DEFAULT_FAMILY = "NanumGothic"


def _iter_font_files(font_dir: Path) -> Iterable[Path]:
    """Yield available TTF font files under the given directory."""
    yield from sorted(font_dir.glob("*.ttf"))


def register_nanum_fonts(font_dir: str | Path = DEFAULT_FONT_DIR) -> List[Path]:
    """Register every Nanum font that ships with this repository.

    Parameters
    ----------
    font_dir:
        Directory that contains the downloaded Nanum ``.ttf`` files.

    Returns
    -------
    list[pathlib.Path]
        Paths of every font successfully registered with Matplotlib.
    """
    directory = Path(font_dir).expanduser().resolve()
    if not directory.exists():
        raise FileNotFoundError(f"Font directory not found: {directory}")

    font_paths = list(_iter_font_files(directory))
    if not font_paths:
        raise FileNotFoundError(
            f"No '*.ttf' files were found under {directory}. "
            "Download Nanum fonts into that directory first."
        )

    for path in font_paths:
        font_manager.fontManager.addfont(str(path))

    return font_paths


def use_nanum_font(
    font_family: str = DEFAULT_FAMILY,
    font_dir: str | Path = DEFAULT_FONT_DIR,
    axes_unicode_minus: bool = False,
) -> List[Path]:
    """Register Nanum fonts and set Matplotlib defaults to use them.

    Examples
    --------
    >>> from nanum_font import use_nanum_font
    >>> use_nanum_font()
    >>> import matplotlib.pyplot as plt
    >>> plt.figure()
    >>> plt.text(0.5, 0.5, "안녕하세요", ha="center")
    >>> plt.show()
    """
    font_paths = register_nanum_fonts(font_dir)

    rcParams["font.family"] = [font_family]
    rcParams["axes.unicode_minus"] = axes_unicode_minus

    return font_paths


__all__ = ["DEFAULT_FONT_DIR", "DEFAULT_FAMILY", "register_nanum_fonts", "use_nanum_font"]

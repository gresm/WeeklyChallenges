from functools import lru_cache
from pathlib import Path
from random import uniform

import pygame

SUBMISSION_DIR = Path(__file__).parent
ASSETS = SUBMISSION_DIR.parent / "assets"


@lru_cache()
def load_image(name: str, scale=1):
    image = pygame.image.load(ASSETS / f"{name}.png")
    if scale != 1:
        new_size = image.get_width() * scale, image.get_height() * scale
        image = pygame.transform.scale(image, new_size)
    return image.convert_alpha()


@lru_cache()
def rotate_image(surf, angle: int):
    """Rotate function that caches its results for performance."""
    return pygame.transform.rotate(surf, angle)


def clamp(value, mini, maxi):
    """Clamp value between mini and maxi"""
    if value < mini:
        return mini
    elif maxi < value:
        return maxi
    else:
        return value


def random_in_rect(rect):
    """Return a random point uniformly in a rectangle."""
    rect = pygame.Rect(rect)
    return pygame.Vector2(
        uniform(rect.left, rect.right), uniform(rect.top, rect.bottom)
    )


def from_polar(rho, theta):
    """Create a Vector2 from its polar representation."""
    v = pygame.Vector2()
    v.from_polar((rho, theta))
    return v


def clamp_vector(v: pygame.Vector2, max_length):
    """Ensure that a vector ahs a magnitude less than max_length."""
    if v.length() > max_length:
        return v.normalize() * max_length
    return v


def segments(points):
    """Return all the segments made from adjacent pairs of points in the list.
    Also return the segment made of the last and first point."""
    return zip(points, points[1:] + [points[0]])

import sys
from pathlib import Path


try:
    import wclib
except ImportError:
    # wclib may not be in the path because of the architecture
    # of all the challenges and the fact that there are many
    # way to run them (through the showcase, or on their own)

    ROOT_FOLDER = Path(__file__).parent.parent.parent
    sys.path.append(str(ROOT_FOLDER))
    import wclib

# This line tells python how to handle the relative imports
# when you run this file directly.
__package__ = "02-particle-system." + Path(__file__).parent.name

# ---- Recommended: don't modify anything above this line ---- #

# Metadata about your submission
__author__ = "CozyFractal#0042"  # Put yours!
__achievements__ = [  # Uncomment the ones you've done
    # "Casual",
    # "Ambitious",
    # "Adventurous",
]

# To import the modules in yourname/, you need to use relative imports,
# otherwise your project will not be compatible with the showcase.
# noinspection PyPackages
from .objects import *
from .particles_manager import *
from .utils import *

BACKGROUND = 0x0F1012


def mainloop():
    pygame.init()

    player = Player((SIZE[0] / 2, SIZE[1] / 2), (0, 0))
    # The state is just a collection of all the objects in the game
    state = State(player, FpsCounter(60), *Asteroid.generate_many())

    particle_manager = ParticleManager(player_instance=player)
    font = pg.font.Font(SUBMISSION_DIR / "regular.ttf", 20)

    while True:
        screen, events = yield
        for event in events:
            if event.type == pygame.QUIT:
                return
            else:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        particle_manager.start_explosion(event.pos)
                    elif event.button == 3:
                        particle_manager.start_mini_explosion(event.pos)
                state.handle_event(event)

        # Note: the logic for collisions is in the Asteroids class.
        # This may seem arbitrary, but the only collisions that we consider
        # are with asteroids.
        state.logic()

        screen.fill(BACKGROUND)

        particle_manager.update(screen)

        state.draw(screen)
        screen.blit(
            font.render(f"Particles : {len(particle_manager.particles)}", True, (255, 0, 0)),
            (0, 50),
        )


if __name__ == "__main__":
    wclib.run(mainloop())

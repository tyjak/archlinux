# -*- coding: utf-8 -*-

import subprocess
import os.path
#import netifaces

from i3pystatus import Status
from i3pystatus.updates import yay, pacman

status = Status(standalone=True)


status.register("updates",
        backends = [yay.Yay()]
        )

status.register("updates",
        backends = [yay.Yay(), pacman.Pacman()]
        )

status.register("updates",
        backends = [yay.Yay(False)]
        )

status.register("updates",
        backends = [yay.Yay(False)]
        )

status.register("updates",
        backends = [yay.Yay()]
        )

status.register("updates",
        backends = [pacman.Pacman()]
        )


status.run()

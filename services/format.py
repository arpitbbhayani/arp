class ArpHeader(object):
    def __init__(self):
        pass

    def from_image_bytes(cls, data):
        return cls()


class Arp(object):
    def __init__(self):
        self.header = None

    @classmethod
    def from_image(cls, path, max_colors=256):
        return cls()


def is_arp(path):
    return False

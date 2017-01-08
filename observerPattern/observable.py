class Observable(object):
    def __init__(self):
        self.observers = []
        self.has_changed = False

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def set_changed(self):
        self.has_changed = True

    def clear_changed(self):
        self.has_changed = False

    def notify_observers(self, *args, **kwargs):
        if self.has_changed:
            for observer in self.observers:
                observer.update(*args, **kwargs)
            self.clear_changed()

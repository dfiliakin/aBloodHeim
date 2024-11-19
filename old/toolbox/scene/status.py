class Status:
    def __init__(
        self, scene_name, done=False, success=None, action="undefined", msg=""
    ):
        self.scene_name = scene_name
        self.done = done
        self.success = success
        self.action = action
        self.msg = msg

    def __str__(self):
        return f"Status(scene_name='{self.scene_name}', done={self.done}, success={self.success}, action={self.action})"

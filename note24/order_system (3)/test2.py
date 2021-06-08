class MacroCommand():
    def __init__(self, commands:list):
        self.commands = commands

    def __call__(self):
        for command in self.commands:
            command()

macroCommand = MacroCommand()
macroCommand()